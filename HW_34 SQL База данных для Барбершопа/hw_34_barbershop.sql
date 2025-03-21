-- Создание таблиц и связей

-- Создание таблицы "Мастера"
CREATE TABLE IF NOT EXISTS Masters (
    master_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL
);

-- Создание таблицы "Услуги"
CREATE TABLE IF NOT EXISTS Services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
);

-- Создание таблицы "Запись на услуги"
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER NOT NULL,
    status TEXT CHECK (status IN ('Подтверждена', 'Отмена', 'Ожидает')) NOT NULL,
    FOREIGN KEY (master_id) REFERENCES Masters(master_id) ON DELETE CASCADE
);


-- Таблица для связи мастеров и услуг
CREATE TABLE IF NOT EXISTS Masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES Masters(master_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE
);

-- Таблица для связи записей и услуг 
CREATE TABLE IF NOT EXISTS Appointments_services (
    appointment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE
);

-- Внесение данных 

-- Данные о мастерах
INSERT INTO Masters (first_name, middle_name, last_name, phone)
VALUES ('Павел', 'Петрович', 'Волосик', '79524158563'),
       ('Эдвард', 'Семенович', 'Рукиножницы', '78529587452');    

-- Данные об услугах
INSERT INTO Services (title, description, price)
VALUES ('Филировка', 'Срез кончиков волос', 1000),    
       ('Стрижка', 'Стрижка женского волоса', 1500),    
       ('Укладка', 'Укладка волос', 1200),
       ('Окрашевание', 'Покраска волос в любой цвет', 3000),
       ('Ламинирование', 'Придание волосам блеска', 1700);

-- Связывание мастеров и услуг
INSERT INTO Masters_services (master_id, service_id)
VALUES (1, 1), (1, 2), (1, 3), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5);

-- Добавление записей
INSERT INTO Appointments (name, phone, master_id, status)
VALUES ('Иван', '79587412589', 1, 'Подтверждена'),
       ('Петр', '79526854578', 2, 'Ожидает'),
       ('Сергей', '79124569852', 1, 'Подтверждена'),
       ('Марина', '79754852369', 2, 'Отмена'),
       ('Елена', '795562581463', 1, 'Подтверждена');

-- Связывание записей и услуг
INSERT INTO Appointments_services (appointment_id, service_id)
VALUES (1, 1), (2, 5), (3, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 5);






