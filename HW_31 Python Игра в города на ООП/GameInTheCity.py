from cities import cities_list
from dataclasses import dataclass
from typing import List, Set
import json
import os

os.system("cls") # очищение терминала



#---Работа с JSON-файлом---
class JsonFile:
    """
    Класс для работы с JSON-файлом (чтение и запись)
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_data(self, data):
        """Запись данных в JSON-файл"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Данные успешно записаны в {self.file_path}")
        except Exception as e:
            print(f"Ошибка при записи JSON: {e}")

    def read_data(self):
        """Чтение данных из JSON-файла"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден! Создайте его.")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в {self.file_path}. Возможно, файл пустой.")
            return []
        
#---Датакласс для представления города---
@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

#---Сериализация данных из JSON в объекты City---
class CitiesSerializer:
    def __init__(self, city_data):
        """
        Инициализирует список города, создавая экземпляры City
        """
        self.city_data = city_data
        self.cities = self.create_city_objects()

    def create_city_objects(self):
        """
        Преобразует данные из JSON в список объектов города
        """
        cities = []
        for city in self.city_data:
            cities.append(City(
                name = city["name"],
                population = city["population"],
                subject = city["subject"],
                district = city["district"],
                latitude = float(city["coords"]["lat"]),
                longitude = float(city["coords"]["lon"])
            ))
        return cities

    def get_all_cities(self) -> List[City]:
        """
        Возвращает список всех городов
        """
        return self.cities
    
#---Логика игры в города---
class CityGame:
    def __init__(self, cities: List[City]):
        """
        Инициализирует игру в города
        """
        self.cities = cities
        self.mistakes = 0
        self.score_user = 0
        self.score_comp = 0
        self.last_letter = ""
        self.used_cities: Set[str] = set()

    def start_game(self):
        """
        Начало игры. Человек ходит первым
        """
        print("Игра началась! Твой ход.")
        
    def human_turn(self):
        """
        Обрабатывает ход человека
        """
        while True:
            city_input = input("Введите город или 'Стоп' для завершения игры: ").strip().capitalize()
            if city_input == "Стоп":
                return False

            city_names = [city.name.capitalize() for city in self.cities]
            used_cities = [city.lower() for city in self.used_cities]

            if city_input not in city_names:
                print("Такого города нет. Попробуйте снова")
                self.mistakes += 1
                if self.check_game_over():
                    return False
                continue
            if city_input in self.used_cities:
                print("Этот город уже был использован. Подумай ещё")
                self.mistakes += 1
                if self.check_game_over():
                    return False
                continue
            if self.last_letter and not city_input.startswith(self.last_letter.upper()):
                print(f'Город должен начинаться на букву "{self.last_letter.upper()}". Попробуйте снова')
                self.mistakes += 1
                if self.check_game_over():
                    return False
                continue
            
            self.mistakes = 0  
            self.used_cities.add(city_input)
            self.score_user += 1
            self.last_letter = self.get_last_valid_letter(city_input)
            return True
            

    def get_last_valid_letter(self, city_name: str) -> str:
        """
        Определяет последнюю букву города, исключая 'ь', 'ъ','ы'
        """
        for letter in reversed(city_name):
            if letter.lower() not in "ьъы":
                return letter.lower()
        return city_name[-1].lower()  # на случай, если вдруг все буквы запрещены
    
    def computer_turn(self):
        """
        Ход компьютера
        """
        used_cities = [city.lower() for city in self.used_cities]
        for city in self.cities:
            if city.name.lower().startswith(self.last_letter) and city.name not in self.used_cities:
                print(f'Компьютер выбрал город: {city.name}')
                self.used_cities.add(city.name)
                self.score_comp += 1
                self.last_letter = self.get_last_valid_letter(city.name)
                return True

        print("Компьютер не смог назвать город и проиграл.")
        return False
    
    #---Проверка конца игры---
    def check_game_over(self):
        """
        Проверяет завершения игры
        """
        if self.mistakes >= 3:
            print(f"\nИгра окончена! Ты сделал {self.mistakes} ошибки.")
            print(f"Счет: Ты - {self.score_user}, Компьютер - {self.score_comp}")
            return True
        return False
        
    def save_game_state(self):
        """
        Сохраняет состояние игры в файл
        """
        game_state = {
            "score_user": self.score_user,
            "score_comp": self.score_comp,
            "used_cities": list(self.used_cities),
            "mistakes": self.mistakes
        }
        with open("game_state.json", "w") as file:
            json.dump(game_state, file)
        print("Состояние игры сохранено!")

#---Управление игрой---
class GameManager:
    """
    Фасад, который инкапсулирует взаимодействие между компонентами
    """
    def __init__(self, json_file: JsonFile, cities_serializer: CitiesSerializer, city_game: CityGame):
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game


    def __call__(self):
        """
        Запускает игру
        """
        self.run_game()

    def run_game(self):
        """
        Координирует выполнения игры
        """
        self.city_game.start_game()
        while True:
            if not self.city_game.human_turn():  # Первый ход теперь делает человек
                break
            if self.city_game.check_game_over():
                break
            if not self.city_game.computer_turn():
                break
            if self.city_game.check_game_over():
                break

        self.display_game_result()

    def display_game_result(self):
        """
        Отображает результаты после завершения игры
        """
        print(f"Игра окончена.")
        if self.city_game.score_comp > self.city_game.score_user:
            print(f"Победил компьютер! Со счетом {self.city_game.score_comp} - {self.city_game.score_user}")
        elif self.city_game.score_user > self.city_game.score_comp:
            print(f"Ты подебил! Со счетом {self.city_game.score_comp} - {self.city_game.score_user}")

        else:
            print(f"Ничья! Со счетом {self.city_game.score_comp} - {self.city_game.score_user}")

#---Запуск игры---
if __name__ == "__main__":
    json_file = JsonFile("cities.json")
    json_file.write_data(cities_list)
    data = json_file.read_data()
    cities_data = json_file.read_data()
    cities_serializer = CitiesSerializer(cities_data)
    city_game = CityGame(cities_serializer.get_all_cities())
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager()