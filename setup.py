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
"""Install Tohru."""

import setuptools

setuptools.setup(
    name="tohru",
    version="0.1.0",
    description="Tohru",
    long_description=(
        "Tohru helps you build a data analysis ecosystem around WireShark."),
    author="Hsuan-Ting Lu",
    author_email="hsuan.ting.lu.ee05@g2.nctu.edu.tw",
    url="https://github.com/HsuanTingLu/tohru",
    license="Apache-2.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
    ],
    extras_require={
        "tests": [
            "pylint",
            "pytest",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords="data analysis wireshark",
)
