# just started pandas, its usefull for mananging the data, for ex, if you'r having raw data then you can make structure for your raw data
# and it will be present in a tabular form, using the pandas we can clean the data and maintain inventory for understandable

import pandas as pd

data = {
    "name" : ["Nithin", "James", "Davis"],
    "age" : [23, 24, 22],
    "email": ["nithin1@gmail.com", "james2@gmail.com", "davison@gmail.com"],
    "salary" : [25000, 25000, 25500]
}

result = pd.DataFrame(data) # here dataframe used for representing data as table format
result1 = result.tail(2) # here tail which is used for to get last rows in a table
result2 = result.head(2) # here head used for to get first rows in a table we need to give value to fetch rows in a table, both tail and head
print(result)
print(result1)
print(result2)
