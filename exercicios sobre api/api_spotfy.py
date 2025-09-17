#@CassioLimaP
#web app onde é possivel pesquisar o autor de musicas e albuns
#
#ambiente grafico com caixa de pesquisa 
#ao clicar e pesquisar autor ou musica/album deve aparecer lista com o que foi encontrado
#se nao achar nada mostrar assim mesmo. 
#
#1. comunicar com api do spotfy
#2. criar database para armazenar respostas
#3. mostrar respostas em um web app streamlit
from pprint import pprint 
import os 
import streamlit as st 
import requests
import dotenv
import pandas as pd 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def buscador(token, busca_do_usuario):
    dicionario_total = token.search(q='artist:'+busca_do_usuario, type='artist', limit=1)
    pprint(dicionario_total)
    print('----------------------------------------------------------------------------')
    lista_de_artistas = dicionario_total['artists']['items']
    
    if not lista_de_artistas:
        print(f"Nenhum artista encontrado para '{busca_do_usuario}'")
        return None # Retorna None se não encontrou nada
    artista_encontrado = lista_de_artistas[0]
    id_artista = artista_encontrado['id']
    albums_artista = token.artist_albums(id_artista)
    informacoes_completas = []
    for item in albums_artista['items']:
        nome_albums = (item['name'])
        nome_artista = item['artists'][0]['name']
        url_imagem = item['images'][0]['url']
        dict_respostas = {
            'artista': nome_artista,
            'albums': nome_albums,
            'imagens': url_imagem
        }
        informacoes_completas.append(dict_respostas)
    config={'imagens': st.column_config.ImageColumn(width='medium')}
    df_pesquisa=pd.DataFrame(informacoes_completas)
    st.dataframe(df_pesquisa, column_config=config, hide_index=True )



def autenticar():
    dotenv.load_dotenv()
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
    url = "https://accounts.spotfy.com/api/token"
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
   
    return sp

def main():
    st.title("webapp pesquisa spotfy")
    busca_do_usuario = st.text_input("digite um artista ")
    token = autenticar()
    buscador(token,busca_do_usuario)
    print(token)
    
if __name__ =='__main__':
    main()


