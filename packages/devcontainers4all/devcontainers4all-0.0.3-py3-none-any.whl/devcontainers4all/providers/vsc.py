"""Visual Studio Code implementations
"""
import pathlib

import commentjson
from logzero import setup_logger

from ..interfaces import DevContainer

# pylint: disable=too-few-public-methods


class Manifest(DevContainer):
    """A representation of the devcontainer.json manifest"""

    def __init__(
        self, location: pathlib.Path, manifest_file="devcontainer.json"
    ) -> None:
        super().__init__()

        self.__logger = setup_logger(name="VisualStudioManifest")

        self.__logger.debug(
            "Using VisualStudioCode Manifest %s ", location.resolve() / manifest_file
        )

        with open(
            pathlib.Path(location, manifest_file), "r", encoding="utf8"
        ) as manifest:
            # VSC DevContainer manifest containes commnets, the standard json module cannot be used
            self.__manifest = commentjson.load(manifest)

    def get(self, key):
        return self.__manifest[key]
