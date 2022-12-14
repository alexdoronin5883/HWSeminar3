# TASK 1
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Решение ////////////////////////////////////////////////////////
 
# some_list = [2, 3, 5, 9, 3] 
# print(some_list)
# sum = 0
# for i in range(len(some_list)):
#     if i%2==0:
#         some_list[i]=0
#     else:
#         sum += some_list[i]     
# print (sum)


# ////////////////////////////////////////////////////////////////

# TASK 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Решение ////////////////////////////////////////////////////////



# list = [2, 3, 4, 5, 6]
# print(list)

# some_list = [int(input())for _ in range(int(input()))]

# pr_list = []
# for i in range(len(some_list) // 2 + len(some_list) % 2):
#     pr_list.append(some_list[i]*some_list[len(some_list)-1-i])
# print(pr_list)



# ////////////////////////////////////////////////////////////////

# TASK 3
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# Решение ////////////////////////////////////////////////////////

# a = [float(input())for i in range(int(input())) ]
# list = [float('0.'+ str(i).split('.')[1]) for i in a if '.' in str(i)]
# print(max(list)-min(list)) 

# ////////////////////////////////////////////////////////////////

# TASK 4
# Напишите программу, 
# которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Решение ////////////////////////////////////////////////////////

# n = int(input())
# b = ''
# while n>0:
#     b = str(n % 2) + b
#     n=n // 2
# print(b)    


# ////////////////////////////////////////////////////////////////

# TASK 5
# Задайте число.
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет 
# выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# Решение ////////////////////////////////////////////////////////

# k = int(input())
# list=[0]*(k*2+1)
# list[k]=0
# list[k+1]=1

# for i in range(k+2,len(list)):
#     list[i]=list[i-2]+list[i-1]

# for i in range(k,-1,-1):
#     list[i]=list[i+2]-list[i+1]    
# print(list)



# ////////////////////////////////////////////////////////////////