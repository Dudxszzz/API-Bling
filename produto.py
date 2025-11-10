import requests

produto = "" #id do item
access = "" #token de acesso
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