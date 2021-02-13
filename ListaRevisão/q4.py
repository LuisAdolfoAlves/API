turno = str(input(" Matutino\n Vespertino\n Noturno\n Qual o turno que você estuda? ")).upper().strip()

if turno[0] == "M":
    print("Bom dia!")

elif turno[0] == "V":
    print("Boa tarde!")

elif turno[0] == "N":
    print("Boa noite!")

else:
    print("Valor inválido!")