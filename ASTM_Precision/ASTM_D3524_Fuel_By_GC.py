from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD3524FuelByGC(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D3524"

    @property
    def analyte_name(self):
        return "Fuel By GC"

    def _calculate_repeatability(self):
        return 0.3

    def _calculate_reproducibility(self):
        return 1.6

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
