#desafio- crie um programa que:
#- pede por nome de usuario e uma senha
#- se ambos forem corretos, exibe uma mensagem de sucesso
#- caso contrario, exibe uma mensagem de erro 
#- o usuario/senha "corretos" podem ser definidos no codigo

usuario_correto = "admin"
senha_correta = int(292929)

flag=0
while flag == 0:
    usuario_tentativa = input("digite seu usuario: ")
    senha_tentativa = int(input("digite sua senha: "))

    if usuario_correto == usuario_tentativa and senha_correta == senha_tentativa:
        print("senha correta!")
        flag = 1
    
    elif usuario_correto != usuario_tentativa and senha_correta != senha_tentativa:
        print("usuario ou senha incorretos!\ntente novamente")
    
    elif usuario_correto == usuario_tentativa and senha_correta != senha_tentativa:
        print("senha incorreta!\ntente novamente")
    
    elif usuario_correto != usuario_tentativa and senha_correta == senha_tentativa:
        print("usuario incorreto!\ntente novamente")
print("fim do codigo!")
