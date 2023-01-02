kolichestvo_b = int(input('Введите количество билетов: '))
stoimost = [0, 990, 1390]
summa = 0
for i in range(kolichestvo_b):
    vozrast = int(input(f'Введите возраст {i+1}-го посетителя - '))
    if vozrast < 18:
        summa = summa + stoimost[0]
    elif 18 <= vozrast <= 25:
        summa = summa + stoimost[1]
    else:
        summa = summa + stoimost[2]
if kolichestvo_b < 4:
    print('Сумма вашего заказа = ', summa, 'руб')
else:
    summa = summa * 0.9
    print('Сумма вашего заказа с 10% скидкой за опт: ', summa, 'руб')











