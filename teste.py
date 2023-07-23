import requests

# Dados que você deseja enviar para a API
new_current = 10  # Substitua pelo valor atual da corrente
new_irradiance = 5.10  # Substitua pelo valor atual da irradiação

# Monta a URL da API com os parâmetros na string de consulta (query string)
url_da_api = f"http://127.0.0.1:8000/solar-painel/send/{new_current}/{new_irradiance}"

# Faz a requisição GET para a API (caso necessário, mude para requests.post() se for um POST)
resposta = requests.post(url_da_api)

# Verifica se a requisição foi bem-sucedida (código de status 2xx indica sucesso)
if resposta.status_code >= 200 and resposta.status_code < 300:
    print("Dados enviados com sucesso para a API!")
else:
    print(f"Erro ao enviar dados para a API. Código de status: {resposta.status_code}")
    print(resposta.text)
