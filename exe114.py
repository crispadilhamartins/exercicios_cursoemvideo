import requests

def verifcar_site(url):
    try:
        resposta = requests.get(url, timeout=10, verify= False)
        if resposta.status_code == 200:
            return f'O site {url} está acessivel.'
        else:
            return f'O site {url} retornou o status code {resposta.status_code}.'
    except requests.ConnectionError:
        return f'Não foi possivel conectar ao site {url}.'
    except requests.Timeout:
        return f'A sua conexão com o site {url} expirou.'
    except requests.RequestException as e:
        return f'Ocorreu um erro ao tentar acessar o site{url}: {e}'

url = "https://www.pudim.com.br/"
status = verifcar_site(url)
print(status)