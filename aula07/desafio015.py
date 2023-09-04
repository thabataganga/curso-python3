dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km percorridos? "))

diaria = dias * 60
kms = km * 0.15

total = diaria + kms

msg = "Durante {} dias o carro percorreu {:.2f} km. \nAs diárias foram R$ {:.2f}\nA quilometragem foi R$ {:.2f} \nO valor total foi R$ {:.2f}".format(
    dias, km, diaria, kms, total
)

print(msg)
