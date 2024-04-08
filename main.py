#Импорт библиотек
import telebot
import sqlite3
import datetime
from datetime import *
from telebot import types
import os



#Настройки версии
version = '0.2'

#Настройка бота
token=os.environ.get('TOKEN')

bot=telebot.TeleBot(token)

comma =['/start', '/help', '/donate', '/print', '/menu', '/enter', '/settings', '/russian', '/literature', '/history', '/sf', '/geography', '/obj', '/lang', '/physics', '/chemestry', '/biology', '/it', '/technology', '/music', '/art', '/geometry', '/algebra']



#Функции
#Распознование команд
def commander(message):
  if message.text == '/help':
    help(message)
  elif message.text == '/donate':
    donate(message)
  elif message.text == '/print':
    f_print_dz(message)
  elif message.text == '/menu':
    menu(message)
  elif message.text == '/enter':
    f_enter_dz(message)
  elif message.text == '/settings':
    settings(message)
  elif message.text == '/russian' or '/literature' or '/history' or '/sf' or '/geography' or '/obj' or '/lang' or '/physics' or '/chemestry' or '/biology' or '/it' or '/technology' or '/music' or '/art' or '/geometry' or '/algebra':
    sci(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: 43 unknown command    ID: {message.from_user.id}    Text: {message.text}\n")
      bot.send_message(message.from_user.id,"Извините, неверная нажата неверная кнопка, попробуйте ещё раз или свяжитесь с технической поддержкой в настройках - /settings")


#Функция записи
def write(id, text, subject, message):

  def end01():

    bot.register_next_step_handler(message, end_enter_dz)

    cur.close()
    conn.close()

  #global message
  conn = sqlite3.connect('data.db')
  cur = conn.cursor()

  markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  menu_btn2 = types.KeyboardButton('⬅️ В меню')
  add_btn2 = types.KeyboardButton('➕ Записать ещё')
  markup2.add(menu_btn2, add_btn2)


  if message.text in comma:
    commander(message)
  elif subject == 'geometry':
    cur.execute(f"UPDATE data SET geometry = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по геометрии записано", reply_markup=markup2)
    end01()
  elif subject == 'algebra':
    cur.execute(f"UPDATE data SET algebra = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по алгебре записано", reply_markup=markup2)
    end01()
  elif subject == 'art':
    cur.execute(f"UPDATE data SET art = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по ИЗО записано", reply_markup=markup2)
    end01()
  elif subject == 'music':
    cur.execute(f"UPDATE data SET music = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по музыке записано", reply_markup=markup2)
    end01()
  elif subject == 'technology':
    cur.execute(f"UPDATE data SET technology = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по технологии записано", reply_markup=markup2)
    end01()
  elif subject == 'IT':
    cur.execute(f"UPDATE data SET IT = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по информатике записано", reply_markup=markup2)
    end01()
  elif subject == 'algebra':
    cur.execute(f"UPDATE data SET algebra = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по алгебре записано", reply_markup=markup2)
    end01()
  elif subject == 'biology':
    cur.execute(f"UPDATE data SET biology = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по биологии записано", reply_markup=markup2)
    end01()
  elif subject == 'chemestry':
    cur.execute(f"UPDATE data SET chemestry = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по химии записано", reply_markup=markup2)
    end01()
  elif subject == 'physics':
    cur.execute(f"UPDATE data SET physics = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по физике записано", reply_markup=markup2)
    end01()
  elif subject == 'lang':
    cur.execute(f"UPDATE data SET lang = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по иностранному языку записано", reply_markup=markup2)
    end01()
  elif subject == 'obj':
    cur.execute(f"UPDATE data SET obj = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по ОБЖ записано", reply_markup=markup2)
    end01()
  elif subject == 'geography':
    cur.execute(f"UPDATE data SET geography = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по географии записано", reply_markup=markup2)
    end01()
  elif subject == 'sf':
    cur.execute(f"UPDATE data SET sf = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по обществознанию записано", reply_markup=markup2)
    end01()
  elif subject == 'history':
    cur.execute(f"UPDATE data SET history = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по истории записано", reply_markup=markup2)
    end01()
  elif subject == 'literature':
    cur.execute(f"UPDATE data SET literature = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по литературе записано", reply_markup=markup2)
    end01()
  elif subject == 'russian':
    cur.execute(f"UPDATE data SET russian = '{text}' WHERE id = '{id}'")
    conn.commit()
    bot.send_message(id,"✅ Дз по русскому языку записано", reply_markup=markup2)
    end01()
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown subject key    ID: {id}    Subject:{subject}    Text: {text}\n")
      bot.send_message(id,"😢 Произошла техническая ошибка, попробуйте попробовать еще раз или напишите в поддержку в настройках", reply_markup=markup2)


#Функция чтения
def read(id, subject):
  global dz_text
  conn = sqlite3.connect('data.db')
  cur = conn.cursor()

  cur.execute(f'SELECT ({subject}) FROM data WHERE id = ({id})')
  dz_text0 = cur.fetchall()
  dz_text = dz_text0[0]

  cur.close()
  conn.close()


#Регистрация
@bot.message_handler(commands=['start'])
def start_message(message):

  #Приветственное сообщение
  bot.send_message(message.chat.id,"Привет ✌️, этот бот поможет записывать дз в телеграм! Помощь - /help")
  id = message.from_user.id

  #Подключение к бд
  conn = sqlite3.connect('data.db')
  cur = conn.cursor()

  #Достаём список пользователей из бд
  cur.execute('SELECT (id) from data')
  ids = cur.fetchall()

  #Проверяем зарегестрован ли пользователь, если нет, то регистрируем
  for i in range (0, len(ids)):
    current = ids[i]
    if current[0] == id:
      find = True
      break
    else:
      find = False
  if find == False:
    cur.execute('INSERT INTO data (id) VALUES (%s)' % id)

  #Сохраняем операции и закрываем соединение с бд
  conn.commit()
  cur.close()
  conn.close()


  menu(message)


#Вывод дз
@bot.message_handler(commands=['print'])
def f_print_dz(message):

  global dz
  dz = ''

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  algebra_btn = types.KeyboardButton("0️⃣  Алгебра")
  geometry_btn = types.KeyboardButton("📐 Геометрия")
  art_btn = types.KeyboardButton("🖌️ ИЗО")
  music_btn = types.KeyboardButton("🎼 Музыка")
  technology_btn = types.KeyboardButton("🗜️ Технология")
  it_btn = types.KeyboardButton("🖥️ Информатика")
  biology_btn = types.KeyboardButton("🌱 Биология")
  chemestry_btn = types.KeyboardButton("🧪 Химия")
  physics_btn = types.KeyboardButton("💡 Физика")
  lang_btn = types.KeyboardButton("🔤 Иностранный язык")
  obj_btn = types.KeyboardButton("🛟 ОБЖ")
  lit_btn = types.KeyboardButton("📕 Литература")
  ru_btn = types.KeyboardButton("🖊️ Русский")
  sf_btn = types.KeyboardButton("🙍‍♂️ Общестовзнание")
  geography_btn = types.KeyboardButton("🗺️ География")
  history_btn = types.KeyboardButton("⚱️ История")
  end_btn = types.KeyboardButton("🔢 Показать расписание")
  menu_btn = types.KeyboardButton('⬅️ В меню')

  markup.add(algebra_btn, geometry_btn, art_btn, music_btn, technology_btn, it_btn, biology_btn, chemestry_btn, physics_btn, lang_btn, obj_btn,lit_btn,ru_btn,sf_btn,history_btn,geography_btn, end_btn, menu_btn)
  bot.send_message(message.from_user.id, f'Выберите предмет:', reply_markup=markup)
  bot.register_next_step_handler(message,print_dz)

def print_dz(message):

  global dz_text, dz

  stop12 = 'False'

  if message.text in comma:
    stop12 = 'command'
  elif message.text == '0️⃣  Алгебра':
    read(message.from_user.id, 'algebra')
    dz = dz + '0️⃣  Алгебра: ' + dz_text[0] +'\n'

  elif message.text == '📐 Геометрия':
    read(message.from_user.id, 'geometry')
    dz = dz + '📐 Геометрия: ' + dz_text[0] +'\n'

  elif message.text == '🖌️ ИЗО':
    read(message.from_user.id, 'art')
    dz = dz + '🖌️ ИЗО: ' + dz_text[0] +'\n'

  elif message.text == '🎼 Музыка':
    read(message.from_user.id, 'music')
    dz = dz + '🎼 Музыка: ' + dz_text[0] +'\n'

  elif message.text == '🗜️ Технология':
    read(message.from_user.id, 'technology')
    dz = dz + '🗜️ Технология: ' + dz_text[0] +'\n'

  elif message.text == '🖥️ Информатика':
    read(message.from_user.id, 'IT')
    dz = dz + '🖥️ Информатика: ' + dz_text[0] +'\n'

  elif message.text == '🌱 Биология':
    read(message.from_user.id, 'biology')
    dz = dz + '🌱 Биология: ' + dz_text[0] +'\n'

  elif message.text == '🧪 Химия':
    read(message.from_user.id, 'chemestry')
    dz = dz + '🧪 Химия: ' + dz_text[0] +'\n'

  elif message.text == '💡 Физика':
    read(message.from_user.id, 'physics')
    dz = dz + '💡 Физика: ' + dz_text[0] +'\n'

  elif message.text == '🔤 Иностранный язык':
    read(message.from_user.id, 'lang')
    dz = dz + '🔤 Иностранный язык: ' + dz_text[0] +'\n'

  elif message.text == '🛟 ОБЖ':
    read(message.from_user.id, 'obj')
    dz = dz + '🛟 ОБЖ: ' + dz_text[0] +'\n'

  elif message.text == '📕 Литература':
    read(message.from_user.id, 'literature')
    dz = dz + '📕 Литература: ' + dz_text[0] +'\n'

  elif message.text == '🖊️ Русский':
    read(message.from_user.id, 'russian')
    dz = dz + '🖊️ Русский: ' + dz_text[0] +'\n'

  elif message.text == '🙍‍♂️ Общестовзнание':
    read(message.from_user.id, 'sf')
    dz = dz + '🙍‍♂️ Общестовзнание: ' + dz_text[0] +'\n'

  elif message.text == '🗺️ География':
    read(message.from_user.id, 'geography')
    dz = dz + '🗺️ География: ' + dz_text[0] +'\n'

  elif message.text == '⚱️ История':
    read(message.from_user.id, 'history')
    dz = dz + '⚱️ История: ' + dz_text[0] +'\n'

  elif message.text == '🔢 Показать расписание':
    stop12 = 'True'
    
  elif message.text == '⬅️ В меню':
    stop12 = 'menu'
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")
      bot.send_message(message.from_user.id,"Извините, неверная нажата неверная кнопка, попробуйте ещё раз или свяжитесь с технической поддержкой в настройках - /settings")

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  algebra_btn = types.KeyboardButton("0️⃣  Алгебра")
  geometry_btn = types.KeyboardButton("📐 Геометрия")
  art_btn = types.KeyboardButton("🖌️ ИЗО")
  music_btn = types.KeyboardButton("🎼 Музыка")
  technology_btn = types.KeyboardButton("🗜️ Технология")
  it_btn = types.KeyboardButton("🖥️ Информатика")
  biology_btn = types.KeyboardButton("🌱 Биология")
  chemestry_btn = types.KeyboardButton("🧪 Химия")
  physics_btn = types.KeyboardButton("💡 Физика")
  lang_btn = types.KeyboardButton("🔤 Иностранный язык")
  obj_btn = types.KeyboardButton("🛟 ОБЖ")
  lit_btn = types.KeyboardButton("📕 Литература")
  ru_btn = types.KeyboardButton("🖊️ Русский")
  sf_btn = types.KeyboardButton("🙍‍♂️ Общестовзнание")
  geography_btn = types.KeyboardButton("🗺️ География")
  history_btn = types.KeyboardButton("⚱️ История")
  end_btn = types.KeyboardButton("🔢 Показать расписание")
  menu_btn = types.KeyboardButton('⬅️ В меню')

  if stop12 == 'False':
    markup.add(algebra_btn, geometry_btn, art_btn, music_btn, technology_btn, it_btn, biology_btn, chemestry_btn, physics_btn, lang_btn, obj_btn,lit_btn,ru_btn,sf_btn,history_btn,geography_btn, end_btn, menu_btn)
    bot.send_message(message.from_user.id, f'Введите предмет:', reply_markup=markup)
    bot.register_next_step_handler(message,print_dz)

  elif stop12 == 'True':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = types.KeyboardButton('⬅️ В меню')
    markup.add(menu_btn)
    bot.send_message(message.from_user.id, text=dz, reply_markup=markup)
    dz = ''
    bot.register_next_step_handler(message,print_dz)

  elif stop12 == 'menu':
    menu(message)

  elif stop12 == 'command':
    commander(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown stop12 value    ID: {message.from_user.id}    Text: {message.text}\n")
      bot.send_message(message.from_user.id,"Извините, возникла внутренняя ошибка, попробуйте ещё раз или свяжитесь с технической поддержкой в настройках - /settings")


#Menu
@bot.message_handler(commands=['menu'])
def menu(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  add_btn = types.KeyboardButton('➕ Записать д/з')
  print_btn = types.KeyboardButton('🔢 Показать дз')
  #settings_btn = types.KeyboardButton('⚙️ Настройки')
  markup.add(add_btn, print_btn)#, settings_btn)
  bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
  bot.register_next_step_handler(message, register_menu)

def register_menu(message):
  if message.text in comma:
    commander(message)
  elif message.text == '➕ Записать д/з':
    f_enter_dz(message)
  elif message.text == '🔢 Показать дз':
    f_print_dz(message)
  elif message.text == '⚙️ Настройки':
    #bot.answer_callback_query(callback_query_id=message.from_user.id, text="⚙️ В разработке ⚙️", show_alert=True)
    bot.register_next_step_handler(message, menu)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")


#Ввод дз
@bot.message_handler(commands=['enter'])
def f_enter_dz(message):

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  algebra_btn = types.KeyboardButton("0️⃣  Алгебра")
  geometry_btn = types.KeyboardButton("📐 Геометрия")
  art_btn = types.KeyboardButton("🖌️ ИЗО")
  music_btn = types.KeyboardButton("🎼 Музыка")
  technology_btn = types.KeyboardButton("🗜️ Технология")
  it_btn = types.KeyboardButton("🖥️ Информатика")
  biology_btn = types.KeyboardButton("🌱 Биология")
  chemestry_btn = types.KeyboardButton("🧪 Химия")
  physics_btn = types.KeyboardButton("💡 Физика")
  lang_btn = types.KeyboardButton("🔤 Иностранный язык")
  obj_btn = types.KeyboardButton("🛟 ОБЖ")
  lit_btn = types.KeyboardButton("📕 Литература")
  ru_btn = types.KeyboardButton("🖊️ Русский")
  sf_btn = types.KeyboardButton("🙍‍♂️ Общестовзнание")
  geography_btn = types.KeyboardButton("🗺️ География")
  history_btn = types.KeyboardButton("⚱️ История")
  menu_btn = types.KeyboardButton('⬅️ В меню')

  markup.add(algebra_btn, geometry_btn, art_btn, music_btn, technology_btn, it_btn, biology_btn, chemestry_btn, physics_btn, lang_btn, obj_btn,lit_btn,ru_btn,sf_btn,history_btn,geography_btn, menu_btn)
  bot.send_message(message.from_user.id, f'Выберите предмет:', reply_markup=markup)
  bot.register_next_step_handler(message, enter_dz)

def enter_dz(message):
  global subgect
  stop01 = 'False'

  if message.text in comma:
    stop01 = 'command'

  elif message.text == '0️⃣  Алгебра':
    subgect = 'algebra'

  elif message.text == '📐 Геометрия':
    subgect = 'geometry'

  elif message.text == '🖌️ ИЗО':
    subgect = 'art'

  elif message.text == '🎼 Музыка':
    subgect = 'music'

  elif message.text == '🗜️ Технология':
    subgect = 'technology'

  elif message.text == '🖥️ Информатика':
    subgect = 'IT'

  elif message.text == '🌱 Биология':
    subgect = 'biology'

  elif message.text == '🧪 Химия':
    subgect = 'chemestry'

  elif message.text == '💡 Физика':
    subgect = 'physics'

  elif message.text == '🔤 Иностранный язык':
    subgect = 'lang'

  elif message.text == '🛟 ОБЖ':
    subgect = 'obj'

  elif message.text == '📕 Литература':
    subgect = 'literature'

  elif message.text == '🖊️ Русский':
    subgect = 'russian'

  elif message.text == '🙍‍♂️ Общестовзнание':
    subgect = 'sf'

  elif message.text == '🗺️ География':
    subgect = 'geography'

  elif message.text == '⚱️ История':
    subgect = 'history'
    
  elif message.text == '⬅️ В меню':
    stop01 = 'True'

  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")

  if stop01 == 'False':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = types.KeyboardButton('⬅️ В меню')
    markup.add(menu_btn)
    bot.send_message(message.from_user.id, f'Введите дз по предмету {message.text} :', reply_markup=markup)
    bot.register_next_step_handler(message, reg_enter_dz)
  elif stop01 == 'command':
    commander(message)
  else:
    menu(message)

def reg_enter_dz(message):
  global subgect

  if message.text in comma:
    commander(message)
  elif message.text == '⬅️ В меню':
    menu(message)
  else:
    write(message.from_user.id, message.text, subgect, message)

def end_enter_dz(message):
  if message.text in comma:
    commander(message)
  elif message.text == '⬅️ В меню':
    menu(message)
  elif message.text == '➕ Записать ещё':
    f_enter_dz(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")


#Помощь
@bot.message_handler(commands=['help'])
def help(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  menu_btn = types.KeyboardButton('⬅️ В меню')
  markup.add(menu_btn)
  bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Этот бот поможет тебе вести школьный дневник прямо в телеграм, для того, чтобы перейти в основное меню используй /menu, также для быстрого доступа к записи и выводу дз можно исользовать команды /enter и /print. Проект полностью бесплатный и без рекламы, поэтому раззработчик будет очень рад донатикам, реквизиты можно глянуть здесь - /donate. На этом вроде всё, если понадобиться помощь, то обращайся - /help\n\nРазработчик: @ilian_meta\nВерсия: {version}', reply_markup=markup)
  bot.register_next_step_handler(message, reg_help)

def reg_help(message):
  if message.text in comma:
    commander(message)
  elif message.text == '⬅️ В меню':
    menu(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")


#Настройки
@bot.message_handler(commands=['settings'])
def settings(message):
  bot.send_message(message.from_user.id, 'Настройки пока что не готовы, но скоро будут, поддержка - @giant47', reply_markup=markup)
  menu(message)


#Донаты
@bot.message_handler(commands=['donate'])
def donate(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  menu_btn = types.KeyboardButton('⬅️ В меню')
  markup.add(menu_btn)
  bot.send_message(message.from_user.id, 'Задонатить на хостинг или печеньки разработчику можно тут, пожалуйста в комментариях к переводу указывайте что это донат и на что он)))\nTinkoff: 2200700771729976\nAlfa-bank: 2200150959802023\nQiWi: https://qiwi.com/n/ILIAN445\nTON: EQDOi-f39PBbaD_1kO6zNZVacjVPwrk_JZnphuzIw_hq-Voy\nBTC: 1M1E4AAcKsipvj9w8fndMnfvHHQ8cKG7d1\n', reply_markup=markup)
  bot.register_next_step_handler(message, reg_donate)

def reg_donate(message):
  if message.text in comma:
    commander(message)
  elif message.text == '⬅️ В меню':
    menu(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")


#Карточки предметов
@bot.message_handler(commands=['russian', 'literature', 'history', 'sf', 'geography', 'obj', 'lang', 'physics', 'chemestry', 'biology', 'it', 'technology', 'music', 'art', 'geometry', 'algebra'])
def sci(message):
  global dz_text

  #Разбираемся с предметом
  s = message.text[1:]

  #Если он хочет посмотреть дз
  if s == 'russian' or s == 'literature' or s == 'history' or s == 'sf' or s == 'geography' or s == 'obj' or s == 'lang' or s == 'physics' or s == 'chemestry' or s == 'biology' or s == 'it' or s == 'technology' or s == 'music' or s == 'art' or s == 'geometry' or s == 'algebra':

    subject01 = s
    #Читаем бд
    read(message.from_user.id, subject01)
    dz_text = dz_text[0]

    #Кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = types.KeyboardButton('⬅️ В меню')
    add_btn = types.KeyboardButton('➕ Записать дз')
    markup.add(menu_btn, add_btn)

    #Отправка сообщения и переход на регистратор
    bot.send_message(message.from_user.id, f'Дз по предмету : {dz_text}', reply_markup=markup)
    bot.register_next_step_handler(message, reg_sci)
  else:
    #Возимся с перменными
    hw = (s[s.find(" "):])
    subject01 = s.replace(hw,"")
    hw = hw[1:]

    #Пишем в бд
    write(message.from_user.id, hw, subject01, message)
      

def reg_sci(message):
  if message.text in comma:
    commander(message)
  elif message.text == '⬅️ В меню':
    menu(message)
  elif message.text == '➕ Записать дз':
    f_enter_dz(message)
  else:
    with open("logs.txt", "a") as file:
      time = datetime.now()
      file.write(f"{time}   Error: unknown button key    ID: {message.from_user.id}    Text: {message.text}\n")



#Main polling
bot.infinity_polling()