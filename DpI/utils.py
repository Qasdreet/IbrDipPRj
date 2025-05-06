from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_phone_data(model, brand, quantity, price):
    if not model or not brand:
        return False
    if not isinstance(quantity, int) or not isinstance(price, (int, float)):
        return False
    return True
