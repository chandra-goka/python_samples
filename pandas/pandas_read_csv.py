# importing pandas and giving an alias name
import pandas as pd
# URL of the data
url = "home/user/kunalgupta2616/datasets/master/Data.csv"
# method to be used to read the data
data = pd.read_csv(url,header=[0],sep=',')
print(data)

#2. Reading custom no. of rows and columns:

import pandas as pd
url = "home/user/kunalgupta2616/datasets/master/Data2.csv"
data1 = pd.read_csv(url,usecols=['Country','Age','Purchased'],skiprows = [1,2],nrows=4,index_col='Country')
print(data1)

#3. Parsing column containing Date:

import pandas as pd
url = "https://raw.githubusercontent.com/kunalgupta2616/datasets/master/employees.csv"
data2 = pd.read_csv(url,nrows=5,parse_dates=[2])
print(data2.dtypes)