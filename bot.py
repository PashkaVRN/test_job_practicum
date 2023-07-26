import glob
import logging
import os

import telebot
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    encoding='utf-8-sig')

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Кнопки внутри бота. """

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3)
    buttons = [
        telebot.types.KeyboardButton(text='Мое последнее селфи'),
        telebot.types.KeyboardButton(text='Мое студенческое фото'),
        telebot.types.KeyboardButton(text='Мое увлечение'),
        telebot.types.KeyboardButton(text='Расскажи про gpt'),
        telebot.types.KeyboardButton(text='Расскажи о SQL и noSQL'),
        telebot.types.KeyboardButton(text='Расскажи историю любви'),
        telebot.types.KeyboardButton(text='Исходный код бота')
    ]
    keyboard.add(*buttons)
    logging.info('Бот запущен')
    bot.reply_to(
        message,
        'Привет!\n '
        'Бот умеет распознавать текстовые команды, так же как и нажатия кнопок\n '
        'Использование нижнего и верхнего регистра символов поддерживается:\n '
        'В ответ на эти команды бот пришлет аудиофайл:\n '
        '- Расскажи про GPT\n '
        '- Расскажи о SQL и noSQL\n '
        '- Расскажи историю любви\n '
        'Если пропадает меню выбора кнопок, нажмите на символ 4 точек в нижнем правом углу.\n '
        'Если возникнут вопросы пишите мне в телеграм: @pashkavrn\n '
        'Хорошего дня :)',
        reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'мое последнее селфи')
def send_selfie(message):
    """Метод отправки моего последнего селфи при нажатии на кнпоку в боте."""

    logging.info('Запрос на отправку селфи')
    selfie_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'my_selfi')
    photo_paths = glob.glob(os.path.join(selfie_dir, '*.jpg'))

    for photo_path in photo_paths:
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            logging.info('Селфи отправлено')


@bot.message_handler(func=lambda message: message.text.lower() == 'мое студенческое фото')
def send_college_photo(message):
    """Метод отправки моих студенческих фотографий. """

    logging.info('Запрос на отправку студенческого фото.')
    post_text = (
        'К сожалению, у меня не остальнось фотографий из школы, '
        'по этому я решил приложить фотографии с учебы в колледже :-) '
    )
    photos_dir = 'my_college_photo'
    photos = os.listdir(photos_dir)
    bot.send_message(message.chat.id, post_text)

    for photo_filename in photos:
        photo_path = os.path.join(photos_dir, photo_filename)
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            logging.info('Студенческое фото отправлено.')


@bot.message_handler(func=lambda message: message.text.lower() == 'мое увлечение')
def send_hobby(message):
    """Метод отправки поста и фотографий о моем увлечении. """

    logging.info('Запрос на отправку поста о моем увлечении.')
    post_text = (
        'Привет! Меня зовут Павел и я увлекаюсь альпинизмом '
        'и программированием. В этом посте я расскажу об альпинизме. '
        'Я несколько лет занимаюсь этим видом спорта, сходил несколько горных '
        'вершин в спортивном стиле в том числе на высочайшую '
        'гору Европы Эльбрус. В альпинизме как и в программировании важно '
        'иметь дружную команду в которой есть взаимопонимание '
        'и работа над общим делом. Каждый год я с нетерпением '
        'жду начала отпуска и отправляюсь в горы!'
    )
    photos_dir = 'my_hobby'
    photos = os.listdir(photos_dir)
    bot.send_message(message.chat.id, post_text)

    for photo_filename in photos:
        photo_path = os.path.join(photos_dir, photo_filename)
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            logging.info('Пост о моем увлечении отправлен')


@bot.message_handler(func=lambda message: message.text.lower() == 'расскажи про gpt')
def send_audio_gpt(message):
    """Метод для отправки аудиофайла о GPT. """

    logging.info('Запрос на оптравку аудиофайла о GPT.')
    audio = open('voice/gpt.m4a', 'rb')
    bot.send_audio(message.chat.id, audio)
    logging.info('Аудиофайл о GPT отправлен.')


@bot.message_handler(func=lambda message: message.text.lower() == 'расскажи о sql и nosql')
def send_audio_sql_nosql(message):
    """Метод для отправки аудиофайла о SQL и noSQL. """

    logging.info('Запрос на оптравку аудиофайла о SQL.')
    audio = open('voice/sql_nosql.m4a', 'rb')
    bot.send_audio(message.chat.id, audio)
    logging.info('Аудиофайл о SQL отправлен')


@bot.message_handler(func=lambda message: message.text.lower() == 'расскажи историю любви')
def send_audio_love(message):
    """Метод для отправки аудиофайла о истории любви. """

    logging.info('Запрос на оптравку аудиофайла о истории любви.')
    audio = open('voice/love.m4a', 'rb')
    bot.send_audio(message.chat.id, audio)
    logging.info('Аудиофайл о истории любви отправлен.')


@bot.message_handler(func=lambda message: message.text.lower() == 'исходный код бота')
def send_source_code(message):
    """Метод отправляющий ссылку на исходный код бота."""

    logging.info('Запрос на оптравку исходного кода бота.')
    bot.send_message(message.chat.id, 'Ссылка на исходный код бота: https://github.com/PashkaVRN/test_job_practicum')
    logging.info('Исходный код бота отправлен.')


if __name__ == "__main__":
    bot.infinity_polling()
