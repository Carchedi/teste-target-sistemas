texto = input("Digite uma string: ")

lista_caracteres = []

for caractere in texto:
    lista_caracteres.append(caractere)

for i in range(len(lista_caracteres)):
    print(lista_caracteres[len(lista_caracteres) - i - 1], end=" ")