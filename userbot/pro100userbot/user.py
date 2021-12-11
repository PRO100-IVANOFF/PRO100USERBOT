#импорты
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import random
from time import sleep
from math import sqrt
from defs import *
from datetime import *

#сессия
app = Client("igor")

#константы
LESYA = 757724042 #id бота
DAY = 86400 #день в секундах
GG = -1001569521657 #id модер-канала
MY_CHANNEL = "pro100_memes"

#команда fight
@app.on_message(filters.command("fight", prefixes=".") & filters.me)
def fight(_, msg):
    text = msg.text.split(".fight", maxsplit=1)[1]
    povtor = 60 * int(text)
    i = 0
    while i < povtor:
        app.send_message(LESYA, "бой")
        i += 1
        sleep(60)

#команда math
@app.on_message(filters.command("math", prefixes=".") & filters.me)
def math(_, msg):
    text = msg.text.split(".math", maxsplit=1)[1]
    chat_id = msg.chat.id
    try:
        summ = eval(text)
        msg.delete()
        app.send_message(chat_id, f"{text} = <strong>{round(summ, 2)}</strong>", parse_mode="html")
    except:
        msg.reply("Пример записан не верно!")

#команда sqrt
@app.on_message(filters.command("sqrt", prefixes=".") & filters.me)
def sqrte(_, msg):
    text = msg.text.split(".sqrt", maxsplit=1)[1]
    try:
        num = int(text)
        msg.edit(f"√{round(num, 2)} = **{sqrt(num)}**")
    except:
        msg.reply("Возникла ошибка!")
    
#команда hack
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
	perc = 0
	msg.edit("👮‍ Взлом пентагона в процессе ...")
	while perc < 99:
		try:
		    iq = 0
		    k = random.randint(1, 3)
		    while iq < k: 
			    perc1 = random.randint(5, 15)
			    perc2 = perc1 / 10
			    perc += perc2
			    if perc < 100:
			        perc += perc2
			    elif perc > 100:
			        perc = 100
			    text = "👮‍ Взлом пентагона в процессе ..." + str(round(perc, 2)) + "%"
			    msg.edit(text)
			    iq += 1
			    sleep(0.08)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🟢 Пентагон успешно взломан!")
	sleep(3)
	msg.edit("👽 Поиск секретных данных об НЛО ...")
	perc = 0
	while perc < 99:
		try:
		    iq = 0
		    k = random.randint(1, 3)
		    while iq < k:
			    perc1 = random.randint(5, 15)
			    perc2 = perc1 / 10
			    perc += perc2
			    if perc < 100:
			        perc += perc2
			    elif perc > 100:
			        perc = 100
			    text = "👽 Поиск секретных данных об НЛО ..." + str(round(perc, 2)) + "%"
			    msg.edit(text)
			    iq += 1
			    sleep(0.08)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

#команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) # 50 ms

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

#команда case
@app.on_message(filters.command("case", prefixes=".") & filters.me)
def lesya(_, msg):
    text = msg.text.split(".case", maxsplit=1)[1]
    lis = text.split()
    num = lis[0]
    try:
        pov = int(lis[1])
        povtor = pov // 4
        pov1 = povtor
        i = 2
        out, now1 = leadtime(pov1, i)
        povtor += 1
        app.reply(f"**case**\n\nБудет отправлено сообщений: **{povtor}**\n{out}")
        o = 0
        while o < povtor:
            try:
                app.send_message(LESYA, f"кейс о {num} 4")
                o += 1
                sleep(2)
            except FloodWait as e:
                sleep(e.x)
        end1 = end(now1)
        app.reply(f"**case**\n\nОперация завершена!\nСообщений было отправлено: **{povtor}**\n{end1}")
    except:
        msg.reply("Возникла ошибка!")

