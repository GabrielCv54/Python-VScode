import requests

url='https://www.bibliaonline.com.br/'
requisition = requests.get(url)
print(requisition.json())

