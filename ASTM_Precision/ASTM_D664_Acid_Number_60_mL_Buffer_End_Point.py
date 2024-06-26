from typing import List, Union

from .abstractASTM import AbstractASTM


class ASTMD664AcidNumber60BufferEndPoint(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D664"

    @property
    def analyte_name(self):
        return "Acid Number 60 mL Buffer End Point"

    def __init__(self, data: List[Union[int, float]]) -> None:
        self.data = data
        super().__init__()

    def _calculate_repeatability(self):
        return 0.3456 * (self.average ** 0.9758)

    def _calculate_reproducibility(self):
        return 0.5542 * (self.average ** 0.9758)

    def _in_domain(self, value: Union[int, float]) -> bool:
        return 0 <= value <= 2