#команда cw
@app.on_message(filters.command("cw", prefixes=".") & filters.me)
def cw(_, msg):
    i = 0
    try:
        app.send_message("me", f"**КВ**\n\nФункция \"**КВ**\" успешно запущена!\n")
        app.send_message(LESYA, "зоотовары 6")
        app.send_message(LESYA, "зоотовары 7")
        app.send_message(LESYA, "зоотовары 8")
        app.send_message(LESYA, "кв начать")
    
        while i < 730:
            app.send_message(LESYA, "бой")
            i += 1
            sleep(60)
        app.send_message("me", f"**CW**\n\nOперация завершена!")

    except FloodWait as e:
        sleep(e.x)

#команда bonus
@app.on_message(filters.command("bonus", prefixes=".") & filters.me)
def bonus(_, msg):
    while True:
        try:
            app.send_message(LESYA, "Бонус")
            app.send_message(LESYA, "Вип бонус")
            sleep(3600*8)
        except FloodWait as e:
            sleep(e.x)

#команда shrug
@app.on_message(filters.command("shrug", prefixes=".") & filters.me)
def shrug(_,msg):
    msg.edit(" ¯\_(ツ)_/¯ ")

#команда donate
@app.on_message(filters.command("donate", prefixes=".") & filters.me)
def donate(_, msg):
    id_sum = msg.text.split(".donate", maxsplit=1)[1]
    huy = id_sum.split()
    try:
        id1 = huy[0]
        summ = huy[1]
        days = int(huy[2])
        i=0
        try:
            while i < days:
                app.send_message(LESYA, f"банк снять {summ}")
                app.send_message(LESYA, f"передать {id1} {summ}")
                i += 1
                sleep(DAY)
        except FloodWait as e:
            sleep(e.x)
    
    except:
        msg.reply("Возникла ошибка!")

#команда test
@app.on_message(filters.command("test", prefixes=".") & filters.me)
def test(_, msg):
    msg.edit("Тест произведён успешно!")

#команда city(город)
@app.on_message(filters.command("city", prefixes=".") & filters.me)
def city(_,msg):
    text = msg.text.split()
    try:
        house = text[1]
        num = text[2]
        kolvo = int(text[3])
        s = 1
        out, now = leadtime(kolvo, s)
        app.send_message(me, f"**CITY**\n\nБудет отправлено сообщений: **{kolvo}**\n{out}")
        
        i = 0
        while i < kolvo:
            app.send_message(LESYA, f"г {house} {num}")
            i += 1
            sleep(s)
            
        end1 = end(now)
        app.send_message(me, f"**CITY**\n\nОперация завершена!\nСообщений было отправлено: **{kolvo}**\n{end1}")
        #q+=1
    except:
        msg.reply("Возникла ошибка!\nВозможно вы забыли ввести необходимые данные!")

#граббер фото из каналов
@app.on_message(filters.photo & filters.chat(channels()))
def photo(_, msg):
    channel_username = msg.chat.username
    channel_id = msg.chat.id
    msg_id = msg.message_id
    mem = msg.photo.file_id
    value = check(channel_id, msg_id)
    time = str(datetime.now())
    time = time.split(".")[0]
    if value == 0:
        app.send_photo(GG, mem, f"CHANNEL:\t@{channel_username}\nID:\t{channel_id}\nMSG:\t{msg_id}\nTIME:\t{time}")
    else:
        pass

#команда db
@app.on_message(filters.command("db", prefixes=".") & filters.me)
def db(_, msg):
    i = msg.text.split()
    if i[1] == "-v":
        tab = table()
        msg.reply(f"`{tab}`")
        
    elif i[1] == "-d":
        t = delete(int(i[2]))
        msg.reply(t)
    
    elif i[1] == "-a":
        t = add(int(i[2]))
        msg.reply(t)
    else:
        msg.reply("Такого флага не существует!")

#команда info
@app.on_message(filters.command("info", prefixes=".") & filters.me)
def info(_, msg):
    msg.reply("**PRO100USERBOT v1.2.0**\n\nЯзык программирования: **PYTHON v3.9.7**\nБиблиотеки:\n**pyrogram v1.2.11\ntgcrypto v1.2.2\nsqlite3 v2.6.0\nprettytable 2.2.0\npycbrf v1.1.0**\n\nGitHub: https://github.com/PRO100-IVANOFF/PRO100USERBOT.git\nСоздатель: t.me/pro100_ivan_off\n\nЧто бы узнать все команды напишите `.commands`")

