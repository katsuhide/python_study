# -*- coding: utf-8 -*-
# ref
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
#

# import lib
import pandas as pd


# read xlsx file
def read_xlsx():
    xlsFile = "hoge.xlsx"
    xls_data = pd.read_excel(xlsFile, sheetname="hoge1", parse_cols="B:H", skiprows=0, skip_footer=5)
    print(xls_data)


# read csv file
def read_csv():
    csvFile = "fuga.csv"
    csv_data = pd.read_csv(csvFile, encoding='utf-8')
    print(csv_data)

read_xlsx()
