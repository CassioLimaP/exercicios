#- escolher um numero secreto
#- pede por um chute do usuario
#- indica se o usuario acertou ou nao
#- se errou da uma dica se é mais alto ou baixo
#- repete ate 3 vezes

numero_gabarito = 8

for i in range(0,3):
    numero_chute = int(input("digite seu chute: "))
    
    if numero_chute > numero_gabarito:
        print("chute maior que o numero!\ntente novamente\n")
    
    elif numero_chute < numero_gabarito:
        print("chute menor que o numero!\ntente novamente\n")
    
    else:
        print("parabens! voce acertou!")
        break
    
    print(f"voce gastou {i+1} chance(s)\n")
print("fim do codigo!")
