# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

"""The Worker type enum"""

from enum import Enum


class WorkerType(str, Enum):
    """A simple enum for 1:1 Worker to type mapping.

    Note:
        Custom types should be placed in the CUSTOM TYPES section.
        This will reduce merge conflicts when merging in upstream changes.
    """

    LOCAL = "local"

    # BEGIN CUSTOM TYPES
    # END CUSTOM TYPES
