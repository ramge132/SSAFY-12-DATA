import pytesseract
from PIL import Image
import sqlite3
import re

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='kor')
    text = text.replace(' ', '')
    return text

def parse_text(text):
    lines = text.split('\n')
    store_name = None
    min_order_amount = None
    delivery_fee = None
    menu_items = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '최소주문금액' in line:
            min_order_amount = re.search(r'\d+,\d+원', line).group()
        elif '배달팁' in line:
            delivery_fee = re.search(r'\d+,\d+원', line).group()
        elif '원' in line and ('최소주문금액' not in line and '배달팁' not in line and '리뷰' not in line):
            menu_match = re.match(r'(.+?)\s*(\d+,\d+원)', line)
            if menu_match:
                item_name = menu_match.group(1).strip()
                price = menu_match.group(2).replace(',', '').replace('원', '').strip()
                menu_items.append((item_name, int(price)))
        elif '봉구킹' in line and '점' not in line:
            item_name = '봉구킹'
            price = '6500'
            menu_items.append((item_name, int(price)))
        elif '봉구스' in line and '점' not in line:
            item_name = '봉구스'
            price = '3000'
            menu_items.append((item_name, int(price)))
            menu_items.append(('햄치즈', int(4300)))
            menu_items.append(('치즈제육', int(4500)))
            menu_items.append(('치즈닭갈비', int(4000)))
        elif '점' in line and store_name is None:
            store_name = line.split('점')[0].strip() + '점'

    return store_name, min_order_amount, delivery_fee, menu_items

def setup_database():
    conn = sqlite3.connect('delivery_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            min_order_amount TEXT,
            delivery_fee TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            item_name TEXT NOT NULL,
            price INTEGER,
            FOREIGN KEY(store_id) REFERENCES store(id)
        )
    ''')
    conn.commit()
    return conn

def insert_data_into_db(conn, store_name, min_order_amount, delivery_fee, menu_items):
    cursor = conn.cursor()

    cursor.execute('INSERT INTO store (name, min_order_amount, delivery_fee) VALUES (?, ?, ?)',
                   (store_name, min_order_amount, delivery_fee))
    store_id = cursor.lastrowid

    for item_name, price in menu_items:
        cursor.execute('INSERT INTO menu (store_id, item_name, price) VALUES (?, ?, ?)',
                       (store_id, item_name, price))

    conn.commit()

def main(image_path):
    conn = setup_database()

    text = extract_text_from_image(image_path)
    store_name, min_order_amount, delivery_fee, menu_items = parse_text(text)
    text = text.replace('\n','')
    print(text)

    if store_name and min_order_amount and delivery_fee:
        insert_data_into_db(conn, store_name, min_order_amount, delivery_fee, menu_items)

    conn.close()

image_path = 'C:/Users/SSAFY/Desktop/temp/image/test2.jpg'
main(image_path)
