import pandas as pd

data_file = pd.read_csv(r"C:\Users\1038588\OneDrive - Blue Yonder\program files\python\PythonforPandas\data.csv")

# exporting data to Excel file
#data_file.to_excel(r"C:\Users\1038588\OneDrive - Blue Yonder\program files\python\PythonforPandas\sample.xlsx", index=False)

print(data_file)

print("DataFrame exported to Excel successfully.")
