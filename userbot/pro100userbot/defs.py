from datetime import *
from time import sleep
from prettytable import from_db_cursor as fdc, from_csv
from sqlite3 import connect
from mtranslate import translate as tr
from pycbrf.toolbox import ExchangeRates as ExRa

rates = ExRa()

#функция для вычисления времени, которое понадобится на выполнение команды
def leadtime(sec, kof):
    sec = sec * kof
    minut = sec // 60
    hour1 = minut // 60
    if minut >= 60:
        minute = minut % 60
    else:
        minute = minut
    if sec >= 60:
        sec1 = sec % 60
    else:
        sec1 = sec
    if hour1 >= 24:
        hour = hour1 % 24
    else:
        hour = hour1
    day = hour1 // 24
    o = 0
    now = datetime.now()
    now1 = now
    now2 = str(now)
    start = now2.split(".")[0]
    en = now + timedelta(days=day, hours=hour, minutes=minute, seconds=sec1)
    en1 = str(en)
    end = en1.split(".")[0]
    
    out1 = f"Приблизительное время операции: **{day}d {hour}h {minute}min {sec1}sec**\nНачало операции: **{start}** \nПриблизительный конец операции: **{end}**"
    
    return out1, now1

def end(now1):
    now = datetime.now()
    now2 = now - now1
    now = str(now2)
    now = now.split(".")[0]
    
    end = f"Операция длилась: {now}"
    
    return end

def add(channel_id):
    with connect("bot.db") as db:
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS donors(
        id INTEGER PRIMARY KEY,
        donor BIGINT
        )""")
        db.commit()
        sql.execute(f"SELECT donor FROM donors WHERE donor = {channel_id}")
        db.commit()
        if sql.fetchone() is None:
            sql.execute("INSERT INTO donors VALUES(?,?)", (None, channel_id))
            db.commit()
            out = "Запись сохранена!"
        else:
            out = "Запись уже имеется!"
        
        return out

def delete(str_id):
    with connect("bot.db") as db:
        sql = db.cursor()
        sql.execute(f"SELECT * FROM donors WHERE donor = {str_id} ")
        if sql.fetchone() is None:
            out = "Запись не существует!"
        else:
            sql.execute(f"DELETE FROM donors WHERE donor = {str_id}")
            db.commit()
            out = "Запись удалена!"
        
        return out

def channels():
    items = []
    with connect("bot.db") as db:
        sql = db.cursor()
        for value in sql.execute("SELECT donor FROM donors").fetchall():
            items.append(value[0])
        return items

def table():
    with connect("bot.db") as db:
        sql = db.cursor()
        sql.execute("SELECT * FROM donors")
        my_table = fdc(sql)
        
    return my_table

def check(channel_id, msg_id):
    with connect("bot.db") as db:
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS metadata(
        id INTEGER PRIMARY KEY,
        info FLOAT
        )""")
        db.commit()
        
        sql.execute(f"SELECT id FROM donors WHERE donor = {channel_id}")
        db.commit()
        
        info = float(f"{sql.fetchone()[0]}.{msg_id}")
        
        sql.execute(f"SELECT info FROM metadata WHERE info = {info}")
        
        if sql.fetchone() is None:
            sql.execute("INSERT INTO metadata VALUES(?,?)", (None, info))
            db.commit()
            out = 0
        else:
            out = 1
        
        return out

def ms(list1):
    text = ""
    for txt in list1:
        text += f" {txt}"
    return text

def translator(l1,l2,txt):
    text = ms(txt)
    results = tr(text, l1, l2)
    return results

def langueges():
    with open("languege.csv") as fp:
        mytable = from_csv(fp)
        
        return mytable

def converter(data):
    cur = data[0]
    cur1 = data[1]
    num = float(data[2])
    if cur1.lower() == "rub":
        currency = float(rates[cur.upper()].rate)
        result = num * currency
    
    elif cur.lower() == "rub":
        currency1 = float(rates[cur1.upper()].rate)
        result = num / currency1
    
    else:
        currency = float(rates[cur.upper()].rate)
        currency1 = float(rates[cur1.upper()].rate)
        result = (currency * num) / currency1
    
    return round(result, 2)

def currencies():
    with open("currencies.csv") as fp:
        mytable = from_csv(fp)
    
    return mytable