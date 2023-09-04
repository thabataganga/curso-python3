temperatura = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (temperatura * 9 / 5) + 32
kelvin = temperatura + 273.15

msg = "A temperatura {:.2f} °C equivale há: \n{:.2f} °F \n{:.2f} K".format(
    temperatura, fahrenheit, kelvin
)

print(msg)
