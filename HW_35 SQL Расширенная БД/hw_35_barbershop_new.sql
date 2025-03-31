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




SELECT * FROM StatusDictionary;
