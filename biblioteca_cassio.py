import random 
def gerar_baralho(quantidade: int, coringa: bool, embaralhar: bool):
    #quantidade é tipo int enquanto coringa apenas precisa ser 'true' ou 'false'
    naipes = ["♥", "♦", "♠", "♣"]
    valores = ['coringa','as','2','3','4','5','6','7','8','9','10','J','Q','K','coringa']
    baralhos_totais = []
    for baralho in range(quantidade):
        for naipe in naipes:
            for valor in valores:
                if coringa == True :
                    baralhos_totais.append([baralho,naipe+valor])
                else:
                    if valor != 'coringa':
                        baralhos_totais.append([baralho,naipe+valor])
    if embaralhar == True:
        random.shuffle(baralhos_totais)
    
    print("fim da funcao gerar_baralho.\n")
    return baralhos_totais

def mostrar_baralho(baralhos_totais):
    for valores in baralhos_totais:
        print(f"baralho: {valores[0]:<3} carta:{valores[1]:<3}")

def dar_cartas(baralhos: list, qtd_jogadores: int):
    #somar baralhos em lista_destribuicao com qtd_jogadores
    mao_dos_jogadores = [[] for _ in range(qtd_jogadores)]
    
    for i,carta in enumerate(baralhos):

        indice_da_qtd_jogadores = i % qtd_jogadores
        mao_dos_jogadores[indice_da_qtd_jogadores].append(carta)
    return mao_dos_jogadores
def mostrar_mao_dos_jogadores(mao_dos_jogadores: list):
    for i,mao in enumerate(mao_dos_jogadores):
        print(f"--- Jogador {i+1} ---")
        print(f"Número de cartas: {len(mao)}")
        print(f"cartas: {', '.join([carta[1] for carta in mao]):<4}") 
        print("-" * 20)  
