# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import random

print('Введите число элементов в списке: ')
len_arr = int (input())
arr = []

if (len_arr < 0):
    print("Error")

for _ in range(len_arr):
    arr.append(random.randint(- len_arr, len_arr))
print(arr)

result_arr = []
for i in range(len_arr // 2):
       result_arr.append(arr[i] * arr[len_arr - 1 - i])

if (len_arr %  2):
      result_arr.append(arr[len_arr // 2])
print(result_arr)

 


