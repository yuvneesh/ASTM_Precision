from typing import List, Union

from .abstractASTM import AbstractASTM


class ASTMD7946iph(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D7946"

    @property
    def analyte_name(self):
        return "i-pH"

    def __init__(self, data: List[Union[int, float]]) -> None:
        self.data = data
        super().__init__()

    def _calculate_repeatability(self):
        return 0.002662 * (10.1353 - self.average)

    def _calculate_reproducibility(self):
        return 0.1207 * (10.1353 - self.average)

    def _in_domain(self, value: Union[int, float]) -> bool:
        return True
