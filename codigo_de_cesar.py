#implementar a cifra de cesar. @cassioLimaP
#string movendo cada letra para um certo numero de passos no alfabeto
#o numero de passos é dado por uma chave. letras com acentos, espacos e pontuacao permanecem iguais
#"abcd" com 1 chave = "bcde"
#"ABCD" com 2 chaves = "CDEF"

#DICA: construa 2 strings com as letras do alfaberto em ordem
#um para letra minusculas e outra para as maiusculas e use este 
#string para guiar as substituicoes.

#1- variaveis de comparacao maiusculas  e minusculas
#2- entrar com variavel da palavra a ser codificada
#3- entrar com numero (chave) da da troca de posicao (+ ou -) 
#4- funcao que compara letras e troca com referencial
    #4.1- verificar em qual numero está a o caractere (0-25)
    #4.2- verificar se vai extrapolar o limite (25)
    #4.3- retornar letra da posicao (original+chave)
#5- saida esperada-> "a palavra "olá tudo bem" com a chave -2 fica "mjá rsbom zck". "
#ord('A') retorna 65
#ord('Z') retorna 90
#ord('a') retorna 97
#ord('z') retorna 122
#chr(97) retorna 'a'
def codificacao_cesar(texto_entrada, base, chave):
    indice_atual=base.index(texto_entrada)
    indice_corrigido=0
    if indice_atual+chave > 25:
        indice_corrigido=(indice_atual+chave)%26
        cifra_char_pronto = base[indice_corrigido]
        

    elif indice_atual+chave <0:
        indice_corrigido=indice_atual+chave
        cifra_char_pronto = base[25 + indice_corrigido]
    
    else:
        cifra_char_pronto = base[indice_atual+chave]
    return cifra_char_pronto
minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
texto_entrada = "olá BOM dia"
chave = -2
cifra=""
for char_da_entrada in texto_entrada:

    if char_da_entrada in maiusculas:
        cifra += codificacao_cesar(char_da_entrada, maiusculas, chave)

    elif char_da_entrada in minusculas:
        cifra += codificacao_cesar(char_da_entrada, minusculas, chave)

    else:
        cifra+=char_da_entrada
print("a palavra:",texto_entrada," com chave:",chave," fica:",cifra)
