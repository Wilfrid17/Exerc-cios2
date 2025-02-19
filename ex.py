#codigo
qtde_hospede = int(input("Informe quantida de pessoa: "))

quarto = []

for i in range(qtde_hospede):
    nome = input("Qual o nome?: ")
    cpf = input("Qual o cpf?: ")
    hospede = [nome, "cpf: {}".format(cpf)]
    quarto.append(hospede)
print(quarto)