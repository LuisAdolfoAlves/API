altura = float(input("Digite a sua altura: "))
gender = str(input("Você é homem ou mulher? ")).upper()

if gender[0] == "H":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é %.2f" % peso_ideal)
    
elif gender[0] == "M":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é %.2f" % peso_ideal)

