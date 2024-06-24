from __future__ import annotations
from typing import Union, List
import abc
from abc import ABC, abstractmethod


class AbstractASTM(ABC):
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        AbstractASTM.registry[cls.__name__] = cls

    @property
    @abstractmethod
    def astm_method_number(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def analyte_name(self):
        raise NotImplementedError

    def __init__(self):
        self.data: List[Union[int, float]]
        self.outlier_rejection()
        self.average = self._calculate_average()
        self.repeatability = self._calculate_repeatability()
        self.reproducibility = self._calculate_reproducibility()

    def _calculate_average(self):
        """Calculates the average value for the data
        """
        sum = 0
        count = 0
        for datapoint in self.data:
            sum += datapoint
            count += 1

        return sum / count

    @abc.abstractmethod
    def _calculate_repeatability(self):
        """Calculates the repeatability limit for the data"""
        raise NotImplementedError

    @abc.abstractmethod
    def _calculate_reproducibility(self):
        """Calculates the reproducibility limit for the data"""
        raise NotImplementedError

    def validate_data(self):
        """
        Returns the dictionary of invalid datapoints
        """
        invalid = {}

        for point in self.data:
            if abs(point - self.average) > self.repeatability:
                invalid.setdefault('r', [])
                invalid['r'].append(point)
            if abs(point - self.average) > self.reproducibility:
                invalid.setdefault('R', [])
                invalid['R'].append(point)

        if len(invalid.values()) > 0:
            return invalid
        else:
            return "All datapoints are valid"

    def outlier_rejection(self):
        pass
