preco = float(input("Digite o preço: "))

desc_5 = preco - (preco * 5 / 100)
desc_10 = preco * (1 - 0.10)

msg = "Valor total: R$ {:.2f} \nDesconto de 5%: R$ {:.2f} \nDesconte de 10%: R$ {:.2f}".format(
    preco, desc_5, desc_10
)

print(msg)
