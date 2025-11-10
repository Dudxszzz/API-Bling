import requests

access = "3732fed5205cde3ee9dea75e61016294b816da64"
base = "https://api.bling.com.br/Api/v3/"
pag = 1
limite = 100

produtos = []
headers={"Authorization": f"Bearer {access}"}

while True:
    url = f"{base}produtos?pagina={pag}&limite={limite}"
    response = requests.get(url, headers=headers)

    if response.status_code ==200:
        try:
            data = response.json()
            ids = [item["id"] for item in data.get("data", [])]
            produtos.extend(ids)
            print(f"IDs obtidos nesta página: {ids} {pag}")

            if len(ids) < limite:
                break
            pag += 1
        except Exception as e:
            print(f"Erro ao processar a resposta: {e}")
            break
    else:
        print(f"Erro ao obter os itens do vendedor: {response.status_code} - {response.text}")
        break

tamanho = len(produtos)
print(f"Quantidade de produtos da conta: {tamanho}")