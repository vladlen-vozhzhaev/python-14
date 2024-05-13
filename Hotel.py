class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms

    def getFreeRooms(self):
        print("Список свободных комнат:")
        for room in self.rooms:
            if not room.reserved:
                print(room.number)
    def reserveRoom(self):
        roomNumber = int(input("Введите номер комнты для бронирования: "))
        error = True
        for room in self.rooms:
            if (roomNumber == room.number and not room.reserved):
                room.reserved = True
                error = False
                print("Комната "+str(roomNumber)+" забронирована")
        if error:
            print("Ошибка при бронировании комнаты")
    def getReservedRooms(self):
        for room in self.rooms:
            if room.reserved:
                print(room.number)
    def filter(self):
        userSelectWifi = input("Нужен ли в комнате wifi? Да/Нет: ")
        userSelectTv = input("Нужен ли в комнате tv? Да/Нет: ")
        for room in self.rooms:
            if(
                    (room.wifi and userSelectWifi == "Да" or not room.wifi and userSelectWifi == "Нет")
                    and (room.tv and userSelectTv == "Да" or not room.wifi and userSelectTv == "Нет")
            ):
                print(room.number)

class Room:
    def __init__(self, number, place, tv, wifi):
        self.number = number
        self.place = place
        self.tv = tv
        self.wifi = wifi
        self.reserved = False

hotel = Hotel([
    Room(11, 3, True, True),
    Room(12, 2, False, False),
    Room(13, 2, False, True),
    Room(21, 1, True, True),
    Room(22, 1, False, False),
    Room(23, 3, False, True),
    Room(31, 2, True, True),
    Room(32, 3, True, False),
    Room(33, 1, True, True),
])
def start():
    command = input("Введите команду: ")
    while command != "exit":
        if command == "getFreeRooms":
            hotel.getFreeRooms()
        elif command == "reserveRoom":
            hotel.reserveRoom()
        elif command == "getReservedRooms":
            hotel.getReservedRooms()
        elif command == "filter":
            hotel.filter()
        command = input("Введите команду: ")


start()