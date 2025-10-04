# @CassioLimaP
# vou tentar criar aqui em partes, a juncao de agno basico com o groq
# groq para escolher as LLM e o agno para criar os agentes.
# posteriormente vou tentar fazer isso rodar com o streamlit
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.agent import Agent
load_dotenv()
groq_model= Groq(id="llama-3.1-8b-instant")
#criando o agente 
agente_veloz = Agent(
    #passamos nosso cliente personalizado
    model=groq_model,
    name="Agente jarvis",
    description={
        '''
        Você é um assistente prestativo. 
        voce passa informações de forma clara e com atencao ao que foi pedido.
        .
        '''
    }
)
try:
    flag = True 
    while flag:
        prompt_usuario = input("usuario: ")
        agente_veloz.print_response(prompt_usuario)
except Exception as e:
    print(f"\nOcorreu um erro: {e}")
    print("Verifique se sua API Key do Groq está correta e se o modelo '{MODELO_GROQ}' é válido.")

