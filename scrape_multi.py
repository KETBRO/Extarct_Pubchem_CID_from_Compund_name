import pandas as pd
import requests
data = pd.read_csv("B.csv")
df = pd.DataFrame(data)
plant=df['plant']
n=len(plant)
for i in range(0,n):
    x=plant[i]
    dls="https://cb.imsc.res.in/imppat/phytochemical/"+x
    print(x) 
    table = pd.read_html(dls)[0]
    table.to_excel("output/"+x+".xlsx")     