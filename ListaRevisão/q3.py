nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2)/2

if media == 10:
    print("Sua média é %.2f! \n--Aprovado com distinção!--" % media)

if media >= 7.0 and media != 10:
    print("Sua média é %.2f! \n--Aprovado!--" % media)

elif media < 7.0:
    print("Sua média é %.2f! \n--Reprovado!--" % media)
