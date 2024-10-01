# -*- coding: utf-8 -*-
import pymysql

# Настройки подключения к базе данных
db_config = {
    'user': 'your_user',  # замените на ваш MySQL пользователь
    'password': 'your_password',  # замените на ваш пароль
    'host': 'localhost',  # если сервер локальный
    'database': 'your_db',  # замените на название базы данных
    'charset': 'utf8'  # Установка кодировки utf8 для работы с кириллицей
}

# Подключение к базе данных
try:
    conn = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        charset='utf8',  # Поддержка utf-8 для MySQL
        use_unicode=True,  # Важно для работы с Unicode
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    print("Соединение с базой данных установлено успешно!")
except pymysql.MySQLError as err:
    print("Ошибка подключения к базе данных: {}".format(err))
    exit()

# Принудительная установка кодировки для текущего сеанса
try:
    cursor.execute("SET NAMES 'utf8';")
    cursor.execute("SET CHARACTER SET 'utf8';")
    cursor.execute("SET character_set_connection='utf8';")
    print("Кодировка UTF-8 установлена успешно для текущего сеанса.")
except pymysql.MySQLError as err:
    print("Ошибка при установке кодировки: {}".format(err))

# 4.1. Создать таблицу
create_table_query = """
CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) CHARACTER SET utf8,
    first_name VARCHAR(50) CHARACTER SET utf8,
    middle_name VARCHAR(50) CHARACTER SET utf8,
    age INT
) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;
"""

try:
    cursor.execute(create_table_query)
    conn.commit()
    print("Таблица people успешно создана с кодировкой UTF-8!")
except pymysql.MySQLError as err:
    print("Ошибка при создании таблицы: {}".format(err))

# 4.2. Заполнить таблицу 5-10 записями.
insert_data_query = """
INSERT INTO people (last_name, first_name, middle_name, age) 
VALUES (%s, %s, %s, %s)
"""

data = [
    ('Иванов', 'Иван', 'Иванович', 30),
    ('Петров', 'Петр', 'Петрович', 25),
    ('Сидоров', 'Алексей', 'Сергеевич', 40),
    ('Иванов', 'Андрей', 'Иванович', 35),
    ('Кузнецов', 'Николай', 'Павлович', 50)
]

try:
    cursor.executemany(insert_data_query, data)
    conn.commit()
    print("Данные успешно добавлены в таблицу!")
except pymysql.MySQLError as err:
    print("Ошибка при добавлении данных: {}".format(err))

# 4.3. Выборка людей с фамилией "Иванов"
select_query = "SELECT * FROM people WHERE last_name = 'Иванов';"

try:
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("Люди с фамилией 'Иванов':")
    for row in rows:
        print(row['last_name'], row['first_name'], row['middle_name'], row['age'])
except pymysql.MySQLError as err:
    print("Ошибка при выполнении запроса на выборку: {}".format(err))

# 4.4. Увеличить возраст на 1 для людей с фамилией "Иванов"
update_age_query = """
UPDATE people
SET age = age + 1
WHERE last_name = 'Иванов';
"""

try:
    cursor.execute(update_age_query)
    conn.commit()
    print("Возраст людей с фамилией 'Иванов' увеличен на 1!")
except pymysql.MySQLError as err:
    print("Ошибка при обновлении возраста: {}".format(err))

# 4.5. Удалить записи с фамилией "Иванов"
delete_query = """
DELETE FROM people WHERE last_name = 'Иванов';
"""

try:
    cursor.execute(delete_query)
    conn.commit()
    print("Люди с фамилией 'Иванов' удалены!")
except pymysql.MySQLError as err:
    print("Ошибка при удалении данных: {}".format(err))

# Закрытие соединения
cursor.close()
conn.close()
print("Соединение с базой данных закрыто.")

