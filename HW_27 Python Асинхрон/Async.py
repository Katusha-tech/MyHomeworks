import os
import asyncio

from openai import AsyncOpenAI
from dotenv import load_dotenv
from hw_27_data import DATA
from typing import List, Dict 
import json

load_dotenv() # загружаем переменные окружения

# константы

VSE_GPT_KEY = os.getenv("VSE_GPT_KEY")
BASE_URL = os.getenv("BASE_URL","https://api.vsegpt.ru/v1")
MAX_CHUNK_SIZE = 5000 # Максимальная длина текста для 1 запроса к API
SLEEP_TIME = 4 # Задержка между запросами
OUTPUT_FILE = "lecture_summary.md"
PROMPT_THEME = """
Привет!

Определи общую тему  текста. И постарайся максимально полно и точно описать её,
с использованием пунктов и подпунктов.

Не додумывай того, чего там небыло.
Исключи small talks.
"""

PROMPT_TIMESTAMPS = """
Привет!

Ты - ассистент по созданию таймкодов для видео.
Тебе будет предоставлен текст с таймкодами из видео.
Твоя задача - создать краткое описание каждого смыслового блока.
Ты не должен использовать полное цитирование. Создай краткое описание для блока.
Каждый блок должен начинаться с таймкода в формате чч:мм:сс.
Описание должно быть одним предложением, передающим суть начинающегося отрезка.
Игнорируй слишком короткие фрагменты или паузы.
Объединяй связанные по смыслу части в один большой блок.
Описания должны быть в стиле, как это обычно делают на youtube.



ВАЖНО.
СТРОГИЕ ПРАВИЛА:
1. Для видео длительностью:
   - до 30 минут: максимум 5 таймкодов
   - 30-60 минут: максимум 8 таймкодов
   - 1-2 часа: максимум 10 таймкодов
   - 2+ часа: максимум 15 таймкодов

2. Минимальный интервал между таймкодами:
   - для коротких видео (до 30 мин): 3-5 минут
   - для длинных видео: 10-15 минут

3. Объединяй близкие по смыслу темы в один таймкод

ВАЖНО: Если ты превысишь количество таймкодов - твой ответ будет отклонён!

В твоём ответе должны быть только таймкоды и описания.
Никаких других комментариев или пояснений.

КАК ПИСАТЬ?

Ты не пишешь описательные, длинные предложения. 
Вроде: "Пояснение адаптивного подхода к верстке на примере Visual Studio Code, где контент перестраивается в зависимости от размера экрана. "

Ты пишешь короткий, ёмкий вариант.
"Адаптивный подход к вёрстке. Пример в Visual Studio Code. Контент перестраивается в зависимости от размера экрана."
Или даже ещё немного короче.

Спасибо!
"""

PROMPT_CONSPECT_WRITER = """
Привет!
Ты опытный технический писатель. Ниже, я предоставляю тебе полный текст лекции а так же ту часть,
с которой ты будешь работать.

Ты великолепно знаешь русский язык и отлично владеешь этой темой.

Тема занятия: {topic}

Полный текст лекции:
{full_text}

Сейчас я дам тебе ту часть, с котороый ты будешь работать. Я попрошу тебя написать конспект лекции.
А так же блоки кода.

Ты пишешь в формате Markdown. Начни с заголовка 2го уровня.
В тексте используй заголовки 3го уровня.

Используй блоки кода по необходимости.

Отрезок текста с которым ты работаешь, с которого ты будешь работать:
{text_to_work}
"""
# Инициализация асинхронного клиента
client = AsyncOpenAI(api_key=VSE_GPT_KEY, base_url=BASE_URL)

# Проверка наличия API-ключа
if not VSE_GPT_KEY:
    raise ValueError("API-ключ VSE_GPT_KEY не найден! Убедитесь, что он задан.")



def second_to_timescode(seconds: float)-> str:
    """
    Конвертация секунд в формат таймкода чч:мм:сс
    """
    if seconds is None:
        return "00:00:00"
    hours = int(seconds//3600)
    minutes = int((seconds % 3600) //60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def add_timestamp_text(data: list[dict]) -> list[dict]:
    """
    Добавляет в словарь ключ "timestamp_text"
    :param data: список словарей с данными
    :return: список словарей с добавленными ключом "timestamp_text"
    """
    for item in data:
        start_time = second_to_timescode(item["timestamp"][0])
        end_time = second_to_timescode(item["timestamp"][1])
        item["timestamp_text"] = [start_time, end_time]
    return data

async def get_ai_request(prompt: str, max_retries: int = 3, base_delay: float = 2.0):
    """
    Отправляет запрос к API с механизмом повторных попыток base_delay - начальная задержка, которая будет увеличиваться экспоненциально
    :param prompt: текст запроса
    :param max_retries: максимальное количество попыток
    :param base_delay: начальная задержка между попытками
    :return: ответ от API
    """
    for attempt in range(max_retries):
        try:
            response = await client.chat.completions.create(
                model = "openai/gpt-4o-mini",
                messages = [{"role": "user", "content": prompt}],
                max_tokens = 16000, # выдать токенов
                temperature = 0.7, # стандартно от 0.5 до 0.8
            )
            return response.choices[0].message.content
        
        except openai.RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) # Экспоненциальное увеличение задержки
            await asyncio.sleep(delay)

def split_text_to_chunks(data: list) -> list:
    """
    Разбивание текста на чанки(мелкие кусочки/отрезки), но не более MAX_CHUNK_SIZE символов
    """
    chunks = []
    current_chunk = ""

    for item in data:
        text = item["text"].strip() 
        if len(current_chunk) + len(text) + 1 <= MAX_CHUNK_SIZE: # +1 для пробела
            current_chunk += " " + text if current_chunk else text
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = text

    if current_chunk:
        chunks.append(current_chunk)

    return chunks



