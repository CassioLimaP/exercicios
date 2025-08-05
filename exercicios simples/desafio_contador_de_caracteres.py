#crie um codigo que conta o numero de vogais de um bloco de texto
#qualquer. o codigo deve desconsiderar letras maiusculas/minususculas,
#isto é, "a" e "A" contam da mesma forma
#o texto pode ser colado diretamente como um string no codigo

texto = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed tortor nibh, hendrerit a sagittis sagittis, tincidunt eget quam. 
        Nam suscipit consequat magna, vitae venenatis mi porta vel. 

        Donec non purus eget erat venenatis dapibus non sed ipsum. 
        Fusce pretium consequat libero ut auctor. 
        Quisque imperdiet in felis quis faucibus. Donec ac eleifend dolor, 
        
        quis tempor ante. Morbi id neque non erat porta feugiat sed quis augue. 
        Morbi id pretium ligula, in consectetur justo. Phasellus a rutrum turpis. 
        Donec efficitur nisl et libero lobortis, nec suscipit odio ultrices. 
        Morbi arcu purus, tincidunt nec suscipit at, maximus eu arcu. i i I I
"""
contador = int(0)
contador += int(texto.lower().count('a')) 
contador += int(texto.lower().count('e'))
contador += int(texto.lower().count('i')) 
contador += int(texto.lower().count('u'))
contador += int(texto.lower().count('o'))
print(f"o texto tem: {contador} vogais")
