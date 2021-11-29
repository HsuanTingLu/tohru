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

import pathlib

import pytest


class TestDataset:

    def test_create_file(self, single_file_dataset_dir, multi_file_dataset_dir):
        assert len(list(single_file_dataset_dir.glob("single.csv"))) == 1
        assert len(list(multi_file_dataset_dir.glob("multi_*.csv"))) > 1
