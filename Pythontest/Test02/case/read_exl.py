import xlrd



d = xlrd.open_workbook("testdata.xlsx")

table = d.sheet_by_name("sheet1")
nrows = table.nrows # 获取总行数
ncols = table.ncols # 获取总列数
print(nrows,ncols)