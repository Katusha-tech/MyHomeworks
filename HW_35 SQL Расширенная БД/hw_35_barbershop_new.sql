-- 1 часть. Создание новых таблиц и доработка тех, которые были созданы.

-- 1. Модификация таблицы Masters_services. Добавить поля price и duration_minutes;

BEGIN TRANSACTION;

ALTER TABLE Masters_services
ADD COLUMN price REAL DEFAULT NULL;

ALTER TABLE Masters_services
ADD COLUMN duration_minutes INTEGER NULL;

COMMIT;

-- 2. Модификация таблицы Appointments. Добавить поле start_time, end_time, status;

BEGIN TRANSACTION;

ALTER TABLE Appointments
ADD COLUMN start_time TEXT NOT NULL DEFAULT '00:00';

ALTER TABLE Appointments
ADD COLUMN end_time TEXT NOT NULL DEFAULT '00:00';

COMMIT;

-- 2.1 Создаем новую таблицу Appointments_new

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS Appointments_new (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (master_id) REFERENCES Masters(master_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES StatusDictionary(status_id) ON DELETE RESTRICT
);

-- 2.2 Перенос данных из старой таблицы Appointments в новую таблицу Appointments_new

INSERT INTO Appointments_new (appointment_id, name, phone, date, master_id, status_id)
SELECT appointment_id, name, phone, date, master_id, 
        (SELECT status_id FROM StatusDictionary WHERE name = Appointments.status)
FROM Appointments;

-- 2.3 Удаление старой таблицы Appointments
DROP TABLE Appointments;

-- 2.4 Переименование новой таблицы в Appointments

ALTER TABLE Appointments_new RENAME TO Appointments;

COMMIT;

-- 3. Новые таблицы;
-- 3.1 Таблица StatusDictionary;

CREATE TABLE IF NOT EXISTS StatusDictionary (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

--  Заполнение таблицы StatusDictionary
INSERT INTO StatusDictionary (name, description)
VALUES ('Подтверждена', 'Клиент подтвердил запись');

INSERT INTO StatusDictionary (name, description)
VALUES ('Ожидает', 'Клиент ожидает подтверждения записи');

INSERT INTO StatusDictionary (name, description)
VALUES ('Отмена', 'Клиент отменил запись');


-- 3.2 Таблицы Reviews;

CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comment TEXT,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE
);

-- 3.3 Таблица MasterSchedule;

CREATE TABLE IF NOT EXISTS MasterSchedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    master_id INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL CHECK(day_of_week BETWEEN 1 AND 7),
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    comment TEXT,
    FOREIGN KEY (master_id) REFERENCES Masters(master_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES StatusDictionary(status_id) ON DELETE CASCADE
);

-- Заполнение таблицы MasterSchedule
-- Мастер 1 (работает с понедельника по воскресенье)
INSERT INTO MasterSchedule (master_id, day_of_week, start_time, end_time, status_id, comment) 
VALUES (1, 1, '09:00', '18:00', 1, 'Рабочий день'),
        (1, 2, '09:00', '18:00', 1, 'Рабочий день'),
        (1, 3, '09:00', '18:00', 1, 'Рабочий день'),
        (1, 4, '09:00', '18:00', 1, 'Рабочий день'),
        (1, 5, '09:00', '18:00', 1, 'Рабочий день'),
        (1, 6, '10:00', '15:00', 1, 'Сокращённый день'),
        (1, 7, 'Выходной', 'Выходной', 2, 'Выходной');

-- Мастер 2 (другое расписание)
INSERT INTO MasterSchedule (master_id, day_of_week, start_time, end_time, status_id, comment) 
VALUES (2, 1, '10:00', '19:00', 1, 'Рабочий день'),
        (2, 2, '10:00', '19:00', 1, 'Рабочий день'),
        (2, 3, '10:00', '19:00', 1, 'Рабочий день'),
        (2, 4, '10:00', '19:00', 1, 'Рабочий день'),
        (2, 5, '10:00', '19:00', 1, 'Рабочий день'),
        (2, 6, '10:00', '14:00', 1, 'Сокращённый день'),
        (2, 7, 'Выходной', 'Выходной', 2, 'Выходной');

SELECT * FROM MasterSchedule;

-- 2 часть. Серия запросов в БД Barbershop
-- 2.1 Новая запись записи на услугу

BEGIN TRANSACTION;

-- Вставляем запись о приеме в  таблицу Appointments
INSERT INTO Appointments (name, phone, date, master_id, status_id, start_time, end_time)
VALUES ('Карл', '+79991234567', '2023-05-15', 1, 1, '10:00', '11:00');

-- Получаем ID последней записи в таблице Appointments и вставляем его в таблицу Appointments_services
INSERT INTO Appointments_services (appointment_id, service_id)
VALUES (last_insert_rowid(), 1);

COMMIT;

-- 2.2 Изменение статуса записи

BEGIN TRANSACTION;

UPDATE Appointments
SET status_id = (
    SELECT status_id
    FROM StatusDictionary
    WHERE name = 'Отмена'
)
WHERE appointment_id = 1;

COMMIT;

-- 2.3 Корректировка цены услуги

BEGIN TRANSACTION;

UPDATE Masters_services
SET price = 2500
WHERE service_id = 1 AND master_id = 1;

COMMIT;

-- 2.4 Обновление расписания мастера

BEGIN TRANSACTION;

UPDATE MasterSchedule
SET start_time = '12:00', end_time = '14:00'
WHERE master_id = 1 AND day_of_week = 1;
COMMIT;

-- 2.5 Добавление нового статуса

BEGIN TRANSACTION;

INSERT INTO StatusDictionary (name, description)
VALUES ('Завершена', 'Клиенту услуга выполнена');

COMMIT;

-- 2.6 Добавление отзыва клиента

BEGIN TRANSACTION;

INSERT INTO Reviews (appointment_id, rating, comment)
SELECT 1, 5, 'Работа выполнена на отлично!'
WHERE EXISTS (SELECT 1 FROM Appointments WHERE appointment_id = 1);

COMMIT;

-- 2.7 Массовая вставка новых услуг

BEGIN TRANSACTION;

INSERT INTO Services (title, description, price)
VALUES ('Колорирование', 'Окрашшивание прядей в разный цвет', 15000),
        ('Завивка', 'Создание кудрей', 6500);
COMMIT;

-- 2.8 Отмена записи на услугу

BEGIN TRANSACTION;

-- Удаляем запись из таблицы Appointments_services
DELETE FROM Appointments_services
WHERE appointment_id = 1;

-- Обновляем статус записи в таблице Appointments
UPDATE Appointments
SET status_id = (SELECT status_id
                FROM StatusDictionary
                WHERE name = 'Отмена')
WHERE appointment_id = 1;

COMMIT;




