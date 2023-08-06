from enum import auto
from typing import NamedTuple

from common.string_enum import StringEnum


class ArtifactType(StringEnum):
    FILE_ACTIVITY_READ = auto()
    FILE_ACTIVITY_WRITE = auto()
    FILE_ACTIVITY_DELETE = auto()
    REGISTRY_ACTIVITY_READ = auto()
    REGISTRY_ACTIVITY_WRITE = auto()
    REGISTRY_ACTIVITY_DELETE = auto()
    NETWORK = auto()
    PROCESS_TREE = auto()


class ArtifactRecord(NamedTuple):
    artifact_type: str
    artifact_value: str
    artifact_xxhash_value: str
