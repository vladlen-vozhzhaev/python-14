import http.client

conn = http.client.HTTPSConnection("vozhzhaev.ru")
conn.request("GET", "/test.php")
response = conn.getresponse()
text = response.read().decode("utf-8")
print(text)
conn.close()
file = open("folder/test.txt", 'w')
file.write(text)
file.close()
