# Art Room Telegram Bot

Telegram-бот для дизайн-студии **Art Room**.  
Позволяет клиентам ознакомиться с услугами, посмотреть примеры работ и оставить заявку.

[![Python](https://img.shields.io/badge/Python-✓-blue)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4)](https://core.telegram.org/bots/api)

## 🚀 Запуск

```bash
git clone https://github.com/EvgenySkorik/Art_room_tg_bot.git
cd Art_room_tg_bot
pip install pyTelegramBotAPI
TG_API_KEY=ваш_токен python main.py
```

## 📋 Функционал

- Информация об услугах компании
- Просмотр примеров дизайн-проектов (случайное фото)
- Ссылка на сайт компании
- Оформление заявки с сохранением в лог

## 🛠 Стек

- **pyTelegramBotAPI** (telebot)
- **Inline-клавиатура** с URL-ссылками
- **Логирование заявок** в файл

## 📁 Структура

```
.
├── art_room_bot/
│   ├── handler_bot.py    # Основная логика бота
│   └── main.py           # Точка входа + обработчики
├── foto_art/             # Примеры работ (фото)
├── .gitignore
└── README.md
```

## 👤 Автор

[Evgeny Skorik](https://github.com/EvgenySkorik)
