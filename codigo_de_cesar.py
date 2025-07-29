#implementar a cifra de cesar.
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
#4- funcao que compara letras e troca com referencial ao maiuscula ou minusculas
    #4.1- verificar se é maiusculas ou minusculas
    #4.2- ver numero referente a letra do alfabeto e trocar de acordo a chave
    #4.3- isso letra a letra da palavra a ser codificada
#5- saida esperada-> "a palavra "olá tudo bem" com a chave -2 fica "mjá rsbom zck". "
def codificacao_cesar(entrada_do_codigo,chave):
    maiusculas = "abcdefghijklmnopqrstuvwxyz"
    minusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codigo_pronto = " "
    controle_de_posicoes = 0
    for i in entrada_do_codigo[]:
        for j in range(1,26):
            if entrada_do_codigo[i] == maiusculas[j] :
                #codifica com maiusculas
                #1- valor de entrada compara com maiusculas
                #2- se verdade
                    #2.1- letra da entrada recebe a letra da posicao posicao+chave de maiusculas
                    #2.2- fazer as letras voltarem ao inicio se extrapolarem o valor total de 26
                #fim
                if maiusculas[j+chave]>25:
                    controle_de_posicoes = ((j+chave)%26)
                    codigo_pronto[i] = maiusculas[0+controle_de_posicoes]
                    
            elif entrada_do_codigo[i] == minusculas[j] :
                #codifica com minusculas
        #fim do for de dentro
    #fim do for de fora 
return codigo_pronto

entrada_do_codigo = "olá tudo bem?" 
chave=-2
print(maiusculas[4])

