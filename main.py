# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# print(a>b)
# print(a<b)
# print(a == b)
# print(a <= b)
# print(a >= b)
# # В магази пришел покупатель и купил некоторый товар за цену X в количестве N
# # На экран необходимо вывести подытог (сумма к опалте)
# # Вывести сколько сдачи необходимо выдать
# itemPrice = int(input("Введите стоимость товара за (ед): "))
# countPrice = int(input("Кол-во товара: "))
# summ = itemPrice * countPrice
# print("Подытог: "+str(summ))
# money = int(input("С какой суммы необходимо дать сдачу: "))
# change = money - summ
# print("Сдача: "+str(change))
#
#
# a = float(input("Введите число: "))
# b = float(input("Введите число: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
#
# name = input("Введите имя: ")
# print(f"Привет {name}")

age = input("Ваш возраст: ")
if (age == ""):
    print("Вы ничего не ввели")
else:
    age = int(age)
    print(age)