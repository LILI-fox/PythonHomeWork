# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

"""
a = int(input('Введите трехзначное число: '))

a2 = a % 10
a = a // 10
a1 = a % 10
a = a // 10

print(f"Сумма цифр данного числа: {a + a1 + a2}.")
"""

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

"""
S = int(input())
# x + x + (x + x)*2 = 6x 
Sergey = S / 6
Peter = S / 6
Kate = (Sergey + Peter)*2
print(int(Peter), int(Kate), int(Sergey))
"""

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

"""
b = int(input('Введите номер билета '))
if b < 1000000:
    b5 = b % 10
    b = b // 10
    b4 = b % 10
    b = b // 10
    b3 = b % 10
    b = b // 10
    b2 = b % 10
    b = b // 10
    b1 = b % 10
    b = b // 10
    b0 = b
print(f"{b0 + b1 + b2} = {b3 + b4 + b5} сумма двух половинок")

a = b0 + b1 + b2 == b3 + b4 + b5
print(a, 'это не счастливый билет!')
"""

# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника)

n = int(input("Введите первое число "))
m = int(input("Введите второе число "))
k = int(input("Введите третье число "))

a = n * m
if k < a and (k % n == 0 or k % m == 0):
    print(True)
else:
    print(False)
