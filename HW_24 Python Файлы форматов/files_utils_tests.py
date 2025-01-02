from Form_file import *
import os

def test_json_operations():
    # Тестовые данные для JSON
    test_data = [
        {"имя": "Иван", "возраст": 25},
        {"имя": "Мария", "возраст": 30}
    ]
    
    # Запись JSON
    write_json(test_data, "test.json")
    
    # Чтение JSON
    read_data = read_json("test.json")
    print("JSON данные:", read_data)
    
    # Добавление в JSON
    new_data = [{"имя": "Петр", "возраст": 35}]
    append_json(new_data, "test.json")

def test_csv_operations():
    # Тестовые данные для CSV
    test_data = [
        ["Имя", "Возраст", "Город"],
        ["Иван", "25", "Москва"],
        ["Мария", "30", "Санкт-Петербург"]
    ]
    
    # Запись CSV
    write_csv(test_data, "test.csv")
    
    # Чтение CSV
    read_data = read_csv("test.csv")
    print("CSV данные:", read_data)
    
    # Добавление в CSV
    new_data = ["Петр", "35", "Казань"]
    append_csv(new_data, "test.csv")

def test_txt_operations():
    # Тестовые данные для TXT
    test_data = "Это тестовая строка для записи в файл."
    
    # Запись TXT
    write_txt(test_data, "test.txt")
    
    # Чтение TXT
    read_data = read_txt("test.txt")
    print("TXT данные:", read_data)
    
    # Добавление в TXT
    append_txt("Это дополнительная строка.", "test.txt")

def test_yaml_operations():
    # Создание тестового YAML файла с погодными данными
    city = "London"
    key = "58ffee3f9e03a1428d9eefbabc922e5c"
    weather_data = f"""
    weather_app:
      settings:
        city: {city}
        update_interval: 30
        units: metric
      api:
        key: {key}
        base_url: https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}
      display:
        temperature: true
        humidity: true
        wind_speed: true
        pressure: false
    """
    
    with open("test.yaml", "w", encoding="utf-8") as file:
        file.write(weather_data)
    
    # Чтение YAML
    yaml_data = read_yaml("test.yaml")
    print("YAML данные:", yaml_data)

def main():
    # Очистка консоли
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Тестирование операций с файлами:\n")
    
    print("=== JSON Тесты ===")
    test_json_operations()
    print("\n=== CSV Тесты ===")
    test_csv_operations()
    print("\n=== TXT Тесты ===")
    test_txt_operations()
    print("\n=== YAML Тесты ===")
    test_yaml_operations()

if __name__ == "__main__":
    main()
