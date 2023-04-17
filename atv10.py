def calc_media(list):
    media = sum(list) / len(list)
    return media

numeros = [10, 20, 30, 40, 50]
media = calc_media(numeros)

print("A média dos números é:", media)