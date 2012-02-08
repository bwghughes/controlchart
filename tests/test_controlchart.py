#!/usr/bin/python

# <test_controlchart.py>
# Created: January 7, 2011
# Version: 0.0.1
# By:  (bwghughes@gmail.com)

import os
import sys
from nose.tools import raises


def setup():
    sys.path.insert(0, os.path.pardir)


def teardown():
    sys.path.remove(os.path.pardir)

from controlchart import ControlChart, InvalidChartDataError


class TestControlChart(object):

    def setup(self):
        self.c = ControlChart([1, 2, 3, 4, 5])

    def teardown(self):
        pass

    @raises(InvalidChartDataError)
    def test_init_blows_with_no_data(self):
        ControlChart(data=None)

    @raises(InvalidChartDataError)
    def test_init_blows_with_empty_data(self):
        ControlChart(data=[])

    @raises(InvalidChartDataError)
    def test_init_blows_with_non_numeric_data(self):
        ControlChart(data=['a', 'b', 'c', 'e'])

    def test_mean_returns_correct_values(self):
        assert self.c.mean() == 3.0
