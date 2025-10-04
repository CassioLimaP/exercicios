# @CassioLimaP
# vou tentar criar aqui em partes, a juncao de agno basico com o groq
# groq para escolher as LLM e o agno para criar os agentes.
# posteriormente vou tentar fazer isso rodar com o streamlit
#
import os
from dotenv import load_dotenv
from openai import OpenAI
from agno.agent import Agent

load_dotenv()
#o esquema aqui é que o agno funciona com o OpenAI entao vou usar ele 
#so que com a api e endereço do groq 
groq_client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1/chat",
)

#escolhendo um modelo  
MODELO_GROQ = "llama3-8b-8192"

#criando o agente 
try:
    agente_veloz = Agent(
        #passamos nosso cliente personalizado
        client=groq_client, 
        #Especifique o nome do modelo que o Groq deve usar
        model=MODELO_GROQ,
        # O resto da configuração do seu agente continua a mesma
        name="Agente jarvis",
        system_prompt="Você é um assistente prestativo e serio. passa as informações de forma clara e objetiva."
    )
    flag = True 
    while flag:
        prompt_usuario = input("usuario: ")
        print(f"\nusuario: {prompt_usuario}")
        resposta = agente_veloz.run(prompt_usuario)
        print("\n--- Resposta do Agente (via Groq) ---")
        print(resposta)
        print("--------------------------------------")
except Exception as e:
    print(f"\nOcorreu um erro: {e}")
    print("Verifique se sua API Key do Groq está correta e se o modelo '{MODELO_GROQ}' é válido.")

