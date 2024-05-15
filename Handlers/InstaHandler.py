from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Core.Insta import get_stories, is_image, is_video
from States.MainState import MyState
from loader import dp


@dp.message(Command('stories'))
async def process_start_command(message: types.Message, state: FSMContext):
    await message.answer("Надішли ім'я користувача", parse_mode='HTML')
    await state.set_state(MyState.ask)


@dp.message(MyState.ask)
async def location_handler(message: types.Message):
    await message.answer(f"♻️♻️♻️", parse_mode='HTML')
    user_input = message.text
    stories_links = get_stories(user_input)
    if isinstance(stories_links, str):
        await message.answer(f"{stories_links}", parse_mode='HTML')
    elif isinstance(stories_links, list):
        media = []
        for url in stories_links:
            if is_image(url):
                media.append(types.InputMediaPhoto(media=url))
            elif is_video(url):
                media.append(types.InputMediaVideo(media=url))
        await message.answer_media_group(media)
