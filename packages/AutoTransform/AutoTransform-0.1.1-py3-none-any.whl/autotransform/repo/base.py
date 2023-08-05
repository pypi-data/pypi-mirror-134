# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

"""The base class and associated classes for Repo components."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Mapping, TypedDict

from autotransform.batcher.base import Batch
from autotransform.repo.type import RepoType


class RepoBundle(TypedDict):
    """A bundled version of the Repo object used for JSON encoding."""

    params: Mapping[str, Any]
    type: RepoType


class Repo(ABC):
    """The base for Repo components.

    Attributes:
        params (Mapping[str, Any]): The paramaters that control operation of the Repo.
            Should be defined using a TypedDict in subclasses
    """

    params: Mapping[str, Any]

    def __init__(self, params: Mapping[str, Any]):
        """A simple constructor.

        Args:
            params (Mapping[str, Any]): The paramaters used to set up the Repo
        """
        self.params = params

    @abstractmethod
    def get_type(self) -> RepoType:
        """Used to map Repo components 1:1 with an enum, allowing construction from JSON.

        Returns:
            RepoType: The unique type associated with this Repo
        """

    @abstractmethod
    def has_changes(self, batch: Batch) -> bool:
        """Check whether any changes have been made to the underlying code based on the Batch.

        Args:
            batch (Batch): The Batch that was used for the transformation

        Returns:
            bool: Returns True if there are any changes to either the files in the Batch or other
                files.
        """

    @abstractmethod
    def submit(self, batch: Batch) -> None:
        """Submit the changes to the Repo (i.e. commit, submit pull request, etc...).
        Only called when changes are present.

        Args:
            batch (Batch): The Batch for which the changes were made
        """

    @abstractmethod
    def clean(self, batch: Batch) -> None:
        """Clean any changes present in the Repo that have not been submitted.

        Args:
            batch (Batch): The Batch for which we are cleaning the repo
        """

    @abstractmethod
    def rewind(self, batch: Batch) -> None:
        """Rewind the repo to a pre-submit state to prepare for executing another Batch. This
        should NOT delete any submissions (i.e. commits should stay present). Only called after a
        submit has been done.

        Args:
            batch (Batch): The Batch for which changes were submitted
        """

    def bundle(self) -> RepoBundle:
        """Generates a JSON encodable bundle.
        If a component's params are not JSON encodable this method should be overridden to provide
        an encodable version.

        Returns:
            RepoBundle: The encodable bundle
        """
        return {
            "params": self.params,
            "type": self.get_type(),
        }

    @staticmethod
    @abstractmethod
    def from_data(data: Mapping[str, Any]) -> Repo:
        """Produces an instance of the component from decoded params. Implementations should
        assert that the data provided matches expected types and is valid.

        Args:
            data (Mapping[str, Any]): The JSON decoded params from an encoded bundle

        Returns:
            Repo: An instance of the Repo
        """
