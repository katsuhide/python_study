# ref
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html
# http://xlsxwriter.readthedocs.io/index.html

# import lib
import pandas as pd
import numpy as np

# create data
dates = pd.date_range("20130101", freq='D', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns = list("ABCD"))

# set data
fileName = "hoge.xlsx"
writer = pd.ExcelWriter(fileName)
df.to_excel(writer, sheet_name="hoge1")
df.T.to_excel(writer, sheet_name="hoge2")

workbook  = writer.book
worksheet1 = writer.sheets['hoge1']
worksheet2 = writer.sheets['hoge2']

# Add some cell formats.
format1 = workbook.add_format()
format1.set_font_color('red')

index = workbook.add_format({'align': 'left'})
index.set_font_color('blue')

# Set the column width and format.
worksheet1.set_column('C:C', None, index)
worksheet2.set_column('B:B', 20, format1)

# save
writer.save()
