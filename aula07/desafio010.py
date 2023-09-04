valor = float(input("Valor em R$: "))

dolar = valor / 4.93
euro = valor / 5.33
iene = valor / 0.034
libra = valor / 6.23
yuan = valor / 0.68

msg = "R$ {:.2f} vale: \n{:.2f} Dolares \n{:.2f} Euros \n{:.2f} Ienes \n{:.2f} Libras \n{:.2f} Yuans".format(
    valor, dolar, euro, iene, libra, yuan
)

print(msg)
