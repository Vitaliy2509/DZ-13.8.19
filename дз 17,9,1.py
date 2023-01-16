array = input('Введите числа через пробел - ')
try:
    nam = int(input('Введите число - '))
    array = list(map(int, array.split()))
except ValueError:
    print('Ввели нечисловые данные')
if min(array) > nam or nam > max(array):
    print('Вы ввели число за пределами массива, исправьте это')
else:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print('Список после сортировки по возрастанию', array)
    def binary_search(array, nam):
      l = []
      for i in array:
          if i < nam:
              l.append(i)
      return l
    position = array.index(max(binary_search(array, nam)))
    print(f'Ответ: Элемент № {position+1} в массиве меньше введеного вами \n числа {nam}, а следующий элемент более или равен')





