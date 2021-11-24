# Copyright 2021 Hsuan-Ting Lu.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Stores a dataset."""
import pathlib
import dask.dataframe
import numpy as np
import pandas as pd


class DatasetFolder:
    CACHE_DIR = "cache"

    def __init__(self, root_dir: pathlib.Path, use_cache: bool = True):
        """
        reads CSV files in a directory,
        and caches them as Apache Parquet files if possible
        """
        self.root_dir = root_dir
        self.cache_dir = root_dir.joinpath(self.CACHE_DIR)

        csv_list = root_dir.glob("*.csv")
        assert all(map(lambda csv: csv.is_file(), csv_list))
        self.cache_dir.mkdir(exist_ok=True)
        csv_cached = len(self.cache_dir.glob("*.parquet")) != 0

        if not use_cache or not csv_cached:
            df = dask.dataframe.read_csv(
                csv_list,
                include_path_column="file_path",
                header=0,
                #
                # NOTE: in order to fix 'No.' later,
                #         when concatenating multiple log files
                index_col=False,
                #
                usecols=["No.", "Time", "Ticks", "Info"],
                dtype={
                    "No.": np.uint32,
                    "Time": np.float64,
                    "Ticks": pd.UInt32Dtype(),
                    "Info": pd.StringDtype()
                },
                na_filter=True,
                verbose=True,
                skip_blank_lines=True,
            )
            df = df.dropna(axis="index", how="any", subset="Ticks")
            df = df.astype({"Ticks": np.uint32})
            df['No'] = df['No.'].apply()  # FIXME: 'file_path'
            df = df.repartition(partition_size="100MB")
            df = df.persist()
            df.to_parquet(
                str(self.cache_dir),
                engine="pyarrow",
                compression="snappy",
                write_index=True,
                append=False,
                overwrite=True,
                write_metadata_file=True,
            )

        self.df = dask.dataframe.read_parquet(
            str(self.cache_dir),
            columns=["No", "Ticks", "Info"],
            index=True,
            engine="pyarrow",
            gather_statistics=True,
            ignore_metadata_file=False,
            aggregate_files=True,
        )

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        # TODO: review this
        return self.df.iloc[idx]
