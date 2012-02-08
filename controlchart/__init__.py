__author__ = 'Ben Hughes <bwghughes@gmail.com>'
__version__ = '0.1'

from collections import deque
from decimal import Decimal


STD_DEV = Decimal(2.66)


class InvalidChartDataError(Exception):
    pass


class ControlChart(object):
    def __init__(self, data=None):
        try:
            assert data, 'Data cannot be None'
            assert len(data) > 0, 'Data cannot be None'
            assert any([isinstance(x, int) for x in data]), 'Data can only be ints or floats'
            self.data = data
            self._rod_mean = None
        except AssertionError, e:
            raise InvalidChartDataError(e)

    def _get_range_of_difference(self):
        shifted_data = deque(self.data, len(self.data))
        shifted_data.appendleft(0)
        rod = [abs(a - b) for a, b in zip(self.data, shifted_data)]
        del rod[0]  # Delete the first one, as we don't need it in the calculation.
        return rod

    @property
    def mean(self):
        return Decimal(sum(self.data) / len(self.data))

    @property
    def range_of_difference_mean(self):
        if not self._rod_mean:
            range_of_difference = self._get_range_of_difference()
            self._rod_mean = Decimal(sum(range_of_difference) / len(range_of_difference))
            return self._rod_mean
        else:
            return self._rod_mean

    @property
    def upper_control_limit(self):
        return Decimal(self.mean + (self.range_of_difference_mean * STD_DEV))

    @property
    def lower_control_limit(self):
        return Decimal(self.mean - (self.range_of_difference_mean * STD_DEV))
