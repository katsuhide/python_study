from xlwings import Workbook, Range


def myfunction():
    wb = Workbook.caller()
    Range('A1').value = "Call Python!"
