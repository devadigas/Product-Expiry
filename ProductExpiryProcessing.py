import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import time

start = time.time()
df = pd.read_csv("Input_Data.txt",delim_whitespace = True)

df.columns = ['Date', 'Id', 'Product_Name', 'DateOfManuf', 'Valid_Months', 'Price']

df.to_csv('Input_Data.csv', index=None)
df1 = df

df1['DateOfManuf'] = pd.to_datetime(df1['DateOfManuf'])

df1['Expiry_Date'] = df.apply(lambda x:x['DateOfManuf'] + pd.DateOffset(months = x['Valid_Months']),axis =1)
days = datetime.today() - timedelta(days=7)
df1['Is_Expiring'] = np.where(df1['Expiry_Date'] <= days.strftime('%Y-%m-%d'), 'Y','N')
#print(df1)

df2 = df1.loc[df1['Is_Expiring'] == 'Y']
df2.to_csv('Output.csv',index = None)

end = time.time()

print(end - start)          # in seconds




