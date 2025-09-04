from pprint import pprint
import requests
## @CassioLimaP

def pegar_ids_estados():
    #preenche dict_estados com nome de estados da api e retorna
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    parametros = {
        'view': 'nivelado', 
    }
    dados_estados = fazer_request(url=url, params=parametros)
    dict_estados = {}
    for dados in dados_estados:
        id_estado = dados['UF-id']
        nome_estado = dados['UF-nome']
        dict_estados[id_estado] = nome_estado

    return dict_estados

def pegar_frequencia_nome_por_estado(nome):
    #preenche dict_frequencias com frequencias do nome em estados da api e retorna 
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    parametros = {
        'groupBy': 'UF', 
    }
    dados_frequencias = fazer_request(url=url, params=parametros)
    dict_frequencias = {}
    for dados in dados_frequencias:
        id_estado = int(dados['localidade'])
        frequencia = dados['res'][0]['proporcao']
        dict_frequencias[id_estado] = frequencia

    return dict_frequencias



def fazer_request(url, params=None):
    
    resposta = requests.get(url, params=params)

    print(resposta.request.url)

    try:
        resposta.raise_for_status()

    except requests.HTTPError as e:
 
        print(f"erro no reques: {e}")
        resultado = None 
    else: 

        resultado = resposta.json()
    return resultado

def main(nome):
    dict_estados = pegar_ids_estados()
    dict_frequencias = pegar_frequencia_nome_por_estado(nome)
    print(f"frequencia do nome {nome} nos estados (por 100 mil habitantes)")
    for id_estado,nome_estado in dict_estados.items():
        frequencia_estado = dict_frequencias[id_estado]
        print(f"--> {nome_estado}: {frequencia_estado} ")


if __name__ =='__main__':
    main('cassio')
