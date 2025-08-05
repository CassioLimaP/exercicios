#crie um jogo. neste jogo, o jogador precisa responder
#o nome da capital de cada estado do brasil. o jogo
#deve perguntar ao usuario "qual a capital do estado X?",
#e checar se o usuario respondeu de forma correta. apos
#cada pergunta, o usuario pode escolher para o jogo ou 
#continuar. quando o usuario decidir parar, ou quando todas
#as perguntas forem respondidas, o codigo mostra o numero
#bruto e a porcentagem de acertos

#1 criar dados (dicionarios)
#2 perguntar qual capital (funcao questionario)
#3 verificar a resposta (funcao questionario)
#4 perguntar novamente (funcao questionario)
#5 numero bruto e porcentagem de acertos 

def questionario(dados_dicionario):
    usuario_digita = "" 
    acertos = int(0)
    tentativas = int(0)

    for estado, capital in dados_dicionario.items():
        usuario_digita = input(f"qual a capital do(a) {estado.lower()}?: ")
        if usuario_digita == capital.lower():
            acertos += 1 
            print("correto!\n")
        
        else:
            print(f"incorreto. a resposta é {capital.lower()} \ntente novamente!\n")
        
        flag_encerrar = int(input("deseja encerrar o jogo? \n[1]para sim \n[0]para nao"))
        if flag_encerrar == 1:
            break
        
        tentativas += 1 
    return acertos, tentativas

capitais = {
    'Rio de Janeiro': 'Rio de Janeiro',
    'São Paulo': 'São Paulo',
    'Bahia': 'Salvador',
    'Minas Gerais': 'Belo Horizonte',
    'Pernambuco': 'Recife',
    'Rio Grande do Sul': 'Porto Alegre',
    'Paraná': 'Curitiba'
}
acertos_recebidos,tentativas_recebidas = questionario(capitais)
porcentagem_de_acerto = (acertos_recebidos*100)/(tentativas_recebidas+1)
print(f"o jogador teve {tentativas_recebidas+1} jogadas das quais acertou {acertos_recebidos}.")
print(f"tendo {porcentagem_de_acerto}% de acertos ")
print("fim do codigo!")
