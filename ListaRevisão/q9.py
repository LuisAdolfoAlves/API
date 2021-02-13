counter = 0

frase = str(input("Digite uma frase: "))

for i in range(len(frase)):
    if frase[i].isalpha():
        counter += 1

print("A quantidade de letras é: {}".format(counter))
