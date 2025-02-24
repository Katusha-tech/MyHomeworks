from PolAndNas import *
import os

# Создание экземпляров классов
json_file = JsonFile("file.json")
txt_file = TxtFile("file.txt")
csv_file = CsvFile("file.csv")

print(json_file)
print(txt_file)
print(csv_file)

# Запись данныхв файлы 
json_file.write({"name": "Савелий", "age": 25})
txt_file.write("Hello, world!")
csv_file.write([["Name", "Age"], ["Руслан", 48]])

print(json_file.read())
print(txt_file.read())
print(csv_file.read())

# Дозапись данных в файлы
json_file.append([{"name": "Зоя", "age": 59}])
txt_file.append("Goodbye!")
csv_file.append(["Анастасия", 45])

print(json_file.read())
print(txt_file.read())
print(csv_file.read())

os.remove("file.json")
os.remove("file.txt")
os.remove("file.csv")
