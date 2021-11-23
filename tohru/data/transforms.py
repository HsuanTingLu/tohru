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
"""Transforms a dataset."""

import numpy as np


class Transform:
    """Base class for transformers"""
    pass


class FixOverflow(Transform):
    """Transformer that fixes integer overflows in a series"""

    def __init__(self,
                 series,
                 min_val: np.integer,
                 max_val: np.integer,
                 step_threshold=None):

        def is_int(x):
            return np.issubdtype(x, np.integer)

        if is_int(max_val) and is_int(min_val):
            if max_val < min_val:
                raise ValueError(
                    f"invalid arguments for {type(self).__name__!r}()"
                    f" with min: '{min_val!r}'"
                    f", max: '{max_val!r}',"
                    "max should not be smaller than min")
        else:
            raise ValueError(f"invalid arguments for {type(self).__name__!r}()"
                             f" with series: '{series!r}'"
                             f", min: '{min_val!r}"
                             f", max: '{max_val!r}'")

        self.max = max_val
        self.min = min_val
        self.step_threshold = step_threshold

    def transform(self):
        pass


class FixRateConversion(Transform):
    pass
