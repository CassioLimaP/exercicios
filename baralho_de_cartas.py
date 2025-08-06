#@CassioLimaP
#crie um codigo que simula um baralho de cartas.
#o codigo deve conter as seguintes funcoes:]

#gerar_baralho -> retorna um baralho novo. parametros da funcao
#definem quantas copias retornar (1 baralho, 2 baralhos, ...),
#se o baralho deve conter coringas, e se deve ser embaralhado 
#antes de ser retornado 

#mostrar_baralho -> exibe a quantidade de cartas no baralho e 
#mostra quais sao.

#dar_as_cartas -> distribui as cartas do baralho entre X  
#jogadores, de forma que cada jogador recebe Y cartas 

#mostrar_jogadores -> exibe a quantidade de cartas na mao de 
#cada jogador e mostra quais sao 

# a partir dessas funcoes, o codigo deve:
# gerar o baralho e exibi-lo 
# dar as cartas para os jogadores
# exibir o baralho apos as cartas terem sido distribuidas 
# exibir a mao de cada jogador

# DICA: utilize os simbolos copas (♥), ouros (♦), espadas (♠) e paus (♣) para representar os naipes.
# DICA: utilize a funcao random.shuffle (modulo random) para embaralhar
import biblioteca_cassio as casslib 
controle = True
baralhos = []
entrada = ""
embaralhar = False
coringa = False
qtd_baralhos = int(0)
while controle:
    print("escolha a opção:\n[1]gerar baralho\n[2]mostrar baralho")
    print("[3]dar as cartas \n[4]mostrar jogadores")
    escolha_inicial = int(input("escolha: "))
    if escolha_inicial == 1:

        entrada = input("para embaralhar digite [1]SIM e [0]NAO: ")
        embaralhar = (entrada == "1")
        entrada = input("para ter corigas digite [1]SIM [0]NAO: ")
        coringa = (entrada == "1")
        qtd_baralhos = int(input("digite a quantidade de baralhos: "))

        print(f"embaralhar={embaralhar}\ncoringa={coringa}\nqtd_baralhos={qtd_baralhos}")
        baralhos=casslib.gerar_baralho(qtd_baralhos, coringa, embaralhar)

    elif escolha_inicial == 2:
        casslib.mostrar_baralho(baralhos) 
    #elif escolha_inicial == 3:
    #    arg
    #elif escolha_inicial == 4:
    #    arg
    entrada = input("\ncontinuar? digite [1] ou [0]: ")
    controle = (entrada == "1")
print("fim do programa!")
