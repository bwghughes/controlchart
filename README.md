Easy Control Charts
=======================

Statistical Process Control charts are easy to use, and invaluable in understanding the stability of a process. 

This module is designed to make it easy for you convert your data into Control Charts.

Example
--------

from controlchart import ControlChart

data = [56.9, 64.8, 45.8, 54.3, 59.8, 49.5, 67.5, 55.5, 59.8, 62.5, 61.5, 59.5, 54.3, 49.5, 52.4, 58.6, 60.2, 61.3, 55.4, 49.6]

chart = ControlChart(data)
chart.upper_control_limit = 74.393 # Has an ucl alias
chart.lower_control_limit = 39.477 # Has a lcl alias

chart.to_json()
chart.to_python()
chart.to_flot()
chart.to_excel()

Simples.

