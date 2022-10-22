import telebot
from telebot import types
from datetime import datetime
import random
from random import randint

from time import sleep

import sqlite3

db = sqlite3.connect('base.db', check_same_thread=False)
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
    id INT,
    username TEXT,
    mess2del INT,
    correct_literas TEXT,
    viselica TEXT,
    alphabet TEXT,
    user_words TEXT,
    mistakes INT,
    mess2del2 INT
)''')

db.commit()

bot = telebot.TeleBot('5694376315:AAEo0IkUJfKpBBhIbTr2zsWZvR94EzUlYds')

who_i_am = '''\
🫰Привет, друг, я *UnicChan*\!
Я \- программист с *3\-х летним* стажем\.

👾Знаю такие языки программирования, как *Python, C\+\+\.*
В своих работах могу использовать\: `базу данных SQL`*,* `парсинг сайтов`*,* `API сторонних сервисов`*\.*

🧐Знаю основы *ООП* и могу разобраться в чужом коде\.

||🙃Примеры того, что я могу сделать, можешь посмотреть далее||
'''

words = ['панама', 'игруля', 'обводка', 'телефон', 'ноутбук', 'супербот', 'лолзтим']

alphabet_liters = ['none', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

max_mistakes = 10

winner_photo = 'AgACAgIAAxkBAAO2Y1KzZNwoV8ttDq9mwPjl6vaQkH4AAmm_MRvhDplKCpp4qy-svAgBAAMCAAN5AAMqBA'

viselica_photos = ['AgACAgIAAxkBAAN8Y1JorzZoK4Y1SpxqlZCSTqjowPUAAt2_MRvhDpFKgpn9DXF9ljgBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAN9Y1Jos8ebaj5hu_PQSnvz3iuW5QcAAt6_MRvhDpFK_hnnW_z6SYsBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAN-Y1JouLnAQ6kio-t0hLFGKo_2brIAAt-_MRvhDpFKsGbS0Lv_bGsBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAN_Y1JovLzLJ33-9vfLApEQnps6t68AAuC_MRvhDpFKy5noCY-pl9wBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOAY1Jov4yee42Sllr_w5J-3-MQ_kYAAuG_MRvhDpFKsN0voJCoNZoBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOBY1JoxFqqO4xsssefxYk0sU2YQoQAAuK_MRvhDpFKG1D32YMhCbQBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOCY1JoyMqqL6g6LRD4oH8W5kcxgbYAAuO_MRvhDpFKfvzOwSjeWqkBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAODY1Joy8gWVcuvdzUU5HaKiAOv5BIAAuS_MRvhDpFK4CRxT5oa3mYBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOEY1JozkiHKKwYiJRFscqtz1qX9wcAAuW_MRvhDpFKOqhdHRsIGZYBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOFY1Jo0IQcIL_-8HHQy4Impsy6fBwAAua_MRvhDpFKrhGszYWySGYBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAOGY1Jo1HL-vvRwtOz3WP5HMYO2SwgAAue_MRvhDpFKlwlNI3x_1QIBAAMCAAN4AAMqBA']

photos = ['AgACAgIAAxkBAAPWY1K7KeAven_e6dxGh66L6hVnygQAAt3AMRsT_ZlKuyN1YBIB2LYBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAPbY1K7Q12wm9itsh1F1lvx8hPTVrMAAuLAMRsT_ZlKrwSMgxcrGbYBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAPZY1K7OMzKBIb8fE9I9nOYvgSanfUAAuDAMRsT_ZlKt7DILj9MqgQBAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAPYY1K7NFU1cqkQDQUCDu1Pfe4Yi30AAt_AMRsT_ZlKk01K-x1-lxkBAAMCAAN5AAMqBA',
'AgACAgIAAxkBAAPXY1K7LvKcV-2sTdkoQTt2kPqZcJcAAt7AMRsT_ZlKZiYCgnUwP8ABAAMCAAN4AAMqBA',
'AgACAgIAAxkBAAPaY1K7PniGAmENr77bOP2eInhUGHgAAuHAMRsT_ZlKNMYLvDYE3pQBAAMCAAN4AAMqBA']

descriptions = ['👾*Андрей.*\nПросто лучший. `10` из `10`.',
'👾*Олежа.*\nДобряк по характеру, `8` из `10`.',
'👾*Пётр.*\nНе самый умный, зато самый красивый. `6` из `10`. ',
'👾*Николай.*\nНелюдимый, но ответственный. `5` из `10`.',
'👾*Женя.*\nДумает, что он велосипед. `7` из `10`.',
'👾*Никодим.*\nПопал сюда по дружбе. `1` из `1`.']

def print_time_now():
    time = datetime.now()
    time = time.strftime('%m-%d %H:%M:%S')
    print(f'--{time}--')

def correct_username(message):
    username = ''
    if message.from_user.username == None:
        username += message.from_user.first_name
        if message.from_user.last_name != None:
            username += ' ' + message.from_user.last_name
    else:
        username = '@' + message.from_user.username
    return username

def make_user(message):
    sql.execute(f'SELECT id FROM users WHERE id = {message.from_user.id}')
    if sql.fetchone() is None: #если впервые запускает
        sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, correct_username(message), None, '', '', '', '', 0, None))
        db.commit()

        print(f'{correct_username(message)}({message.chat.id}) впервые запустил бота!')
    db.commit()

while True:
    try:
        @bot.message_handler(content_types=["photo"])
        def confirming(message):
            if message.content_type == 'photo':
                photo = max(message.photo, key=lambda x: x.height)
                print(photo.file_id)

        @bot.message_handler(commands=['start'])
        def start(message):
            bot.delete_message(message.chat.id, message.message_id)
            if message.chat.type == 'private':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                menu = types.KeyboardButton('🧐Покажи, что можешь!')

                markup.add(menu)
                bot.send_message(message.chat.id, who_i_am, parse_mode='MarkdownV2', reply_markup=markup)

                make_user(message)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Переходи в личные сообщения со мной 😉')

        @bot.message_handler(content_types=['text'])
        def bot_message(message):
            if message.chat.type == 'private':
                bot.delete_message(message.chat.id, message.message_id)
                if 'Покажи' in message.text: 
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    galery = types.KeyboardButton('🩻\nГалерея')
                    viselica = types.KeyboardButton('🎮\nИгра "Виселица"')
                    me = types.KeyboardButton('⌨️\nНаписать мне')

                    markup.add(galery, viselica, me)
                    bot.send_message(message.chat.id, '🩻*Галерея* \- галерея ботов\.\n\n🎮*Игра "Виселица"* \- отгадай слово, которое я тебе загадаю\! За каждую неверно предположенную букву ты становишься всё ближе к проигрышу\.\n\n⌨️*Написать мне* \- связь со мной\.', parse_mode='MarkdownV2', reply_markup=markup)
                
                elif 'Виселица' in message.text:
                    try:
                        sql.execute(f'SELECT mess2del, mess2del2 FROM users WHERE id = {message.from_user.id}')
                        this = sql.fetchone()
                        mess2del = this[0]
                        mess2del2 = this[1]
                        db.commit()
                        bot.delete_message(message.chat.id, mess2del)
                        bot.delete_message(message.chat.id, mess2del2)
                        sql.execute(f'UPDATE users SET mess2del = ?, mess2del2 = ? WHERE id = {message.from_user.id}', (None, None))
                        db.commit()
                    except:
                        pass

                    sql.execute(f'UPDATE users SET correct_literas = ?, viselica = ?, alphabet = ?, mistakes = ? WHERE id = {message.from_user.id}', ('', words[random.randint(0, len(words)-1)], '', 0))
                    db.commit()

                    sql.execute(f'SELECT * FROM users WHERE id = {message.from_user.id}')
                    user = sql.fetchall()[0]
                    db.commit()

                    photo = viselica_photos[0]

                    markup = types.InlineKeyboardMarkup(row_width=8)
                    a = types.InlineKeyboardButton('А', callback_data='1')
                    b = types.InlineKeyboardButton('Б', callback_data='2')
                    v = types.InlineKeyboardButton('В', callback_data='3')
                    g = types.InlineKeyboardButton('Г', callback_data='4')
                    d = types.InlineKeyboardButton('Д', callback_data='5')
                    e = types.InlineKeyboardButton('Е', callback_data='6')
                    ee = types.InlineKeyboardButton('Ё', callback_data='7')
                    gh = types.InlineKeyboardButton('Ж', callback_data='8')
                    z = types.InlineKeyboardButton('З', callback_data='9')
                    i = types.InlineKeyboardButton('И', callback_data='10')
                    ii = types.InlineKeyboardButton('Й', callback_data='11')
                    k = types.InlineKeyboardButton('К', callback_data='12')
                    l = types.InlineKeyboardButton('Л', callback_data='13')
                    m = types.InlineKeyboardButton('М', callback_data='14')
                    n = types.InlineKeyboardButton('Н', callback_data='15')
                    o = types.InlineKeyboardButton('О', callback_data='16')
                    p = types.InlineKeyboardButton('П', callback_data='17')
                    r = types.InlineKeyboardButton('Р', callback_data='18')
                    s = types.InlineKeyboardButton('С', callback_data='19')
                    t = types.InlineKeyboardButton('Т', callback_data='20')
                    y = types.InlineKeyboardButton('У', callback_data='21')
                    f = types.InlineKeyboardButton('Ф', callback_data='22')
                    h = types.InlineKeyboardButton('Х', callback_data='23')
                    c = types.InlineKeyboardButton('Ц', callback_data='24')
                    hh = types.InlineKeyboardButton('Ч', callback_data='25')
                    sh = types.InlineKeyboardButton('Ш', callback_data='26')
                    shsh = types.InlineKeyboardButton('Щ', callback_data='27')
                    tv = types.InlineKeyboardButton('Ъ', callback_data='28')
                    iii = types.InlineKeyboardButton('Ы', callback_data='29')
                    mg = types.InlineKeyboardButton('Ь', callback_data='30')
                    eee = types.InlineKeyboardButton('Э', callback_data='31')
                    yy = types.InlineKeyboardButton('Ю', callback_data='32')
                    aa = types.InlineKeyboardButton('Я', callback_data='33')

                    markup.add(a,b,v,g,d,e,ee,gh,z,i,ii,k,l,m,n,o,p,r,s,t,y,f,h,c,hh,sh,shsh,tv,iii,mg,eee,yy,aa)
                    mess2del2 = bot.send_message(message.chat.id, '🎮Выбирай буквы и попытайся отгадать слово!')
                    mess2del = bot.send_photo(message.chat.id, photo, '🪫Слово:  ' + '||\_|| '* len(user[4]), parse_mode='MarkdownV2', reply_markup=markup)

                    sql.execute(f'UPDATE users SET mess2del = ?, mess2del2 = ? WHERE id = {message.from_user.id}', (mess2del.message_id, mess2del2.message_id))
                    db.commit()

                elif 'Написать мне' in message.text:
                    markup = types.InlineKeyboardMarkup()
                    link = types.InlineKeyboardButton('@UnicChan', url='https://t.me/UnicChan')

                    markup.add(link)
                    bot.send_message(message.chat.id, '⌨️', reply_markup=markup)

                elif 'Галерея' in message.text:
                    try:
                        sql.execute(f'SELECT mess2del, mess2del2 FROM users WHERE id = {message.from_user.id}')
                        this = sql.fetchone()
                        mess2del = this[0]
                        mess2del2 = this[1]
                        db.commit()
                        bot.delete_message(message.chat.id, mess2del)
                        bot.delete_message(message.chat.id, mess2del2)
                        sql.execute(f'UPDATE users SET mess2del = ?, mess2del2 = ? WHERE id = {message.from_user.id}', (None, None))
                        db.commit()
                    except:
                        pass

                    photo = photos[0]
                    description = descriptions[0]
                    all_photos = len(photos) - 1

                    markup = types.InlineKeyboardMarkup(row_width=3)
                    back = types.InlineKeyboardButton('⬅️', callback_data=f'forward{all_photos}')
                    close = types.InlineKeyboardButton('❌', callback_data='del')
                    forward = types.InlineKeyboardButton('➡️', callback_data='forward1')

                    markup.add(back, close, forward)
                    mess2del2 = bot.send_message(message.chat.id, '👾Посмотри, какие крутые боты!')
                    mess2del = bot.send_photo(message.chat.id, photo, caption=f'{description}', parse_mode='Markdown', reply_markup=markup)

                    sql.execute(f'UPDATE users SET mess2del = ?, mess2del2 = ? WHERE id = {message.from_user.id}', (mess2del.message_id, mess2del2.message_id))
                    db.commit()

                # else:
                #     sql.execute(f'UPDATE photos SET description = {message.text} WHERE photo = ""')
                #     db.commit()

            else:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Переходи в личные сообщения со мной 😉')

        @bot.callback_query_handler(func=lambda call: True) #обработка inline кнопок
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == 'что-то':
                        pass

                    elif call.data == 'del':
                        sql.execute(f'SELECT mess2del, mess2del2 FROM users WHERE id = {call.from_user.id}')
                        this = sql.fetchone()
                        mess2del = this[0]
                        mess2del2 = this[1]
                        db.commit()
                        bot.delete_message(call.message.chat.id, mess2del)
                        bot.delete_message(call.message.chat.id, mess2del2)

                    elif call.data == 'already_used':
                        bot.answer_callback_query(call.id, '✖️')

                    for num in range(0, 34):
                        if call.data == f'{num}':
                            try:
                                sql.execute(f'SELECT alphabet, viselica, mistakes, correct_literas, mess2del FROM users WHERE id = {call.from_user.id}')
                                this = sql.fetchone()
                                db.commit()
                                alphabet = this[0]
                                viselica = this[1]
                                mistakes = this[2]
                                correct_literas = this[3]
                                mess2del = this[4]
                                litera = alphabet_liters[num]
                                continue_game = True

                                alphabet = alphabet + litera

                                if litera in viselica:
                                    correct_literas = correct_literas + litera
                                    sql.execute(f'UPDATE users SET correct_literas = ?, alphabet = ? WHERE id = {call.from_user.id}', (correct_literas, alphabet))
                                    db.commit()
                                    bot.answer_callback_query(call.id, '✅')
                                else:
                                    mistakes += 1
                                    sql.execute(f'UPDATE users SET mistakes = ?, alphabet = ? WHERE id = {call.from_user.id}', (mistakes, alphabet))
                                    db.commit()
                                    bot.answer_callback_query(call.id, '🅾️')

                                    if mistakes >= max_mistakes:
                                        continue_game = False
                                
                                if continue_game:
                                    word = ''
                                    for lit in viselica:
                                        if lit in correct_literas:
                                            word += lit + ' '
                                        else:
                                            word += '||\_|| '
                                    if '_' in word:
                                        photo = viselica_photos[mistakes]

                                        markup = types.InlineKeyboardMarkup(row_width=8)
                                        if 'а' in alphabet:
                                            a = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            a = types.InlineKeyboardButton('А', callback_data='1')
                                        if 'б' in alphabet:
                                            b = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            b = types.InlineKeyboardButton('Б', callback_data='2')
                                        if 'в' in alphabet:
                                            v = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            v = types.InlineKeyboardButton('В', callback_data='3')
                                        if 'г' in alphabet:
                                            g = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            g = types.InlineKeyboardButton('Г', callback_data='4')
                                        if 'д' in alphabet:
                                            d = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            d = types.InlineKeyboardButton('Д', callback_data='5')
                                        if 'е' in alphabet:
                                            e = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            e = types.InlineKeyboardButton('Е', callback_data='6')
                                        if 'ё' in alphabet:
                                            ee = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            ee = types.InlineKeyboardButton('Ё', callback_data='7')
                                        if 'ж' in alphabet:
                                            gh = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            gh = types.InlineKeyboardButton('Ж', callback_data='8')
                                        if 'з' in alphabet:
                                            z = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            z = types.InlineKeyboardButton('З', callback_data='9')
                                        if 'и' in alphabet:
                                            i = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            i = types.InlineKeyboardButton('И', callback_data='10')
                                        if 'й' in alphabet:
                                            ii = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            ii = types.InlineKeyboardButton('Й', callback_data='11')
                                        if 'к' in alphabet:
                                            k = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            k = types.InlineKeyboardButton('К', callback_data='12')
                                        if 'л' in alphabet:
                                            l = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            l = types.InlineKeyboardButton('Л', callback_data='13')
                                        if 'м' in alphabet:
                                            m = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            m = types.InlineKeyboardButton('М', callback_data='14')
                                        if 'н' in alphabet:
                                            n = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            n = types.InlineKeyboardButton('Н', callback_data='15')
                                        if 'о' in alphabet:
                                            o = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            o = types.InlineKeyboardButton('О', callback_data='16')
                                        if 'п' in alphabet:
                                            p = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            p = types.InlineKeyboardButton('П', callback_data='17')
                                        if 'р' in alphabet:
                                            r = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            r = types.InlineKeyboardButton('Р', callback_data='18')
                                        if 'с' in alphabet:
                                            s = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            s = types.InlineKeyboardButton('С', callback_data='19')
                                        if 'т' in alphabet:
                                            t = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            t = types.InlineKeyboardButton('Т', callback_data='20')
                                        if 'у' in alphabet:
                                            y = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            y = types.InlineKeyboardButton('У', callback_data='21')
                                        if 'ф' in alphabet:
                                            f = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            f = types.InlineKeyboardButton('Ф', callback_data='22')
                                        if 'х' in alphabet:
                                            h = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            h = types.InlineKeyboardButton('Х', callback_data='23')
                                        if 'ц' in alphabet:
                                            c = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            c = types.InlineKeyboardButton('Ц', callback_data='24')
                                        if 'ч' in alphabet:
                                            hh = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            hh = types.InlineKeyboardButton('Ч', callback_data='25')
                                        if 'ш' in alphabet:
                                            sh = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            sh = types.InlineKeyboardButton('Ш', callback_data='26')
                                        if 'щ' in alphabet:
                                            shsh = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            shsh = types.InlineKeyboardButton('Щ', callback_data='27')
                                        if 'ъ' in alphabet:
                                            tv = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            tv = types.InlineKeyboardButton('Ъ', callback_data='28')
                                        if 'ы' in alphabet:
                                            iii = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            iii = types.InlineKeyboardButton('Ы', callback_data='29')
                                        if 'ь' in alphabet:
                                            mg = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            mg = types.InlineKeyboardButton('Ь', callback_data='30')
                                        if 'э' in alphabet:
                                            eee = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            eee = types.InlineKeyboardButton('Э', callback_data='31')
                                        if 'ю' in alphabet:
                                            yy = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            yy = types.InlineKeyboardButton('Ю', callback_data='32')
                                        if 'я' in alphabet:
                                            aa = types.InlineKeyboardButton('✖️', callback_data='already_used')
                                        else:
                                            aa = types.InlineKeyboardButton('Я', callback_data='33')

                                        markup.add(a,b,v,g,d,e,ee,gh,z,i,ii,k,l,m,n,o,p,r,s,t,y,f,h,c,hh,sh,shsh,tv,iii,mg,eee,yy,aa)
                                        bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, mess2del)
                                        bot.edit_message_caption(f'🪫Слово: *{word}*', call.message.chat.id, mess2del, parse_mode='MarkdownV2', reply_markup=markup)

                                    else:
                                        try:
                                            sql.execute(f'SELECT mess2del, mess2del2 FROM users WHERE id = {call.from_user.id}')
                                            this = sql.fetchone()
                                            db.commit()
                                            mess2del = this[0]
                                            mess2del2 = this[1]
                                            bot.delete_message(call.message.chat.id, mess2del)
                                            bot.delete_message(call.message.chat.id, mess2del2)
                                        except:
                                            pass

                                        bot.send_photo(call.message.chat.id, winner_photo, f'🔋Слово: *{viselica}*\n\n🥳Поздравляю, ты отгадал слово!\nПромокод *10%* на первый заказ: `LIKE`', parse_mode='Markdown')
                                else:
                                    photo = viselica_photos[10]
                                    bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, mess2del)
                                    bot.edit_message_caption(f'🪫Слово: ||{viselica}||\n\n🥲Ты проиграл\. Попробуй ещё раз\!', call.message.chat.id, mess2del, parse_mode='MarkdownV2')
                            except:
                                bot.answer_callback_query(call.id, '🤯Не так быстро, пожалуйста', show_alert=True)

                        elif call.data == f'forward{num}':
                            bot.answer_callback_query(call.id)
                            all_photos = len(photos) - 1

                            back = num - 1
                            forward = num + 1

                            if num == 0:
                                back = all_photos
                            if num == all_photos:
                                forward = 0

                            photo = photos[num]
                            description = descriptions[num]

                            markup = types.InlineKeyboardMarkup(row_width=3)
                            back = types.InlineKeyboardButton('⬅️', callback_data=f'forward{back}')
                            close = types.InlineKeyboardButton('❌', callback_data='del')
                            forward = types.InlineKeyboardButton('➡️', callback_data=f'forward{forward}')

                            markup.add(back, close, forward)
                            bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, call.message.message_id, reply_markup=markup)
                            bot.edit_message_caption(f'{description}', call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)

            except Exception as e:
                print_time_now()
                print(f'ошибка в обработке inline кнопки!\n{repr(e)}')

        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        print(print_time_now(), 'Ошибка в боте. Рестарт через 1 секунду')
        sleep(1)
