import pandas as pd

url = "https://raw.githubusercontent.com/kunalgupta2616/datasets/master/employees.csv"
data2 = pd.read_csv(url,nrows=5,parse_dates=[2])
data2.to_csv('modified_emp_data.csv',sep=' ',index=False)
