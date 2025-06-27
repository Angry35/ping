palabra=input("digita la cadena que forma la palabra:")

if str(palabra)== str(palabra)[::-1]: ## ::-1 invierte la sintaxis
    print("es palindromo")
else:
    print("no es palindromo")