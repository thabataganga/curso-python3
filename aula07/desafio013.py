salario = float(input("Salário do funcionário em R$: "))

aumento = salario + (salario * 15 / 100)

msg = "O salário de R$ {:.2f} com aumento de 15% passa a ser R$ {:.2f}".format(
    salario, aumento
)

print(msg)
