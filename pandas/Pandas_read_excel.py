# importing pandas module
import pandas as pd
# defining File path
fpath = "Fruit.xlsx"
# method to be used to read the excel file
data2 = pd.read_excel(fpath,sheet_name='sweet or sour',header=[0])
print(data2)

#Reading custom no. of rows and columns:
import pandas as pd
# File path
fpath = "Fruit.xlsx"
# method to be used to read the data
data2 = pd.read_excel(fpath,usecols=['Fruit','Sweetness','Soreness'],index_col='Fruit',nrows = 5)
print(data2)

#Reading selective rows

import pandas as pd
fpath = "Fruit.xlsx"
data3 = pd.read_excel(fpath,header=None,nrows=4,skiprows=2)
print(data3)