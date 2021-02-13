soma = 0
for i in range(5):
    num = int(input("Digite o {}˚ número: ".format(i + 1)))
    soma += num
media = soma / 5

print("Soma: {}\nMédia: {}\n".format(soma, media))