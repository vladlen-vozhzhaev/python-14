# Уровень здоровья не может превышать 100ед.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__hp = 100
    def sayHi(self):
        print("Привет, меня зовут "+self.name+" мне "+str(self.age)+" лет")
    def get_private_hp(self):
        return self.__hp
    def set_private_hp(self, value):
        if self.__hp+value >= 100:
            self.__hp = 100
        else:
            self.__hp += value

person1 = Person("Иван", 40)
person2 = Person("Алекс", 35)
person3 = Person("Вася", 30)
person4 = Person("Петя", 34)
person5 = Person("Коля", 28)
medKit = 50
print(person1.get_private_hp())
person1.set_private_hp(-30)
print(person1.get_private_hp())
person1.set_private_hp(medKit)
print(person1.get_private_hp())