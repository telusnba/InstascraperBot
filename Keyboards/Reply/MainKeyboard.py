from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard():
    main_kb = ReplyKeyboardBuilder()

    main_kb.button(text='/stories')
    main_kb.adjust(2)
    return main_kb.as_markup()
