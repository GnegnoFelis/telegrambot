from telebot import types
import telebot, random
from datetime import timedelta, datetime
bot = telebot.TeleBot()
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

@bot.message_handler(commands=['start', 'help'])
def start(message):
    global now
    bot.send_message(message.from_user.id, str(que))
    bot.send_message(message.from_user.id, "Расшифруй ребус")
    now = datetime.now()

@bot.message_handler(content_types=['text'])
def start_welcome(message):
    global now1
    if message.text == answ:
        now1 = "{} секунд".format((datetime.now() - now).total_seconds())
        bot.send_message(message.from_user.id, "Всё верно, напиши своё имя и фамилию для рейтинга:)")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, "Напиши верный ответ")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + ", твоё время ответа: " + str(now1))

bot.polling(none_stop=True, interval=0)
