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
"""Tests single and multiple log file inputs"""

import tohru.data.datasets


class TestDataset:

    def test_single_file_fixture(self, single_file_dataset_dir):
        """Tests if the single log file fixture is working."""
        assert len(list(single_file_dataset_dir.glob("single.csv"))) == 1

    def test_multi_file_fixture(self, multi_file_dataset_dir):
        """Tests if the partitioned log file fixture is working."""
        assert len(list(multi_file_dataset_dir.glob("multi_*.csv"))) > 1

    def test_read_single_file_without_cache(self, single_file_dataset_dir):
        """Test reading single log files and paritioned log files."""
        dataset = tohru.data.datasets.DatasetFolder(
            root_dir=single_file_dataset_dir,
            use_cache=False,
        )

    def test_read_multiple_files_without_cache(self, multi_file_dataset_dir):
        """Test reading single log files and paritioned log files."""
        dataset = tohru.data.datasets.DatasetFolder(
            root_dir=multi_file_dataset_dir,
            use_cache=False,
        )

    def test_read_single_file_with_cache(self, single_file_dataset_dir):
        """Test reading single log files and paritioned log files."""
        dataset = tohru.data.datasets.DatasetFolder(
            root_dir=single_file_dataset_dir,
            use_cache=True,
        )

    def test_read_multiple_files_with_cache(self, multi_file_dataset_dir):
        """Test reading single log files and paritioned log files."""
        dataset = tohru.data.datasets.DatasetFolder(
            root_dir=multi_file_dataset_dir,
            use_cache=True,
        )
