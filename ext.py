import pandas as pd

df1 = pd.read_csv("cse_3rd.csv")
df = pd.DataFrame(df1)
df.set_index('USN',inplace=True)
df2=df[df.Subfail>4]

c=df2.Name.count()

print(df2)
print ("Total = "+str(c))
