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
"""Shared fixtures"""

import pathlib

import pytest

import tests.data

DATA_DIR = pathlib.Path(tests.data.__file__).parent


@pytest.fixture(scope="package")
def multi_file_dataset_dir(tmp_path_factory):
    """Return a temporary directory path object
 pointing to the temporary directory storing multiple files."""

    tmp_dir = tmp_path_factory.mktemp("multi_file-")
    tests.data.generate_test_data(partitions=3,
                                  data_dir=DATA_DIR,
                                  rows_per_file=70_000)
    for csv in DATA_DIR.glob("multi_*.csv"):
        tmp_dir.joinpath(csv.name).symlink_to(csv)
    return tmp_dir


@pytest.fixture(scope="package")
def single_file_dataset_dir(tmp_path_factory):
    """Return a temporary directory path object
 pointing to the temporary directory storing a single file."""

    tmp_dir = tmp_path_factory.mktemp("single_file-")
    tests.data.generate_test_data(partitions=1,
                                  data_dir=DATA_DIR,
                                  rows_per_file=70_000)
    for csv in DATA_DIR.glob("single.csv"):
        tmp_dir.joinpath(csv.name).symlink_to(csv)
    return tmp_dir
