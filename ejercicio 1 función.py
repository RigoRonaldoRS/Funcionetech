def hora (a, b, c):
    list = [a,b,c]
    suma = sum(list)
    if suma > 15:
        print("imprimir suma: ", max(list))
    elif suma<10:
        print("imprimir suma: ", min(list))
    elif suma>=10 and suma<=15:
        print("imprimir suma:", list[1])

hora(7, 2, 3)
