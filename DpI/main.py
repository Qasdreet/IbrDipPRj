import tkinter as tk
from tkinter import ttk, messagebox
from db_manager import init_db, add_phone, get_all_phones, get_phones_by_brand, sort_phones_by_price
from utils import validate_phone_data

# Инициализация базы данных
init_db()

# Функция для обновления таблицы
def refresh_table(data=None):
    for row in tree.get_children():
        tree.delete(row)

    phones = data if data is not None else get_all_phones()
    for phone in phones:
        tree.insert('', tk.END, values=phone)

# Функция для добавления телефона
def submit():
    model = entry_model.get()
    brand = entry_brand.get()
    try:
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения!")
        return

    if validate_phone_data(model, brand, quantity, price):
        add_phone(model, brand, quantity, price)
        refresh_table()
        messagebox.showinfo("Успех", "Телефон добавлен!")
    else:
        messagebox.showerror("Ошибка", "Неверные данные!")

# Функции для фильтрации и сортировки
def filter_by_brand():
    brand = entry_filter.get()
    filtered = get_phones_by_brand(brand)
    refresh_table(filtered)

# Функции для сортировки
def sort_price_asc():
    sorted_list = sort_phones_by_price(ascending=True)
    refresh_table(sorted_list)

# Функция для сортировки по цене по убыванию
def sort_price_desc():
    sorted_list = sort_phones_by_price(ascending=False)
    refresh_table(sorted_list)

root = tk.Tk()
root.title("Учет телефонов на складе")

# Создание интерфейса
tk.Label(root, text="Модель").grid(row=0, column=0)
entry_model = tk.Entry(root)
entry_model.grid(row=0, column=1)

tk.Label(root, text="Бренд").grid(row=1, column=0)
entry_brand = tk.Entry(root)
entry_brand.grid(row=1, column=1)

tk.Label(root, text="Количество").grid(row=2, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=2, column=1)

tk.Label(root, text="Цена").grid(row=3, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1)

tk.Button(root, text="Добавить", command=submit).grid(row=4, columnspan=2)


tk.Label(root, text="Фильтр по бренду").grid(row=5, column=0)
entry_filter = tk.Entry(root)
entry_filter.grid(row=5, column=1)
tk.Button(root, text="Фильтровать", command=filter_by_brand).grid(row=5, column=2)

tk.Button(root, text="↑ Сортировать по цене", command=sort_price_asc).grid(row=6, column=0)
tk.Button(root, text="↓ Сортировать по цене", command=sort_price_desc).grid(row=6, column=1)

columns = ('ID', 'Модель', 'Бренд', 'Количество', 'Цена', 'Статус')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=7, column=0, columnspan=3, pady=10)

refresh_table()

root.mainloop()

