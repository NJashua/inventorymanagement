# loc will return one or more specified row(s)
import pandas as pd
data = {
    "jack": ["Hey Jack"],
    "jacky": ["Hey Jackuuuu"]
}

df = pd.DataFrame(data, index=[1])
print(df.loc[1])
