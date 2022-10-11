import telebot
from telebot import types
import kurs

# Создаем экземпляр  TelegramBot
bot = telebot.TeleBot('Telegram_bot_API_key')


class ConvertionException(Exception):
    pass


# Обработка команды \start
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    user_id = message.from_user.id
    text = '💱 Валютные операции\n Курсы валют: /kurs \n Доллар 🔄 Сум: /usd_to_uzs  \n Сум 🔄 Доллар: /uzs_to_usd \n Евро 🔄 Сум: /eur_to_uzs \n Сум 🔄 Евро: /uzs_to_eur \n  Рубль 🔄 Сум: /rub_to_uzs \n Сум 🔄 Рубль: /uzs_to_rub'
    service_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    service1 = types.KeyboardButton('/kurs', )
    service2 = types.KeyboardButton('/usd_to_uzs')
    service3 = types.KeyboardButton('/uzs_to_usd')
    service4 = types.KeyboardButton('/eur_to_uzs')
    service5 = types.KeyboardButton('/uzs_to_eur')
    service6 = types.KeyboardButton('/rub_to_uzs')
    service7 = types.KeyboardButton('/uzs_to_rub')

    # service_btn.row(service1)
    service_btn.add(service1, service2, service3, service4, service5, service6, service7)
    bot.send_message(user_id, 'Выберите услугу', reply_markup=service_btn)


# KURS
@bot.message_handler(commands=['kurs'])
def kurs_info(message: telebot.types.Message):
    user_id = message.from_user.id
    bot.send_message(user_id,
                     f'Курс Валють на {kurs.date()[0]} \n 🇪🇺{kurs.eur()[0][0]}: {kurs.eur()[0][1]}\n 🇺🇸{kurs.usd()[0][0]}: {kurs.usd()[0][1]}\n 🇷🇺{kurs.rub()[0][0]}: {kurs.rub()[0][1]}\n')


# Convert UZS to USD
@bot.message_handler(commands=['uzs_to_usd'])
def uzs_to_usd(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Конвертирую UZS на USD")
    bot.register_next_step_handler(message, uzsusd)


def uzsusd(message):
    kurs_usd = float(kurs.usd()[0][1])  # наш курс цифрой
    try:
        amount1 = float(message.text)  # конвертируем входящие данные в число
        total1 = round((amount1 / kurs_usd), 2)  # находим нужное количество
        result = f'{amount1} UZS это {total1} USD'  # выводим результат
        if type(amount1) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount1}')
    except:
        bot.send_message(message.from_user.id, "Ввели не число")
        return
    bot.send_message(message.chat.id, result)


# Convert USD to UZS
@bot.message_handler(commands=['usd_to_uzs'])
def usd_to_uzs(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Конвертирую USD на UZS")
    bot.register_next_step_handler(message, usduzs)


def usduzs(message):
    user_id = message.from_user.id
    kurs_usd = float(kurs.usd()[0][1])  # наш курс цифрой
    try:
        amount2 = float(message.text)  # конвертируем входящие данные в число
        total2 = round((amount2 * kurs_usd), 2)  # находим нужное количество
        result2 = f'{amount2} USD это {total2} UZS'  # выводим результат
        if type(amount2) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount2}')
    except:
        bot.send_message(user_id, "Вы ввели не число")
        return
    bot.send_message(user_id, result2)


# Convert EUR to UZS
@bot.message_handler(commands=['eur_to_uzs'])
def eur_to_uzs(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Конвертирую EUR на UZS")
    bot.register_next_step_handler(message, euruzs)


def euruzs(message):
    user_id = message.chat.id
    kurs_eur = float(kurs.eur()[0][1])  # наш курс цифрой
    try:
        amount3 = float(message.text)  # конвертируем входящие данные в число
        total3 = round((amount3 * kurs_eur), 2)  # находим нужное количество
        result2 = f'{amount3} EUR это {total3} UZS'  # выводим результат
        if type(amount3) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount3}')
    except:
        bot.send_message(user_id, "Вы ввели не число")
        return
    bot.send_message(user_id, result2)


# Convert UZS to EUR
@bot.message_handler(commands=['uzs_to_eur'])
def uzs_to_eur(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Конвертирую UZS на EUR")
    bot.register_next_step_handler(message, uzseur)


def uzseur(message):
    user_id = message.chat.id
    kurs_eur = float(kurs.eur()[0][1])  # наш курс цифрой
    try:
        amount4 = float(message.text)  # конвертируем входящие данные в число
        total4 = round((amount4 / kurs_eur), 2)  # находим нужное количество
        result4 = f'{amount4} UZS это {total4} EUR'  # выводим результат
        if type(amount4) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount4}')
    except:
        bot.send_message(user_id, "Вы ввели не число")
        return
    bot.send_message(user_id, result4)


# Convert UZS to RUB
@bot.message_handler(commands=['uzs_to_rub'])
def uzs_to_rub(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Конвертирую UZS на RUB")
    bot.register_next_step_handler(message, uzsrub)


def uzsrub(message):
    user_id = message.chat.id
    kurs_rub = float(kurs.rub()[0][1])  # наш курс цифрой
    try:
        amount5 = float(message.text)  # конвертируем входящие данные в число
        total5 = round((amount5 / kurs_rub), 2)  # находим нужное количество
        result5 = f'{amount5} UZS это {total5} RUB'  # выводим результат
        if type(amount5) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount5}')
    except:
        bot.send_message(user_id, "Вы ввели не число")
        return
    bot.send_message(user_id, result5)


# Convert RUB to UZS
@bot.message_handler(commands=['rub_to_uzs'])
def rub_to_uzs(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Конвертирую RUB на UZS ")
    bot.register_next_step_handler(message, rubuzs)


def rubuzs(message):
    user_id = message.chat.id
    kurs_rub = float(kurs.rub()[0][1])  # наш курс цифрой
    try:
        amount6 = float(message.text)  # конвертируем входящие данные в число
        total6 = round((amount6 * kurs_rub), 2)  # находим нужное количество
        result6 = f'{amount6} RUB это {total6} UZS'  # выводим результат
        if type(amount6) == str:
            raise ConvertionException(f'Не удалось обработать количество {amount6}')
    except:
        bot.send_message(user_id, "Вы ввели не число")
        return
    bot.send_message(user_id, result6)


try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass
