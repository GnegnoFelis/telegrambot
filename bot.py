import telebot, random, time;
from telebot import types
bot = telebot.TeleBot('1253646147:AAGSW1B5VAgD2Sw_Gaa0I5t8WBEKhg4v9B0');
bot.polling(none_stop=True, interval=0)
filename = input.txt
name = ''
surname = ''

file = open(filename, "r")
lines = file.read().splitlines()
file.close()
count = len(lines)
que = random.randint(0, count-1)
answ = lines[que]

que = str(que)+'.jpg'

@bot.message_handler(commands=['start'])
def start(message):
        bot.send_photo(message.from_user.id, open(que, 'rb'))
        timeyou = time.clock()
        
@bot.message_handler(content_types=['text'])
def start_welcome(message):
    if message.text == answ:
        timeyou = time.clock()
        bot.send_message(message.from_user.id, "Всё верно, напиши своё имя для рейтинга")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши верный ответ')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Напиши свою фамилию для рейтинга:)')
    bot.register_next_step_handler(message, get_surnme)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, name + ' ' + surname + 'твоё время ответа: ' + timeyou + ' сек')
