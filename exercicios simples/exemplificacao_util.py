var_0 = int(input("digite a idade: "))
#direciona a variavel para ser inteiro
var_1 = input("digite a idade: ")
#esta acima armazena o valor numerico como string

nome = input("digite seu nome: ")
#um nome qualquer
tamanho_nome = len(nome)
#armazena o tamanho do nome


#sobre listas e tuplas
lista=[1,2,7,3,4.2,'arroz',]
#listas podem ter varios tipos
print(lista[0])
#printa primeiro item da lista
print(lista[-1])
#printa ultimo item da lista 
print(lista[-2])
#printa penultimo item da lista
del lista[0]
#apaga posicao na lista
tupla = (1,2,7,3,4.2,'arroz',)
#nao é possivel modificacoes de tuplas 
tuple(lista)
#transforma em tupla a lista
list(lista)
#transforma esta lista em lista novamente
bool(lista)
#verifica se a lista é vazia retornando true ou false
#nesse caso retorna true (com elementos)
listavazia=[]
#cria lista vazia
bool(listavazia)
#retorna false (vazio)
#em if apenas digitar a variavel pois ja testa true or false
if listavazia:
    print("lista preenchida")
else: print("lista vazia")
