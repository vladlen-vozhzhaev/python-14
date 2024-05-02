# def f(x):
#     return x**2
#
# print( f(1) )
# print( f(2) )
# print( f(-2) )
# print( f(3) )
# print( f(4) )
# print( f(-5) )



# names = ["Иван", "Вася", "Алекс"]
# def sayHi(name):
#     print(f"Hello {name}!")
#
# for name in names:
#     sayHi(name)

# Имеется кофе автомат, по завершении процесса приготовления кофе автомат выдаёт сдачу
# монетами с номиналом: 1, 2, 5, 10
# Реализовать функцию, которая принимает на вход число(сдача) и печатает на экран сдачу
# Пример:
# 36 = 10 10 10 5 1
# 29 = 10 10 5 2 2

# def getChange(num):
#     coin = 0
#     if num >= 10: coin = 10
#     elif num>=5: coin = 5
#     elif num>=2: coin = 2
#     elif num>=1: coin = 1
#
#     if coin != 0:
#         print(coin)
#         getChange(num - coin)
#
# getChange(29)

# def f(n):
#     if n>2:
#         return f(n-1)+f(n//2)
#     else:
#         return n
# i = 3
# while i<10:
#     print("При n="+str(i)+" функция вернёт: "+str(f(i)))
#     i += 1

# Что вернёт функция f(9)
# f(9) = f(8)+f(4) = 18 + 5 = 23
# f(8) = f(7)+f(4) = 13 + 5 = 18
# f(7) = f(6)+f(3) = 10 + 3 = 13
# f(6) = f(5)+f(3) = 7 + 3 = 10
# f(5) = f(4)+f(2) = 5 + 2 = 7
# f(4) = f(3)+f(2) = 3 + 2 = 5
# f(3) = f(2)+f(1) = 2 + 1 = 3

# def f(n):
#     if n>2:
#         return g(n-1)+f(n-2)
#     else:
#         return 1
#
# def g(n):
#     if n>2:
#         return g(n//2)+f(n//2)
#     else:
#         return n
#
# print( f(6) )
# Что вернёт функция f(6)
# f(6) = g(5)+f(4) = 3 + 3 = 6
# g(5) = g(2)+f(2) = 2 + 1 = 3
# f(4) = g(3)+f(2) = 2 + 1 = 3
# g(3) = g(1)+f(1) = 1 + 1 = 2

# def f(n):
#     if n>0:
#         f(n//4)
#         print(n)
#         f(n-1)

# Какая последовательность цифр будет напечатана на экране если вызвать f(5)
# 1514321

# f(5) -> f(1) -> 5 -> f(4)
# f(1) -> f(0) -> 1 -> f(0)
# f(4) -> f(1) -> 4 -> f(3)
# f(3) -> f(0) -> 3 -> f(2)
# f(2) -> f(0) -> 2 -> f(1)

import math
def calcVector(x1, y1, x2, y2):
    coords = [x2-x1, y2-y1]
    print(f"Вектор с точками x1={x1} y1={y1} и x2={x2} y2={y2} имеет координаты: X={coords[0]} Y={coords[1]}")

#calcVector(2,1, -2, 3)

def calcLengthVector(x1, y1, x2, y2):
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(f"Длина вектора с точками x1={x1} y1={y1} и x2={x2} y2={y2} ровняется: {length}")

calcLengthVector(int(input("Введите число")),int(input("Введите число")), int(input("Введите число")), int(input("Введите число")))
