''' Series, Series, Series...!
It's like a one dimensional array
series is nothing but a column which contains with values..., like a colum with values and holds any datatype

'''

import pandas as pd

age = [20, 22, 24]

get_age = pd.Series(age)

values = ["ilu", "lu", "lutoo"]
result = pd.Series(values, index=["bittu", "chintu", "bhanttu"]) # if we dont want id's we can give alternative's
print(result)