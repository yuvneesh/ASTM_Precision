from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD664AcidNumber125mLInflection(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D664"

    @property
    def analyte_name(self):
        return "Acid Number 125 mL Inflection"

    def _calculate_repeatability(self):
        return 0.1275 * (self.average ** 1.0431)

    def _calculate_reproducibility(self):
        return 0.2188 * (self.average ** 1.0431)

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
