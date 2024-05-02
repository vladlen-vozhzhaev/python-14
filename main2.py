login = input("Введите логин: ")
password = input("Введите пароль: ")
if login == "admin" and password == "123":
    print("Доступ разрешен! - ADMIN")
elif login == "user" and password == "321":
    print("Доступ разрешен! - USER")
else:
    print("Доступ запрещен!")