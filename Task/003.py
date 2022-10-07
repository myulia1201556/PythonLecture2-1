# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Минимальное значение дробной части отличное от нуля, 
# у целых чисел дробной части нет их в расчет не берем.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform

def num_in_list(count):
    arr = list()

    if count < 0:
        return "Error"
        
    for i in range(count):
        num = round(uniform(1, count), 2)
        arr.append(num)
    print(arr)
    min = 1
    max = 0
    dif = 0
    for i in range(count):
        if (arr[i] % 1) < min:
            min = round((arr[i] % 1), 2)
        if (arr[i] % 1) > max:
            max = round((arr[i] % 1), 2)
    dif = round(max - min, 2)
    print(f'Min:', min, 'Max:', max, 'Difference:', dif)

print('Введите чиcло: ')
num_in_list(int(input()))