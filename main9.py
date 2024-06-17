import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'test14'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
login = input("Введите логин: ")
data = (login,)
cursor.execute("DELETE FROM users WHERE login = %s", data)
conn.commit()
# name = input("Введите новое имя: ")
# data = (name, login)
# cursor.execute("UPDATE `users` SET `name`= %s WHERE login = %s", data)
# conn.commit()
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# data = (name, login, password)
# cursor.execute(f"INSERT INTO `users`(`name`, `login`, `pass`) VALUES (%s, %s, %s)", data)
# conn.commit()
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# data = (login, password)
# cursor.execute("SELECT * FROM users WHERE login = %s AND pass = %s", data)
# for row in cursor.fetchall():
#     print(row)