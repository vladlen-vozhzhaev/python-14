class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print("Привет, меня зовут "+self.name+" мне "+str(self.age)+" лет")

person1 = Person("Иван", 40)
person2 = Person("Алекс", 35)
person3 = Person("Вася", 30)
person4 = Person("Петя", 34)
person5 = Person("Коля", 28)

person5.sayHi()