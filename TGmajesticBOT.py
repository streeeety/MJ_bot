import telebot
from telebot import types

bot = telebot.TeleBot('5995857148:AAF4_wUGvJjMuIQjOIjdNFjqKJJUQQ1Abkk')


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('colored_emotions_volk_kun_001.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    mess = f'Привет, <b>{message.from_user.first_name}</b>!✌️\n<i>Я бот, который будет помогать тебе в мире MajesticRP</i>\nНажми 🠖 /go , чтобы увидеть список команд\n\nP.S. Кстати, я был создан при помощи <i>Discord канала <b>Logan Fletcher</b></i>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['go'])
def map(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('/exel')
    btn2 = types.KeyboardButton('/family')
    btn3 = types.KeyboardButton('/map')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Выберите нужный пункт\n/exel - Таблицы\n/family - Семейные контракты\n/map - Карты', reply_markup=markup)


@bot.message_handler(commands=['exel'])
def exel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('🚗 Таблица свалки автомобилей 🚗')
    btn2 = types.KeyboardButton('⚙️ Таблица тюнинга и скорости автомобилей ⚙️')
    btn3 = types.KeyboardButton('💵 Таблица зарплат на всех работах 💵')
    btn4 = types.KeyboardButton('📈 Таблица уровней 📈')
    btn5 = types.KeyboardButton('🔫 Таблица оружия 🔫')
    btn6 = types.KeyboardButton('🍔 Таблица еды и воды 🍔')
    btn7 = types.KeyboardButton('👕 Таблица irl-одежды 👕')
    btn8 = types.KeyboardButton('👮‍♂️ Таблица автоугона 👮‍♂️')
    btn9 = types.KeyboardButton('Вернуться назад')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(message.chat.id, 'Выберете нужный пункт', reply_markup=markup)


@bot.message_handler(commands=['map'])
def map(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🗑️ Карта мусорок 🗑️')
    btn2 = types.KeyboardButton('📱 Карта телефонов 📱')
    btn3 = types.KeyboardButton('🐮 Карта охоты 🐮')
    btn4 = types.KeyboardButton('💎 Карта кладов 💎')
    btn5 = types.KeyboardButton('Вернуться назад')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Выберете нужный пункт', reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['family'])
def family(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🐟 Рыбный день 🐟')
    btn2 = types.KeyboardButton('🎁 Свадебный банкет 🎁')
    btn3 = types.KeyboardButton('👨‍🔧 Кабельщик 👨‍🔧')
    btn4 = types.KeyboardButton('🎙 415-й, я база, ответьте 🎙')
    btn5 = types.KeyboardButton('👷‍♂️ Шахта 👷‍♂️')
    btn6 = types.KeyboardButton('◻️ Краткий гайд ◻️')
    btn7 = types.KeyboardButton('Вернуться назад')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, 'С каким контрактом нужна помощь?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Вернуться назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('/exel')
        btn2 = types.KeyboardButton('/family')
        btn3 = types.KeyboardButton('/map')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите нужный пункт\n/exel - Таблицы\n/family - Семейные контракты\n/map - Карты', reply_markup=markup)
    if message.text == '📱 Карта телефонов 📱':
        ph1 = open('phones.jpg', 'rb')
        bot.send_photo(message.chat.id, ph1)
    if message.text == '🗑️ Карта мусорок 🗑️':
        ph2 = open('trash (2).jpg', 'rb')
        bot.send_photo(message.chat.id, ph2)
    if message.text == '🐮 Карта охоты 🐮':
        ph3 = open('hunt.png', 'rb')
        bot.send_photo(message.chat.id, ph3)
    if message.text == '💎 Карта кладов 💎':
        ph4 = open('klad.jpg', 'rb')
        photoklad = open('priceklad.png', 'rb')
        bot.send_photo(message.chat.id, ph4)
        bot.send_message(message.chat.id, '<b>В подарок лови стоимости кладов\nУдачи в поисках!</b>', parse_mode='html')
        bot.send_photo(message.chat.id, photoklad)
    if message.text == '🚗 Таблица свалки автомобилей 🚗':
        bot.send_message(message.chat.id, '<b>Лови таблицу со свалкой автомобилей!</b>\n https://docs.google.com/spreadsheets/d/1DtKOEIQe2MLZxrzdKf8-YMIkZYQyeDb8pKB8jcz4BoI/edit#gid=0', parse_mode='html')
    if message.text == '⚙️ Таблица тюнинга и скорости автомобилей ⚙️':
        bot.send_message(message.chat.id, '<b>Лови таблицу с тюнингом автомобилей!</b>\n https://docs.google.com/spreadsheets/d/1lR3Ms3Lv4iarFd0zrpRIlZ1ipaa-1pDTtEkwlpnDO_s/edit#gid=0', parse_mode='html')
    if message.text == '💵 Таблица зарплат на всех работах 💵':
        ph5 = open('rabota.png', 'rb')
        bot.send_message(message.chat.id, '<b>Лови таблицу с зарплатами всех работ!</b>\n https://docs.google.com/spreadsheets/d/1N1hSs1lZK-2Eq8k4Jsnz4IFAeOGE8sbqNlodywuaGUc/edit?usp=sharing', parse_mode='html')
        bot.send_message(message.chat.id, 'Вот еще таблица закладок\nНо с этим будь осторожнее')
        bot.send_photo(message.chat.id, ph5)
    if message.text == '📈 Таблица уровней 📈':
        bot.send_message(message.chat.id, '<b>Лови таблицу со всеми уровнями!</b>\n https://docs.google.com/spreadsheets/d/1Mi15U43CeCpq6P_mD_Hhmag11zIEsaVvGE2CG6y9UGA/edit#gid=0', parse_mode='html')
    if message.text == '🔫 Таблица оружия 🔫':
        bot.send_message(message.chat.id, '<b>Я вижу тут...Я вижу тут одного гангстера!</b>\n https://docs.google.com/spreadsheets/d/18Wn_594mNO1wGK3kSokcvN8DPLxDBBfAiJ1FREpGYJM/edit?usp=sharing', parse_mode='html')
    if message.text == '🍔 Таблица еды и воды 🍔':
        ph6 = open('eda.jpg', 'rb')
        bot.send_message(message.chat.id, '<b>Вижу ты хочешь перекусить!\nСпециально для тебя подготовил таблицу со всей едой!</b>', parse_mode='html')
        bot.send_photo(message.chat.id, ph6)
    if message.text == '👕 Таблица irl-одежды 👕':
        bot.send_message(message.chat.id, '<b>Любишь модно одеваться? - Это для тебя!</b>\n https://docs.google.com/spreadsheets/d/1ku--MRGLMZwVqfEIJ4YHNOkMgGGUBDCnVxrB06oo8Z8/edit#gid=0', parse_mode='html')
    if message.text == '👮 Таблица автоугона 👮‍':
        bot.send_message(message.chat.id, '<b>Хм...Вижу ты любишь рисковать\nНу...Дело твое</b>\n https://docs.google.com/spreadsheets/d/16Y_DxNIrj4IhasDaIvPXQkSY80HDTYy_R8ekGE71TYg/edit?usp=sharing', parse_mode='html')
    if message.text == '🐟 Рыбный день 🐟':
        ph7 = open('contr1.png', 'rb')
        bot.send_photo(message.chat.id, ph7)
        bot.send_message(message.chat.id, 'Рыбный день:\nЗадача - сдать 80 кг форели скупщику. Рыбу можно выловить самому с помощью удочки и наживки которые можно купить в магазинах 24/7, либо же приобрести рыбу на вторичном рынке. \nРасходы: Удочка - min цена 175$, max цена 350$. Наживка - min цена 100$, max цена 200$.\nЦена активации: 20.000$\nНаграда: Деньги 140.000$, Репутация +100, Опыт +50.', parse_mode='html')
    if message.text == '🎁 Свадебный банкет 🎁':
        ph8 = open('contr2.png', 'rb')
        bot.send_photo(message.chat.id, ph8)
        bot.send_message(message.chat.id, 'Свадебный банкет:\nЗадача - купить 10 бутылок Вина Rockford Hills Resort, приобрести их можно в любом из баров и сдать их на яхте Дель-Перро-Бич. \nЦена активации: 5.000$ \nРасходы: 15.000$ (На вино) \Награда: Деньги 40.000$, Репутация -50, Опыт +50.', parse_mode='html')
    if message.text == '👨‍🔧 Кабельщик 👨‍🔧':
        ph9 = open('contr3.png', 'rb')
        bot.send_photo(message.chat.id, ph9)
        bot.send_message(message.chat.id, 'Кабельщик:\nЗадача - перевести 150 ящиков с кабелем по 7.5кг каждый. Для выполнения контракта требуется 5 человек. От одного человека принимается максимум 30 ящиков. Лучше всего использовать для перевозки несколько авто, либо же вертолёт. \nЦена активации: 20.000$ \nНаграда: Деньги 140.000$, Репутация +150, Опыт +100.', parse_mode='html')
    if message.text == '🎙 415-й, я база, ответьте 🎙':
        ph10 = open('contr4.png', 'rb')
        bot.send_photo(message.chat.id, ph10)
        bot.send_message(message.chat.id, '415-й, я база, ответьте:\nЗадача - купить 10 раций, купить их можно в магазинах 24/7, после чего сдать их.\nЦена активации: 1.000$ \nРасходы: min цена: 2.000$, max цена: 4.000$ (За рацию) \nНаграда: Деньги 60.000$, Репутация +50, Опыт +50.', parse_mode='html')
    if message.text == '👷‍♂️ Шахта 👷‍♂️':
        ph11 = open('contr5.png', 'rb')
        bot.send_photo(message.chat.id, ph11)
        bot.send_message(message.chat.id, 'Шахта:\nЗадача - привезти руду, бывает несколько вариаций данного контракта: Железная руда (300шт), Серебро (190шт), Медь (100шт), Олово (45шт), Золото (25шт).\nДля выполнения контракта требуется 5 человек. От одного человека принимается максимум: Железная руда (60шт), Серебро (38шт), Медь (20шт), Олово (9шт), Золото (5шт).\nВид изменяется каждый раз полностью рандомно. Золотую руду найти сложнее всего, можно потратить часы на шахте\nЦена активации: 25.000$ \nНаграда (Железо): Деньги 120.000$, Репутация +200, Опыт +150.\nНаграда (Серебро): Деньги 125.000$, Репутация +200, Опыт +150.\nНаграда (Медь): Деньги 140.000$, Репутация +200, Опыт +150.\nНаграда (Олово): Деньги 155.000$, Репутация +200, Опыт +150.\nНаграда (Золото): Деньги 180.000$, Репутация +200, Опыт +150.', parse_mode='html')
    if message.text == '◻️ Краткий гайд ◻️':
        ph12 = open('contr6.png', 'rb')
        ph13 = open('contr7.png', 'rb')
        bot.send_photo(message.chat.id, ph12)
        bot.send_photo(message.chat.id, ph13)
        bot.send_message(message.chat.id, 'Коротко обо всем')


bot.polling(none_stop=True)






# @bot.message_handler()
# def user_message(message):
#     name = f'Привет, <b>{message.from_user.first_name}</b>!'
#     if message.text == 'Привет' or message.text == 'привет' or message.text == 'ПРИВЕТ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'Хай' or message.text == 'хай' or message.text == 'ХАЙ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'Ку' or message.text == 'ку' or message.text == 'КУ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'мусор':
#         photo = open('Capture001.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')

# @bot.message_handler(commands=['musor'])
# def musor(message):
#     markup = types.InlineKeyboardMarkup()
#     photo = open('Capture001.png', 'rb')
#     markup.add(types.InlineKeyboardButton('Открыть карту мусорок', {bot.send_photo(message.chat.id, photo)}))           #Верно
#     bot.send_message(message.chat.id, 'Перейти к картинке', reply_markup=markup)
#
# @bot.message_handler(commands=['phone'])
# def phone(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Открыть карту телефонов', url='https://media.discordapp.net/attachments/983658895627141120/984053150875021372/93a91e4ca0c79c39.jpg?width=432&height=701'))
#     bot.send_message(message.chat.id, 'Перейти к картинке', reply_markup=markup)

# @bot.message_handler(commands=['help'])
# def help(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     photo = open('Capture001.png', 'rb')
#     btn1 = types.KeyboardButton('КАРТА МУСОРА', {bot.send_photo(message.chat.id, photo)})
#     btn2 = types.KeyboardButton('КАРТА МУСОРА', {bot.send_photo(message.chat.id, photo)})
#     markup.add(btn2, btn1)
#     bot.send_message(message.chat.id, 'Выберете нужный пункт', reply_markup=markup)


    # @bot.message_handler(commands=['start'])
    # def battlepass(message):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #     musor = types.KeyboardButton('Карта мусорок')
    #     phones = types.KeyboardButton('Карта телефонов')
    #     markup.add(musor, phones)
    #     bot.send_message(message.chat.id, 'Выберете нужный пункт', reply_markup=markup)

# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5995857148:AAF4_wUGvJjMuIQjOIjdNFjqKJJUQQ1Abkk')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name}</b>!'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler()
# def user_message(message):
#     name = f'Привет, <b>{message.from_user.first_name}</b>!'
#     if message.text == 'Привет' or message.text == 'привет' or message.text == 'ПРИВЕТ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'Хай' or message.text == 'хай' or message.text == 'ХАЙ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'Ку' or message.text == 'ку' or message.text == 'КУ':
#         bot.send_message(message.chat.id, name, parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('Capture001.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Карта мусорок', url='https://pypi.org/project/pyTelegramBotAPI/')
#     bot.send_message(message.chat.id, 'go', reply_markup=markup)
#
#
#
# @bot.message_handler(commands=['start'])
# def battlepass(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     musor = types.KeyboardButton('Карта мусорок')
#     phones = types.KeyboardButton('Карта телефонов')
#     markup.add(musor, phones)
#     bot.send_message(message.chat.id, 'Выберете нужный пункт', reply_markup=markup)
#
#
# bot.polling(none_stop=True)