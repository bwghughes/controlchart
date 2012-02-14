__title__ = 'controlchart'
__author__ = 'Ben Hughes <bwghughes@gmail.com>'
__version__ = '0.1'
__build__ = 0x000911
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Ben Hughes'
__docformat__ = 'restructuredtext'

from collections import deque
from decimal import Decimal
from tablib import Dataset

STD_DEV = Decimal(2.66)


class InvalidChartDataError(Exception):
    pass


class ControlChart(Dataset):
    """ """
    def __init__(self, *args, **kwargs):
        if self._validate_args(args):
            try:
                kwargs['header']
            except KeyError:
                kwargs['header'] = "Raw Data"
            super(ControlChart, self).__init__(*args, **kwargs)
            self._rod_mean = None

    def _get_range_of_difference(self):
        """ Calculate the mean of a 1 point shifted moving average """
        the_data = self._data[0].list
        shifted_data = deque(the_data, len(the_data))
        shifted_data.appendleft(0)
        rod = [abs(a - b) for a, b in zip(the_data, shifted_data)]
        del rod[0]  # Delete the first one, as we don't need it in the calculation.
        return rod

    def _calculate_mean(self, data):
        print data[0].list
        return Decimal(sum(data[0].list) / len(data[0].list))

    @property
    def mean(self):
        return self._calculate_mean(self._data)

    @property
    def range_of_difference_mean(self):
        """Calculate the mean of a 1 point shifted moving average.

        .. versionadded:: 0.1
        """
        if not self._rod_mean:
            range_of_difference = self._get_range_of_difference()
            self._rod_mean = Decimal(sum(range_of_difference) / len(range_of_difference))
            return self._rod_mean
        else:
            return self._rod_mean

    @property
    def upper_control_limit(self):
        """Calculate the upper control limit and adds a series to the Dataset.

        .. versionadded:: 0.1
        """
        ucl = Decimal(self.mean + (self.range_of_difference_mean * STD_DEV))
        self._add_series_of_fixed_values(fixed_value=ucl, header='Upper Control Limit')
        return ucl

    @property
    def lower_control_limit(self):
        """ Calculate the lower control limit and adds a series to the Dataset.

        .. versionadded:: 0.1
        """
        lcl = Decimal(self.mean - (self.range_of_difference_mean * STD_DEV))
        self._add_series_of_fixed_values(fixed_value=lcl, header='Lower Control Limit')
        return lcl

    def _add_series_of_fixed_values(self, fixed_value=None, header=None):
        self.append_col([fixed_value for x in xrange(self.height)], header=header)

    def _validate_args(self, args):
        """ Make sure we're only accepting a dataset with numbers in it """
        try:
            assert isinstance(args[0], list)
            assert any([isinstance(x, int) or isinstance(x, float) \
                   or isinstance(x, Decimal) for x in args[0]]), 'Data can only be int, float or Decimal'
            return True
        except AssertionError, e:
            raise InvalidChartDataError(e)

    def append(self, *args):
        """ Append an item to the dataset (requires recalculation)

        .. versionadded:: 0.1
        """
        # Lets add then recalc
        super(ControlChart, self).append(*args)
        self._rod_mean = None
        self._recalculate()

    def _recalculate(self):
        """ Recalculates the ROD, UCL, LCL based on the new values.

        .. versionadded:: 0.1
        """
        pass
