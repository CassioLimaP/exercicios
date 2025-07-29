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
#4- funcao que compara letras e troca com referencial ao maiuscula ou minusculas
    #4.1- verificar se é maiusculas ou minusculas
    #4.2- ver numero referente a letra do alfabeto e trocar de acordo a chave
    #4.3- isso letra a letra da palavra a ser codificada
#5- saida esperada-> "a palavra "olá tudo bem" com a chave -2 fica "mjá rsbom zck". "
#ord('A') retorna 65
#ord('Z') retorna 90
#ord('a') retorna 97
#ord('z') retorna 122
#chr(97) retorna 'a'
def codificacao_cesar(entrada_do_codigo, chave):
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codigo_pronto = ""
    controle_de_posicoes = 0
    for i in entrada_do_codigo:
        for j in range(0,25):
            if entrada_do_codigo[i] == maiusculas[j] :#codifica com maiusculas ASCII(65 ate 90)
                
                if ord(maiusculas[j+chave]) > ord('Z'):
                    controle_de_posicoes = ((j+chave)%26)
                    codigo_pronto = codigo_pronto+maiusculas[controle_de_posicoes]
                    break
                
                elif ord(maiusculas[j+chave]) < ord('A'):
                    controle_de_posicoes = ((j+chave)%26)
                    codigo_pronto = codigo_pronto+maiusculas[25+controle_de_posicoes]
                    break
                
                else:
                    controle_de_posicoes = (ord(entrada_do_codigo[i]) - ord('A'))
                    codigo_pronto = codigo_pronto+maiusculas[controle_de_posicoes+chave]
                    break

            elif entrada_do_codigo[i] == minusculas[j]:#codifica com minusculas ASCII(97 ate 122)

                if ord(maiusculas[j+chave]) > ord('Z'):
                    controle_de_posicoes = ((j+chave)%26)
                    codigo_pronto = codigo_pronto+maiusculas[controle_de_posicoes]
                    break
                
                elif ord(maiusculas[j+chave]) < ord('A'):
                    controle_de_posicoes = ((j+chave)%26)
                    codigo_pronto = codigo_pronto+maiusculas[25+controle_de_posicoes]
                    break
                
                else:
                    controle_de_posicoes = (ord(entrada_do_codigo[i]) - ord('A'))
                    codigo_pronto = codigo_pronto+maiusculas[controle_de_posicoes+chave]
                    break
                    
            else:
                codigo_pronto = codigo_pronto+entrada_do_codigo[i]
                break
        #fim do for de dentro
        print(codigo_pronto)
    #fim do for de fora
    print("codigo original:",entrada_do_codigo,"com chave:",chave)
    print("resultado:",codigo_pronto)
    #return codigo_pronto
entrada_do_codigo = "olá tudo bem?"
chave=-2
codificacao_cesar(entrada_do_codigo, chave)
#print(maiusculas[4])

