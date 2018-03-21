import telebot
import random
import datetime
""" Данный бот создан для отправки мотивационных сообщений пользователям мессенджера telegram. Сообщения отправляются
 как по запросу в виде произвольного текстового набора, так и по временному промежутку в 6 часов (данный алгоритм запус-
 кается командой /start"""
"""This bot was created for sending motivate messages to users of telegram. Messages sends by user's request (random text request) and by time period in 6 hours, too
(this mode launches automatically by starting bot)"""

token = 'NOT_A_REAL_TOKEN' #here is token\ это токен
bot = telebot.TeleBot(token)



list1 = ['Man,', 'Friend,','Buddy,', 'Dude,', 'Pal,', 'Comrad,', 'Mate,', 'Brother,', 'Bro,',
         'Soldier,']  #list of allocutions\ список обращений к пользователю

list2 = ['pump this shit', 'you can break rocks', 'you will overcome this borders', 'your body - your castle',
          'go to the gym', 'lazy is not about you', 'wake up', 'keep calm and keep pumping',
          'do your best', 'you became stronger', 'all depends on you', 'no one can hold you', 'always be better than before',
         'pain in your muscles means your growning', 'brain is your main muscle', 'don\'t stop', 'never give up',
         'all within your hands', 'be worthy to your\'s respect', 'love yourself', 'head by your own way',
         'you can be the best', 'never sit on one place', 'dream on, and dreams will come true',
         'this world was made for you, so take it', 'be steady', 'eat vegetables', 'podnimy carya na pero', 'svergni putina'
         ] #motivate phrases\ мотивирующие фразы

list3 = ['',
         '',
         '',
         '',
         '',
         '',
         '',
         '',] #empty list for some kind of stuff(smiles)\ лист для смайликов (заполнение на ваше усмотрение с импользованием таблицы кодировок эмоджи)



list_of_picture = ['https://i.pinimg.com/736x/71/75/6c/71756c698af108b9ec5efaf47a7b36ee--design-typography-journal.jpg',
                   'https://www.google.com.ua/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiy7IDQvbDZAhVLbFAKHXrMA4UQjRwIBw&url=https%3A%2F%2Fru.pinterest.com%2Fpin%2F375276581440009345%2F&psig=AOvVaw3YzTxYYKzmHH_TDpTOJM7X&ust=1519078107240848',
                   ] #list of picture's URLs\ список ссылок на медиа контент

print(len(list1))
print(len(list2))
print(len(list3))
print(len(list_of_picture))
#upper you can see output commands of  quantity elements in lists\выше указаны команды для вывода длин списков
while True:
  try: #endless cycle upper and here exception start \ Выше - бесконеный цикл, а на этой строке начало исключения
     @bot.message_handler(commands=['start'])#functions under decorator launches after typing and sending /start \ функция под декоратором запускается после отправки боту команды start
     def timing_messages(message):
       while True: #function check daytime\ функция поверяет время суток
         now = datetime.datetime.now()
         if now.hour == 10 and now.minute == 00 and now.second == 00:
            bot.send_photo(message.chat.id, list_of_picture[random.randint(0, 1)])
         elif now.hour == 16 and now.minute == 00 and now.second == 00:
            bot.send_photo(message.chat.id, list_of_picture[random.randint(0, 1)])          


     @bot.message_handler(content_types= ['text'])
     def answer(message):
         #rands uses for making original prases and make bot more interesting\ случайные числа используются для создания оригинальных фраз
      a = random.randint(0,19)#rands to send only a photo
      if 0 <= a <= 2:
         bot.send_photo(message.chat.id, list_of_picture[random.randint(0, 1)]) #sending photo here\ подготовка медиа к отправке тут
      else:
         b = random.randint(0, 3) #randoms for text messages\ случайные для текстовых сообщений
         if 0 <= b <= 2:
            answer = list1[random.randint(0, 9)] + " " + list2[random.randint(0, 28)] #produsing the short phrase \ создаем короткие фразы
         else:
            answer = list1[random.randint(0, 9)] + " " + list2[random.randint(0, 28)] + " " + list3[random.randint(0, 7)]
            #produsing long phrase upphere\ создаем длинные фразы
      bot.send_message(message.chat.id, answer) #sending prodused message \ отправка сообщения
   except:
     bot.send_message('Чат id создателя', 'Возникла ошибка, перезапуск бота') #message for developer \ сообщение для разработчика







bot.polling(none_stop= True, interval= 0) #for endless bot working
