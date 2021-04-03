import numpy as np
import pandas as pd
import string
ls = []
def Detect(Address):
  URL = 'https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address=' + Address + '&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
  df = pd.read_json(URL)
  _df = []
  for i in x:
    if i['tokenSymbol'] == 'BKTC':
      _df.append(i)
  for data in _df:
    print('Hash:'+data['blockHash'] +' '+'From:'+data['from']+' '+'To:'+data['to']+' '+'Amount'+str(int(data['value'])/10**18))
#    Detect(data['to']) // a string bug here
#Address = '0xEcA19B1a87442b0c25801B809bf567A6ca87B1da'
Address = str(input())
Detect(Address)


