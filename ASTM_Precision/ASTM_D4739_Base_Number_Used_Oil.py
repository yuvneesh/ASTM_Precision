from .abstractASTM import AbstractASTM


class ASTMD4739BaseNumberUsedOil(AbstractASTM):
    @property
    def astm_method_number(self):
        return "D4739"

    @property
    def analyte_name(self):
        return "Base Number Used Oil"

    def _calculate_repeatability(self):
        repeatability = 0.22 * (self.average ** 0.47)
        return repeatability

    def _calculate_reproducibility(self):
        reproducibility = 1.53 * (self.average ** 0.47)
