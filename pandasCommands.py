import pandas as pd

dataFrame = pd.read_csv('orders.csv')
print(dataFrame.iloc[0])

tempDict = { "col1":[1,2,3], "col2":[4,5,6], "col3":[7,8,9]}
dataFrame2 = pd.DataFrame.from_dict(tempDict)

print(dataFrame2)

print(dataFrame.columns)
print(dataFrame.dtypes)