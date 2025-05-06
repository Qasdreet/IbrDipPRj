import sqlite3

DB_NAME = 'inventory.db'

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        brand TEXT NOT NULL,
        quantity INTEGER DEFAULT 0,
        price REAL,
        status TEXT DEFAULT 'на складе'
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_id INTEGER,
        operation_type TEXT,
        quantity INTEGER,
        date TEXT,
        comment TEXT,
        FOREIGN KEY (phone_id) REFERENCES phones (id)
    )
    ''')

    conn.commit()
    conn.close()

# Функции для работы с базой данных
def add_phone(model, brand, quantity, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO phones (model, brand, quantity, price) VALUES (?, ?, ?, ?)',
                   (model, brand, quantity, price))
    conn.commit()
    conn.close()

# Функция для обновления данных телефона
def get_all_phones():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phones')
    phones = cursor.fetchall()
    conn.close()
    return phones

# Функция для фильтрации телефонов по бренду
def get_phones_by_brand(brand):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phones WHERE brand LIKE ?', ('%' + brand + '%',))
    phones = cursor.fetchall()
    conn.close()
    return phones

# Функция для фильтрации телефонов по цене
def sort_phones_by_price(ascending=True):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    order = 'ASC' if ascending else 'DESC'
    cursor.execute(f'SELECT * FROM phones ORDER BY price {order}')
    phones = cursor.fetchall()
    conn.close()
    return phones
