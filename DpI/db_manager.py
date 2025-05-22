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
            specs TEXT,  -- Новое поле для хранения характеристик
            status TEXT DEFAULT 'на складе'
        )
    ''')
    conn.commit()
    conn.close()

# Функции для работы с базой данных
def add_phone(model, brand, quantity, price, specs):
       conn = sqlite3.connect(DB_NAME)
       cursor = conn.cursor()
       cursor.execute('''
           INSERT INTO phones (model, brand, quantity, price, specs) 
           VALUES (?, ?, ?, ?, ?)
       ''', (model, brand, quantity, price, specs))
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

        # Добавляем проверку на пустую строку
        if not brand:
            return []

        cursor.execute("SELECT * FROM phones WHERE brand LIKE ?", ('%' + brand + '%',))
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
