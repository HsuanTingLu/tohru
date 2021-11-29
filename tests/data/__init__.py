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
"""Test data generator"""

from os import path
import pathlib

import numpy as np
import pandas as pd


def generate_test_data(*, overwrite=False, rows_per_file=700_000, partitions=4):
    test_data_dir = pathlib.Path(__file__).parent

    test_data_names = [
        "single",
        *[f"partition_{i}" for i in range(1, partitions + 1)],
    ]

    rng = np.random.default_rng()
    for file_name in test_data_names:
        test_data = test_data_dir.joinpath(f"{file_name}.csv")

        if overwrite or not test_data.is_file():
            idx = np.arange(rows_per_file, dtype=np.uint64)
            time_stamps = np.cumsum(
                np.add(
                    np.clip(
                        rng.lognormal(mean=0., sigma=1., size=rows_per_file), 0,
                        10),
                    3,
                ))
            df = pd.DataFrame({
                "No.": idx,
                "Time": time_stamps,
                "Ticks": np.multiply(time_stamps, 1000),
                "Type": "LOGMSG",
                "Length": 126,
                "Info": "Wubba Lubba Dub Dub!!",
            })

            # Pick some rows to be txt_msg and other typed as log_msg
            txt_msg_indexes = np.sort(
                rng.integers(0,
                             rows_per_file,
                             size=int(rows_per_file * 0.05),
                             dtype=np.uint64),)

            for i in txt_msg_indexes:
                df.at[i, "Ticks"] = None
                df.at[i, "Type"] = "TXTMSG"
                df.at[i, "Info"] = "Abracadabra!!"

            df.to_csv(test_data, index=False)


if __name__ != "__main__":
    generate_test_data(overwrite=False, rows_per_file=70_000, partitions=3)
