pizza1_price = float(input('Cena pizzy 1: '))
pizza1_avg = float(input('Średnica pizzy 1: '))
pizza2_price = float(input('Cena pizzy 2: '))
pizza2_avg = float(input('Średnica pizzy 2: '))

pole1 = 3.14 * ((pizza1_avg/2) ** 2)
pole2 = 3.14 * ((pizza2_avg/2) ** 2)

a = pizza1_price/pole1
b = pizza2_price/pole2

if a < b:
    print('Pizza 1 opłaca się bardziej')
elif a == b:
    print('Obie są równe')
else:
    print('Pizza 2 opłaca się bardziej')