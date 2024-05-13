cars = ["bmw", "audi", "kia", "vaz"]
print( len(cars) )
print(cars[0])
print(cars[1])
print(cars[2])


for car in cars:
    print(car)

i = 0
while i<len(cars):
    print(cars[i])
    i += 1 # i = i + 1

marks = [5,5,4,5,5,5,4,4]
sum = 0
for mark in marks:
    sum = sum + mark

print(sum/len(marks))
print( round(sum/len(marks)) )
import math
# # Найти максимальный нечетный элемент списка
nums = [342,456,233,74,221,22]
max = -math.inf
for num in nums:
    if num>max and num % 2 != 0:
        max = num
print(max)

# имеется список символов chars = ['К','Л','М','Н']
# 1) необходимо вывести на экран все возможные комбинации 4х символьных слов
# 2) каждая строка вывода на экран должна быть пронумерована
# 3) узнать на какой строке (номер) находится слово "МЛКН"
chars = ['К','Л','М','Н']
counter = 1
wordPosition = 0
for char1 in chars:
    for char2 in chars:
        for char3 in chars:
            for char4 in chars:
                word = char1+char2+char3+char4
                if(word == "МЛКН"):
                    wordPosition = counter
                print(str(counter)+") "+word)
                counter += 1
print("Слово 'МЛКН' находится под номером "+str(wordPosition))