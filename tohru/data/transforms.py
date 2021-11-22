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

    def __new__(cls, series, **kwargs):
        """
        valid arguments formats:
        1) int_type (an integer class)
        2) max, min (two ints, with max>min)
        3) min, max (two ints, with max>min)
        """

        def is_int(x):
            return np.issubdtype(x, np.integer)

        int_type = kwargs.get("int_type")
        max_val = kwargs.get("max")
        min_val = kwargs.get("min")

        if len(kwargs) == 1 and is_int(int_type):
            int_info = np.iinfo(int_type)
            min_val = int_info.min
            max_val = int_info.max
        elif len(kwargs) == 2 and is_int(max_val) and is_int(min_val):
            if max_val < min_val:
                raise ValueError(
                    f"invalid arguments for {cls.__name__!r}()"
                    f" with min: '{min_val!r}', max: '{max_val!r}'")
        else:
            raise ValueError(
                f"invalid arguments for {cls.__name__!r}()"
                f" with series: '{series!r}', keyword arguments: '{kwargs!r}'")

        instance = super().__new__(cls)
        return instance

    def __init__(self):
        pass

    def transform(self):
        pass


class FixRateConversion(Transform):
    pass
