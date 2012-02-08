from collections import deque


class InvalidChartDataError(Exception):
    pass


class ControlChart(object):
    def __init__(self, data=None):
        try:
            assert data, 'Data cannot be None'
            assert len(data) > 0, 'Data cannot be None'
            assert any([isinstance(x, int) for x in data]), 'Data can only be ints or floats'
            self.data = data
            self._ucl = None
            self._lcl = None
        except AssertionError, e:
            raise InvalidChartDataError(e)

    def mean(self):
        return float(sum(self.data) / len(self.data))

    def range_of_difference(self):
        _shifted_data = deque(self.data, len(self.data))
        _shifted_data.appendleft(0)
        _rod = [abs(a - b) for a, b in zip(self.data, _shifted_data)]
        del _rod[0]
        return _rod