#команда commands
@app.on_message(filters.command("commands", prefixes=".") & filters.me)
def commands(_, msg):
    chat_id = msg.chat.id
    app.send_message(chat_id, "Список команд:\n\nРазвлекательные:\n`.hack` - взлом Пентагона\n`.type` - придаёт сообщению эффект печати(любой текст)\n`.shrug` - изменяет сообщение на ¯\_(ツ)_/¯")
    app.send_message(chat_id, "Полезные:\n`.math` - решение примеров(любой пример)\n`.sqrt` - извлечение квадратного корня(принимает число)\n`.test` - проверка программы на работоспособность\n`.msg` - отправляет сообщения в чат, в котором была вызванна команда. Принимает количество сообщений и текст сообщения")
    app.send_message(chat_id, "Для LESYA BOT:\n`.fight` - бой в автоматическом режиме(принимает время в часах)\n`.case` - автоматическое открыьие кейсов(номер кейса, количество кейсов)\n`.cw` - запускает КВ и закупается зоотоварами\n`.bonus` - команда для для получения бонуса\n`.donate` - отправка игровой валюты другим игрокам (количество дней)\n`.city` - команда для построек зданий в городе (тип зданий, номер здания и их количество)")
    app.send_message(chat_id, "Граббер:\n`.db` - [-a, -d] - добавить или удалить id канала, -v - посмотреть все записи")
    app.send_message(chat_id, "Переводчик:\n`.tr` - переводит сообщения на любой язык доступный в **GOOGLE translate**. Принимает язык на который еужно перевести, язык с которого нужно перевести и текст. Указывать надо код языка!\n`.languege`(`.lg`) - выводит сообщение с доступными языками и их кодами")
    app.send_message(chat_id, "Конвертер валют:\n`.con` - перевод одной валюты в другую, может не совпадать с результатами гугл конвертера.\nПринимает: первая валюта, вторая валюта в которую нужно перевести, количество.\n`.cur` - коды и названия валют.")
    app.send_message(chat_id, "Прочее:\n`.info` - краткая информация\n`.commands` - вывести это сообщение")

#команда msg(message)
@app.on_message((filters.command("msg", prefixes=".") | filters.command("message", prefixes="."))& filters.me)
def message(_, msg):
    output = msg.text.split()
    povtor = int(output[1])
    chat_id = msg.chat.id
    text = ms(output[2::])
    msg.delete()
    i = 0
    while i < povtor:
        try:
            app.send_message(chat_id, text)
            sleep(0.3)
            i += 1
        except FloodWait as e:
            sleep(e.x)

#команда tr(translate)
@app.on_message((filters.command("tr", prefixes=".") | filters.command("translate", prefixes=".")) & filters.me)
def translate(_, msg):
    try:
        inp = msg.text.split()
        l1 = inp[1]
        l2 = inp[2]
        text = inp[3::]
        msg.edit(f"{translator(l1,l2,text)}")
    except:
        msg.reply("Прозошла ошибка!")

#команда lg(languege)
@app.on_message((filters.command("lg", prefixes=".") | filters.command("languege", prefixes=".")) & filters.me)
def lang(_, msg):
    msg.reply(f"`{langueges()}`")

#команда con(converter)
@app.on_message((filters.command("con", prefixes=".") | filters.command("converter", prefixes=".")) & filters.me)
def con(_,msg):
    try:
        data = msg.text.split()[1:4]
        result = converter(data)
        msg.delete()
        msg.reply(f"**{data[2]}**{data[0].lower()} ≈ **{result}**{data[1].lower()}")
    except:
        msg.reply("Произошла ошибка!")

#команда cur(currencies)
@app.on_message((filters.command("currencies", prefixes=".") | filters.command("cur", prefixes=".")) & filters.me)
def markups(_, msg):
    msg.reply(f"`{currencies()}`")

app.run()