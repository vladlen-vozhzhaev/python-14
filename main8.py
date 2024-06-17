class Animal:
    def __init__(self, nickname, age, breed):
        self.nickname = nickname
        self.age = age
        self.breed = breed
        self.__hp = 100
    def run(self):
        print(f"{self.nickname} побежал(а)")
    def speak(self):
        print("Звук не назначен")

    def get_private_hp(self):
        return self.__hp

class Cat(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def speak(self):
        print("Мяу")

class Bird(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def fly(self):
        print(f"{self.nickname} полетела(а)")
    def speak(self):
        print("Чык чырык")

class Horse(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)

cat1 = Cat("Барсик", 4, "Дворняга")
bird1 = Bird("Кеша", 7, "Волнистый")
horse1 = Horse("Мустанг", 6, "Рысак")
horse1.speak()
cat1.run()
bird1.run()
bird1.fly()
cat1.speak()
bird1.speak()
print(horse1.get_private_hp())