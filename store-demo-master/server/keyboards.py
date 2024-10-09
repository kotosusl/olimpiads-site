from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


to_site_btn = KeyboardButton(text='Перейти на сайт с олимпиадами')
send_help_btn = KeyboardButton(text='Помощь')
delete_telegram_notif_btn = KeyboardButton(text='Не присылать уведомления в боте')
add_telegram_notif_btn = KeyboardButton(text='Включить уведомления в боте')

menu_keyboard_with_notif = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   row_width=1).add(to_site_btn, send_help_btn, delete_telegram_notif_btn)

menu_keyboard_without_notif = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   row_width=1).add(to_site_btn, send_help_btn, add_telegram_notif_btn)
menu_keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                          row_width=1).add(to_site_btn, send_help_btn)