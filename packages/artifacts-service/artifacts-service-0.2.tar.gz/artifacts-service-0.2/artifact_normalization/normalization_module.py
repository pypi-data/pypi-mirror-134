import injector

from artifact_normalization.normalization_manager import NormalizationManager
from artifact_normalization.normalizers.dual_value_dict_normalizer import DualValueDictNormalizer
from artifact_normalization.normalizers.process_tree_normalizer import ProcessTreeNormalizer
from artifacts.config import Config


class NormalizationModule(injector.Module):
    """
    This class is used to define all the bindings between classes and their wanted instances
    """

    @injector.provider
    def provide_normalization_manager(self,
                                      process_tree_normalizer: ProcessTreeNormalizer,
                                      network_normalizer: DualValueDictNormalizer) -> NormalizationManager:
        return NormalizationManager(process_tree_normalizer, network_normalizer)

    @injector.provider
    def provide_network_normalizer(self) -> DualValueDictNormalizer:
        return DualValueDictNormalizer()

    @injector.provider
    def provide_process_tree_normalizer(self, _config: Config) -> ProcessTreeNormalizer:
        return ProcessTreeNormalizer(_config.separator, _config.process_tree_combination_length)
