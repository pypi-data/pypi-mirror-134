# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

"""The implementation for a LocalWorker."""

import json
import os
import tempfile
from argparse import ArgumentParser, Namespace
from subprocess import Popen
from typing import List, Optional, Sequence

from autotransform.batcher.base import Batch
from autotransform.common.cachedfile import CachedFile
from autotransform.schema.schema import AutoTransformSchema
from autotransform.worker.runnable import RunnableWorker
from autotransform.worker.type import WorkerType


class LocalWorker(RunnableWorker):
    """A Worker that is run locally by the Runner and merely executes the batches in a subprocess.

    Attributes:
        data_file (str): The path to a temp file containing the information required to run the
            Worker
        proc (Optional[Popen]): A handle of the subprocess the Worker spawned to execute it's work
    """

    data_file: str
    proc: Optional[Popen]

    def __init__(self, data_file: str):
        """A simple constructor

        Args:
            data_file (str): The path to a temp file containing the information required to run the
                Worker
        """
        RunnableWorker.__init__(self)
        self.data_file = data_file
        self.proc = None

    def is_finished(self) -> bool:
        """Checks whether the subprocess has finished

        Returns:
            bool: Returns True if the subprocess is complete
        """
        proc = self.proc
        assert proc is not None
        return proc.poll() is not None

    def start(self) -> None:
        """Spawns a subprocess using autotransform.instance to run the work"""

        # pylint: disable=consider-using-with

        self.proc = RunnableWorker.spawn_proc(WorkerType.LOCAL, [self.data_file])

    @staticmethod
    def spawn_from_batches(
        schema: AutoTransformSchema, batches: List[Batch]
    ) -> Sequence[RunnableWorker]:
        """Sets up a data file with the batches and schema, creating a LocalWorker based on
        this data file.

        Args:
            schema (AutoTransformSchema): The Schema that is being run
            batches (List[Batch]): The Batches that have been found for the Schema

        Returns:
            Sequence[RunnableWorker]: A list containing a single Worker to execute all Batches
        """
        # pylint: disable=consider-using-with

        data_file = tempfile.NamedTemporaryFile(mode="w+", encoding="utf8", delete=False)
        encodable_batches = [
            {"files": [file.path for file in batch["files"]], "metadata": batch["metadata"]}
            for batch in batches
        ]
        full_data = {"batches": encodable_batches, "schema": schema.bundle()}
        json.dump(full_data, data_file)
        data_file.close()

        return [LocalWorker(data_file.name)]

    def kill(self):
        """Removes the temp file and kills the subprocess."""
        os.unlink(self.data_file)
        proc = self.proc
        if proc is not None:
            proc.kill()

    @staticmethod
    def _parse_arguments(parser: ArgumentParser) -> Namespace:
        """Adds the argument to allow access to the data file

        Args:
            parser (ArgumentParser): The parser with previously added arguments

        Returns:
            Namespace: The arguments for the Worker
        """
        parser.add_argument(
            "data_file",
            metavar="data_file",
            type=str,
            help="The file containing a JSON encoded batch",
        )
        return parser.parse_args()

    @staticmethod
    def main(args: Namespace) -> None:
        """Runs the local version of the Worker

        Args:
            args (Namespace): The arguments required to run the Worker
        """
        with open(args.data_file, "r", encoding="utf8") as data_file:
            data = json.loads(data_file.read())
            schema = AutoTransformSchema.from_bundle(data["schema"])
            encoded_batches = data["batches"]
            batches: List[Batch] = [
                {
                    "files": [CachedFile(path) for path in batch["files"]],
                    "metadata": batch["metadata"],
                }
                for batch in encoded_batches
            ]
            for batch in batches:
                schema.execute_batch(batch)
