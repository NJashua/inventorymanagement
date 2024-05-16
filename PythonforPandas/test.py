# import pandas as pd

# data = {'A': [1, 2, 3, 4, 5],
#         'B': [6, 7, 8, 9, 10]}
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# # Accessing a single element
# # print(df.loc[['a', 'c'], ['A', 'B']])
# # # Accessing a row
# # print(df.loc['b'])
# print(df.iloc[0, 1])
# # # Accessing multiple rows and columns
# # print(df.loc[['a', 'c'], ['A', 'B']])


# importing the module

import pandas as pd
import matplotlib.pyplot as plt

# Specify the correct file path where your Excel file is located
file_path = "C:\\Users\\1038588\\OneDrive - Blue Yonder\\program files\\python\\PythonforPandas\\MarksData.xlsx"

# Read the Excel file into a DataFrame
marks_data = pd.read_excel(file_path)

# Set the 'Name' column as the index
marks_data.set_index('Name', inplace=True)

# Display the first few rows of the DataFrame
print(marks_data.head())

# Plot the data as a bar chart
marks_data.plot(kind='bar', rot=0, xlabel='Subject', ylabel='Marks')
plt.show()

# Plot the data as an area chart
marks_data.plot.area(figsize=(12, 4), xlabel='Subject')
plt.show()
