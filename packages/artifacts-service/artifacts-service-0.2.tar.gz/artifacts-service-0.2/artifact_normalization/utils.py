from typing import Generator
from typing import List

from common.utilities import xxhash64

from artifact_normalization.data_types import ArtifactRecord


# todo: can we move this encoding to common?
def xxhash_string(value: str) -> str:
    return xxhash64(value.encode('utf-8'))


def format_artifacts(artifact_type: str, values: List[str]) -> Generator:
    """
    return value: generator of tuples [artifact_type, artifact_value, artifact_xxhash]
    """
    yield from (ArtifactRecord(artifact_type, value, xxhash_string(value)) for value in values)
