def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]
entrada = input("Ingrese una palabra: ")
if es_palindromo(entrada):
    print(f"{entrada} es un palíndromo.")
else:
    print(f"{entrada} no es un palíndromo.")