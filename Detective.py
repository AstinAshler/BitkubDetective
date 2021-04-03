import numpy as np
import pandas as pd
def Detect(Address):
 
  URL = 'https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address=' + Address + '&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
  df = pd.read_json(URL)
  _df = []
  for i in x:
    if i['tokenSymbol'] == 'BKTC':
      _df.append(i)
  return _df
def transact(df):
  for data in df:
    print('Hash:'+data['blockHash'] +' '+'From:'+data['from']+' '+'To:'+data['to']+' '+'Amount'+str(int(data['value'])/10**18))
Address = str(input())
data = Detect(Address)
transact(data)
