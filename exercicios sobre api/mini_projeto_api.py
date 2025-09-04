from pprint import pprint
import requests
import streamlit as st 
import pandas as pd 
## @CassioLimaP

def pegar_nome_por_decada(nome):
    #preenche dict_frequencias com frequencias do nome em estados da api e retorna 
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    dados_decadas = fazer_request(url=url)
    dict_nome_decadas = {}
    if not dados_decadas:
        return {}
    for dados in dados_decadas[0]['res']:
        quantidade = dados['frequencia']
        decada = dados['periodo']
        dict_nome_decadas[decada] = quantidade

    return dict_nome_decadas

def fazer_request(url, params=None):
    
    resposta = requests.get(url, params=params)

    try:
        resposta.raise_for_status()

    except requests.HTTPError as e:
 
        print(f"erro no reques: {e}")
        resultado = None 
    else: 

        resultado = resposta.json()
    return resultado

def main():
    #dict_estados = pegar_ids_estados()
    st.title("web app nomes")
    st.write("dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/v2/censos/nomes/)")
    nome = st.text_input("consulte um nome: ")
    if not nome:
        st.stop()

    dict_nome_decadas = pegar_nome_por_decada(nome)
    if not dict_nome_decadas: 
        st.warning(f"nenhum dado encontrado para o nome {nome}")
        st.stop()
    df =pd.DataFrame.from_dict(dict_nome_decadas, orient="index")
    
    col1, col2 = st.columns([0.3,0.7])
    with col1:
        st.write("frequencia por decada")
        st.dataframe(df)
    with col2:
        st.write("grafico das frequencias")
        st.line_chart(df)
    #print(f"frequencia do nome {nome} nas decadas (por 100 mil habitantes)")
    #for id_estado,nome_estado in dict_estados.items():
    #    frequencia_estado = dict_frequencias[id_estado]
    #    print(f"--> {nome_estado}: {frequencia_estado} ")


if __name__ =='__main__':
    main()
