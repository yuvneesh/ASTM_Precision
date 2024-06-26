from typing import Union

from .abstractASTM import AbstractASTM


class ASTMD1287pH(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D1287"

    @property
    def analyte_name(self):
        return "pH"

    def _calculate_repeatability(self):
        return 0.1

    def _calculate_reproducibility(self):
        return 0.2

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
