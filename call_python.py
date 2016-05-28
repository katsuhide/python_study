# -*- coding: utf-8 -*-
# import xlwings as xw
from xlwings import Workbook, Range

def hoge():
    wb = Workbook.caller()
    Range('A1').value = "Call Python!"
