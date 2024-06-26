from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD664AcidNumber60mLInflection(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D664"

    @property
    def analyte_name(self):
        return "Acid Number 60 mL Inflection"

    def _calculate_repeatability(self):
        return 0.1938 * (self.average ** 0.8199)

    def _calculate_reproducibility(self):
        return 0.4022 * (self.average ** 0.8199)

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
