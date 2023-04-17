def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    vel_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, vel_media

def calc_dist(tempo, vel_media):
    dist = tempo * vel_media
    return dist

def calc_litros(dist):
    litros_usados = dist / 12
    return litros_usados

def apresent_result(tempo, vel_media, dist, litros_usados):
    print("Velocidade média: {:.2f} km/h".format(vel_media))
    print("Tempo gasto na viagem: {:.2f} horas".format(tempo))
    print("Distância percorrida: {:.2f} km".format(dist))
    print("Quantidade de litros utilizada na viagem: {:.2f} litros".format(litros_usados))

tempo, vel_media = ler_valores()
dist = calc_dist(tempo, vel_media)
litros_usados = calc_litros(dist)
apresent_result(tempo, vel_media, dist, litros_usados)
