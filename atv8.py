def ler_temp():
    temp = float(input("Digite a temperatura em graus Celsius: "))
    return temp

def converter_fah(temp_celsius):
    temp_fah = (9 * temp_celsius + 160) / 5
    return temp_fah

def mostrar_resultado(temp_fah):
    print("A temperatura convertida em graus Fahrenheit é: {:.2f}".format(temp_fah))

temp_celsius = ler_temp()
temp_fah = converter_fah(temp_celsius)
mostrar_resultado(temp_fah)
