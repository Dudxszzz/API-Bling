'''
import requests

produto = "16336273766"
access = "7d022ba0ddc8dc6aa6d970894ec9ba4dfefa3044"
base = "https://api.bling.com.br/Api/v3/"

url = f"{base}produtos?idsProdutos[]={produto}"
headers = {"Authorization": f"Bearer {access}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro api")

'''

import requests

produto = "16487360305"
access = "3732fed5205cde3ee9dea75e61016294b816da64"
base = "https://api.bling.com.br/Api/v3/"

url = f"{base}produtos/?idsProdutos[]={produto}"
headers = {"Authorization": f"Bearer {access}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
    estoque = [item["estoque"]["saldoVirtualTotal"] for item in data.get("data", [])]
    print("="*70)
    print(f"O estoque do produto {produto} é {estoque}")
else:
    print("Erro api")