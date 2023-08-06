from functools import reduce
from typing import Set

import artifact_normalization
from artifact_normalization.data_types import ArtifactRecord
from artifact_normalization.data_types import ArtifactType
from artifact_normalization.normalizers.dual_value_dict_normalizer import DualValueDictNormalizer
from artifact_normalization.normalizers.process_tree_normalizer import ProcessTreeNormalizer
from artifact_normalization.utils import format_artifacts


class NormalizationManager:
    def __init__(self,
                 process_tree_normalizer: ProcessTreeNormalizer,
                 network_normalizer: DualValueDictNormalizer):
        self._process_tree_normalizer = process_tree_normalizer
        self._network_normalizer = network_normalizer
        self._normalizers_by_artifact_type = {
            ArtifactType.NETWORK: [self._network_normalizer],
            ArtifactType.PROCESS_TREE: [self._process_tree_normalizer],
            ArtifactType.FILE_ACTIVITY_READ: [],
            ArtifactType.FILE_ACTIVITY_WRITE: [],
            ArtifactType.FILE_ACTIVITY_DELETE: [],
            ArtifactType.REGISTRY_ACTIVITY_READ: [],
            ArtifactType.REGISTRY_ACTIVITY_WRITE: [],
            ArtifactType.REGISTRY_ACTIVITY_DELETE: [],
        }

    @property
    def version(self):
        return artifact_normalization.__version__

    def normalize(self, artifacts: list, artifact_type: ArtifactType) -> Set[ArtifactRecord]:
        normalizers = self._normalizers_by_artifact_type[artifact_type]
        return set(
            format_artifacts(
                artifact_type,
                reduce(
                    lambda current_artifacts, function: function.normalize(current_artifacts),
                    normalizers,
                    artifacts
                )
            )
        )
