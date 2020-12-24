import pandas as pd
import re

df = pd.read_csv("CJQ06.20201222T181202.csv")
df['Garda Division'] =  [re.sub(r' Garda Division','', str(x)) for x in df['Garda Division']]
df['Garda Division'] =  [re.sub(r'D.M.R.','DMR', str(x)) for x in df['Garda Division']]
df['Garda Division'] =  [re.sub(r'DMR Eastern','DMR East', str(x)) for x in df['Garda Division']]
df['Garda Division'] =  [re.sub(r'DMR Western','DMR West', str(x)) for x in df['Garda Division']]
df['Garda Division'] =  [re.sub(r'DMR Northern','DMR North', str(x)) for x in df['Garda Division']]
df['Garda Division'] =  [re.sub(r'DMR Southern','DMR South', str(x)) for x in df['Garda Division']]
# df['Garda Division'] =  [re.sub(r'DMR Southern Central','DMR South Central', str(x)) for x in df['Garda Division']]
# df['Garda Division'] =  [re.sub(r'DMR Norethern Central','DMR North Central', str(x)) for x in df['Garda Division']]
print(df['Garda Division'].unique())


df.to_csv("CRIME.csv")
print (df)