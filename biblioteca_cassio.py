import random 
def gerar_baralho(quantidade: int, coringa: bool, embaralhar: bool):
    #quantidade é tipo int enquanto coringa apenas precisa ser 'true' ou 'false'
    naipes = ["♥", "♦", "♠", "♣"]
    valores = ['coringa','as','2','3','4','5','6','7','8','9','10','J','Q','K','coringa']
    baralhos_totais = []
    for baralho in range(quantidade):
        for naipe in naipes:
            for valor in valores:
                if(coringa == False):
                    baralhos_totais.append([baralho,naipe+valor])
                else:
                    if valor != 0 or valor != 14:
                        baralhos_totais.append([baralho,naipe+valor])
    if embaralhar == True:
        random.shuffle(baralhos_totais)

    return baralhos_totais
print("fim da funcao gerar_baralho.\n")
def mostrar_baralho(baralhos_totais):
    for valores in baralhos_totais:
        print(f"baralho: {valores[0]:<3} carta:{valores[1]:<3}")
#
#def dar_cartas(baralhos, qtd_jogadores, qtd_cartas):
    
#def mostrar_jogadores
