largura = float(input("Largura: "))
altura = float(input("Altura: "))

area = largura * altura

litros = area / 2

msg = "A dimensão de {:.2f} x {:.2f} possui área de {:.2f} m² e consome {:.2f} litros de tinta".format(
    largura, altura, area, litros
)

print(msg)
