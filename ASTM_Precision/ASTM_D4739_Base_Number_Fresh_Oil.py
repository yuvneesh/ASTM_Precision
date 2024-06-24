from __future__ import annotations

from typing import List, Union

from .abstractASTM import AbstractASTM


class ASTMD4739BaseNumberFreshOil(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D4739"

    @property
    def analyte_name(self):
        return "Base Number Fresh Oil"

    def __init__(self, data: List[Union[int, float]]) -> None:
        self.data = data
        super().__init__()

    def _calculate_repeatability(self):
        repeatability = 0.11 * ((self.average + 0.0268) ** 0.79)
        return repeatability

    def _calculate_reproducibility(self):
        reproducibility = 0.42 * ((self.average + 0.0268) ** 0.79)
        return reproducibility
