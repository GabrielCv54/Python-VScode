import urllib.error
import requests as r
import urllib
try:
    url='https://www.bibliaonline.com.br/'
    requisition = r.get(url)
    
except r.exceptions.ConnectionError:
   print('O site está offline!!')
else:
    print('O site está acessível!')

    
