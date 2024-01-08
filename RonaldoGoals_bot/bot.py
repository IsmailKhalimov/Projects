import requests
from bs4 import BeautifulSoup
import telebot

url="https://soccer365.ru/players/3596/?ysclid=lpllorelr189107832"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')
block = soup.find('div', id = "main_container").find_all('table', {'class': 'tablesorter'})[0].tbody.tr

date = block.find_all('td', {'class': 'al_c tb_value_gray'})[0].text[-10:]
score = block.find_all('td', {'class': "al_c"})[1].text.strip()
command = block.find_all('div', {'class': 'img16'})[0].text
riv = block.find_all('div', {'class': 'img16'})[1].text
goals = block.find_all('td', {'class': "al_c"})[2].text
assists = block.find_all('td', {'class': "al_c"})[3].text


bot=telebot.TeleBot('6926857713:AAGoAzI1I0DHlNg6iAemKKi3Jj3A8xkwmU0')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, Я <b>Криштиану Роналду</b> \n'
                                      'Здесь ты узнаешь информацию про мой последний матч. \n'
                                      'Просто запусти коману /match', parse_mode='html')
    
@bot.message_handler(commands=['match'])
def start(message):
    bot.send_message(message.chat.id, f'Дата: {date} \n'
                                      f'Команды: {command + " - " + riv} \n'
                                      f'Общий счёт: {score} \n'
                                      f'Голы Роналду: {goals} \n'
                                      f'Ассисты Роналду: {assists} \n'
                                      f'SSUUUUIIII', parse_mode='html')

bot.polling(none_stop=True)
