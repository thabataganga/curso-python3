medida = float(input("Distancia em metros: "))

dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida * 0.001

msg = "{} metros equivale há: \n{} dm,\n{} cm,\n{} mm,\n{}km".format(
    medida, dm, cm, mm, km
)

print(msg)
