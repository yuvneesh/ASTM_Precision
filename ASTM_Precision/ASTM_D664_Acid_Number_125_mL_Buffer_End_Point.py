from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD664AcidNumber125BufferEndPoint(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D664"

    @property
    def analyte_name(self):
        return "Acid Number 125 mL Buffer End Point"

    def _calculate_repeatability(self):
        return 0.2028 * (self.average ** 1.0513)

    def _calculate_reproducibility(self):
        return 0.3160 * (self.average ** 1.0513)

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
