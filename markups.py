from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_menu = InlineKeyboardMarkup()
btn_new_gdz = InlineKeyboardButton(text = "Новое ГДЗ", callback_data="menu_new_hm")
btn_essay = InlineKeyboardButton(text = "Сочинение", callback_data="menu_essay")

keyboard_menu.insert(btn_new_gdz)
keyboard_menu.insert(btn_essay)

keyboard_start_subject =InlineKeyboardMarkup(row_width=1)
btn_math_geo = InlineKeyboardButton(text = "Математика/Геометрия", callback_data="sub_math_geo")
btn_phys = InlineKeyboardButton(text = "Физика", callback_data="sub_phys")
btn_chemistry = InlineKeyboardButton(text = "Химия", callback_data="sub_chemistry")


keyboard_start_subject.insert(btn_math_geo)
keyboard_start_subject.insert(btn_phys)
keyboard_start_subject.insert(btn_chemistry)

keyboard_next =InlineKeyboardMarkup()
btn_next = InlineKeyboardButton(text="Далее", callback_data="next_send")
keyboard_next.insert(btn_next)

keyboard_check = InlineKeyboardMarkup()
btn_check = InlineKeyboardButton(text="Проверить подписку", callback_data="check")
keyboard_check.insert(btn_check)

