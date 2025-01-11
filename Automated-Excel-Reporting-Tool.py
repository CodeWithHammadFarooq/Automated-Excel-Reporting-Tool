import pandas as pd
df1 = pd.read_excel(r"C:\Users\hamma\Downloads\Data01.xlsx", sheet_name="class1")
df2 = pd.read_excel(r"C:\Users\hamma\Downloads\Data01.xlsx", sheet_name="class2")
df3 = pd.read_excel(r"C:\Users\hamma\Downloads\Data02.xlsx", sheet_name="class3")
df = pd.concat([df1,df2,df3])
df.to_excel(r"C:\Users\hamma\Downloads\TOTAL.xlsx", index=False)

result = df.groupby(by='class').mean()
result=result.loc[:,["math", "physics"]]
print(result)

import matplotlib.pyplot as plt
result.plot(kind="bar")
plt.show()