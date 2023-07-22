### Опиcание проекта.
Тестовое задания для Яндекс Практикум.
Телеграм бот с использованием фреймворка telebot.
Вызов всех команд доступен как по вызову кнопок, так и по написанию в поле ввода текста бота.

## Инструкции по установке
***- Клонируйте репозиторий:***
```
git clone git@github.com:PashkaVRN/test_job_practicum.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
```
***- Активируйте виртуальное окружение:***
```
source venv/bin/activate
source venv/Scripts/activate
```

***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Создайте .env файл и введите туда токен бота:*** 
```
TOKEN=*************************************************
```

***- Запустите телеграм бот в локально режиме:***
```
python bot.py
```



