# ref
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
#
# -*- coding: utf-8 -*-

# import lib
import pandas as pd

# read xlsx file
xlsFile = "hoge.xlsx"
xls_data = pd.read_excel(xlsFile, sheetname="hoge1")
print(xls_data)

# read csv file
csvFile = "fuga.csv"
csv_data = pd.read_csv(csvFile, encoding='utf-8')
print(csv_data)

