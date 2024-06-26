from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD974AcidNumber(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D974"

    @property
    def analyte_name(self):
        return "Acid Number"

    def _calculate_repeatability(self):
        if self.average < 0.1:
            return 0.03
        if 0.1 <= self.average <= 0.5:
            return 0.05
        if 0.5 <= self.average <= 1.0:
            return 0.08
        if 1.0 <= self.average <= 2.0:
            return 0.12

    def _calculate_reproducibility(self):
        if self.average < 0.1:
            return 0.04
        if 0.1 <= self.average <= 0.5:
            return 0.08
        if 0.5 <= self.average <= 2.0:
            return 0.15 * self.average

    def _in_domain(self, value: Union[int, float]) -> bool:
        return 0 < value <= 2.0
