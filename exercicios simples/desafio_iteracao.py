#dado uma sequencia de numeros, calcule a soma e media dos numero
#nao usar funcao sum()

#dado uma sequencia de numeros, calcule o maior valor da sequencia
#nao usar funcao max()

#dado uma lista de palavras, printe todas as palavras
#com pelo menos 5 caracteres

seq_numeros = "123213421"
maior_num = int()
soma = int()
media = int()
lista_de_palavras = ["arroz","gasolina","farinha","tapete","costela"]

for i in range(len(seq_numeros)):

    soma += int(seq_numeros[i])
    media = soma / len(seq_numeros)
    
    if maior_num < int(seq_numeros[i]):
        maior_num = int(seq_numeros[i])

print(f"a soma dos valores {seq_numeros} é {soma} \na media é {media} \no maior numero é {maior_num}!\n\n")

for i in range(len(lista_de_palavras)):
    print(lista_de_palavras[i])
print("\n---------------------\n")
#dado duas listas, printe todos os valores que aparecerem
#duplicados nas duas listas

#dados duas listas, printe uma mensagem dizendo se existe 
#algum alemento em comum entre elas ou nao

lista_1 = ["farinha","tijela","costas","teclado","poste","cachorro"]
lista_2 = ["andromeda","telegrafo","ambiente","poste","tijela"]
existe_duplicata = int()

print(lista_1)
print(lista_2)
for i in lista_1:
    for j in lista_2:
    
        if j == i:
            print(f"\nlista_1: {i}\nlista_2: {j} \nsao duplicados")
            existe_duplicata = 1 

if existe_duplicata:
    print("\nexiste duplicata")
else: print("\nnao existe duplicata")
