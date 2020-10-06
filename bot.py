from telebot import types
import telebot, random, time;
bot = telebot.TeleBot('1253646147:AAGSW1B5VAgD2Sw_Gaa0I5t8WBEKhg4v9B0');
name = ''
surname = ''
timeyou = 0

file = open("input.txt", "r")
file1 = open("imagelist.txt", "r")
lines = file.read().splitlines()
lines1 = file1.read().splitlines()
file.close()
file1.close()
count = len(lines)
que = random.randint(0, count-1)
answ = lines[que]
que = lines1[que]

@bot.message_handler(commands=['start'])
def start(message):
		bot.send_message(message.from_user.id, str(que))
		bot.send_message(message.from_user.id, 'Расшифруй ребус')

@bot.message_handler(content_types=['text'])
def start_welcome(message):
    if message.text == answ:
        bot.send_message(message.from_user.id, "Всё верно, напиши своё имя и фамилию для рейтинга:)")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши верный ответ')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + 'твоё время ответа: ' + timeyou + ' сек')

bot.polling(none_stop=False, interval=0)