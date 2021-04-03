import numpy as np
import pandas as pd
Address = str(input())
URL = 'https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address=' + Address + '&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
df = pd.read_json(URL)
_df = []
for i in x:
  if i['tokenSymbol'] == 'BKTC':
   _df.append(i)
_df
