import os
import io
import sys
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, WebAppData
from dotenv import load_dotenv

from database import init_db, get_or_create_user, get_user, update_user_progress, mark_exercise_done, mark_exercise_failed, get_leaderboard
from lessons import LESSONS

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Middleware для обработки ошибок
class ErrorMiddleware:
    async def __call__(self, handler, event, data):
        try:
            return await handler(event, data)
        except Exception as e:
            print(f"Error in handler: {e}")
            raise  # Пробрасываем дальше, чтобы aiogram обработал

dp.update.middleware(ErrorMiddleware())

USER_STATE = {}


def get_menu_kb(user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Уроки", callback_data="lessons")],
        [InlineKeyboardButton(text="🏆 Рейтинг", callback_data="leaderboard")],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="stats")],
    ])
    return kb


@dp.message(Command("start"))
async def cmd_start(message: Message):
    user = get_or_create_user(
        message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
    )
    if user is None:
        user = get_or_create_user(message.from_user.id)

    level = user.get("level", 1)
    xp = user.get("xp", 0)
    lesson_idx = user.get("lesson_index", 0)
    lesson_title = LESSONS[lesson_idx]["title"] if lesson_idx < len(LESSONS) else "Все пройдены!"

    welcome = (
        f"🐍 <b>Python Learn Bot</b>\n\n"
        f"Привет, {message.from_user.first_name}!\n\n"
        f"Изучай Python с нуля через теорию и практику.\n\n"
        f"📊 <b>Твой прогресс:</b>\n"
        f"⭐ Уровень: {level}\n"
        f"✨ XP: {xp}\n"
        f"📖 Урок: {lesson_title}\n"
    )

    try:
        await message.answer(welcome, reply_markup=get_menu_kb(user), parse_mode="HTML")
    except Exception:
        pass


@dp.message(Command("lessons"))
async def cmd_lessons(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        user = get_or_create_user(message.from_user.id)

    lesson_idx = user.get("lesson_index", 0)
    text = "<b>📚 Уроки</b>\n\n"

    for i, lesson in enumerate(LESSONS):
        status = "✅" if i < lesson_idx else "🔒" if i == lesson_idx else "⬜"
        if i == lesson_idx:
            status = "▶️"
        text += f"{status} {lesson['index'] + 1}. {lesson['title']}\n"

    text += "\nНажми на урок чтобы начать!"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"📖 {l['title']}", callback_data=f"lesson_{l['index']}")]
        for l in LESSONS
    ])

    await message.answer(text, reply_markup=kb, parse_mode="HTML")


@dp.callback_query(lambda c: c.data.startswith("lesson_"))
async def cb_lesson(callback: types.CallbackQuery):
    try:
        lesson_idx = int(callback.data.split("_")[1])
        lesson = LESSONS[lesson_idx]

        user = get_user(callback.from_user.id)
        if user is None:
            user = get_or_create_user(callback.from_user.id)

        USER_STATE[callback.from_user.id] = {
            "state": "exercise",
            "lesson_index": lesson_idx,
            "exercise_index": 0,
        }

        await callback.message.answer(
            lesson["theory"],
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="💻 Терминал", callback_data=f"terminal_{lesson_idx}")],
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="lessons")],
            ]),
            parse_mode="HTML",
        )
    except Exception as e:
        await callback.message.answer(f"Ошибка: {e}")
    await callback.answer()


@dp.callback_query(lambda c: c.data == "lessons")
async def cb_lessons(callback: types.CallbackQuery):
    try:
        user = get_user(callback.from_user.id)
        if user is None:
            user = get_or_create_user(callback.from_user.id)

        lesson_idx = user.get("lesson_index", 0)
        text = "<b>📚 Уроки</b>\n\n"

        for i, lesson in enumerate(LESSONS):
            status = "✅" if i < lesson_idx else "🔒" if i == lesson_idx else "⬜"
            if i == lesson_idx:
                status = "▶️"
            text += f"{status} {lesson['index'] + 1}. {lesson['title']}\n"

        text += "\nНажми на урок чтобы начать!"

        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"📖 {l['title']}", callback_data=f"lesson_{l['index']}")]
            for l in LESSONS
        ])

        await callback.message.answer(text, reply_markup=kb, parse_mode="HTML")
    except Exception as e:
        await callback.message.answer(f"Ошибка: {e}")
    await callback.answer()


@dp.callback_query(lambda c: c.data.startswith("terminal_"))
async def cb_terminal(callback: types.CallbackQuery):
    lesson_idx = int(callback.data.split("_")[1])
    lesson = LESSONS[lesson_idx]

    # Сохраняем данные урока для Mini App
    lesson_data = {
        "index": lesson["index"],
        "title": lesson["title"],
        "expectedOutput": lesson["expected_output"],
        "starterCode": lesson["starter_code"],
        "hints": lesson["hints"],
    }
    import json
    import base64

    encoded = base64.b64encode(json.dumps(lesson_data, ensure_ascii=False).encode()).decode()

    # index.html — данные урока в URL hash, ноль сетевых запросов
    app_url = f"https://tigrik234.github.io/python-learn-bot/index.html#data={encoded}"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💻 Открыть IDE", web_app=WebAppInfo(url=app_url))],
    ])

    await callback.message.answer(
        f"💻 Открой редактор кода:\n\nУрок {lesson_idx + 1}: {lesson['title']}\n"
        f"Задание: {lesson['expected_output']}",
        reply_markup=kb,
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "run_code")
async def cb_run_code(callback: types.CallbackQuery):
    state = USER_STATE.get(callback.from_user.id)
    if not state or state["state"] != "terminal":
        await callback.answer("Сначала открой терминал урока.")
        return

    if not state["code_lines"]:
        await callback.answer("Код пуст! Напиши код в терминале.")
        return

    user_code = "\n".join(state["code_lines"])
    lesson_idx = state["lesson_index"]
    lesson = LESSONS[lesson_idx]

    try:
        result = run_user_code(user_code, lesson)
    except Exception as e:
        await callback.answer(f"Ошибка: {str(e)}")
        return

    if result["success"]:
        await callback.message.answer(f"✅ Отлично! Код верный. +10 XP")
        update_user_progress(callback.from_user.id, lesson_idx + 1, 10)
        mark_exercise_done(callback.from_user.id, lesson_idx, 0, user_code, result["output"])
        state["code_lines"] = []

        term_text = build_terminal_text(lesson, [])
        await update_terminal_with_keyboard(callback.from_user.id, term_text)
    else:
        await callback.message.answer(f"❌ Неверно. Ожидалось: {lesson['expected_output']}")
        # Автоматически очищаем код
        state["code_lines"] = []

        term_text = build_terminal_text(lesson, [])
        await update_terminal_with_keyboard(callback.from_user.id, term_text)

    await callback.answer()


@dp.callback_query(lambda c: c.data == "show_hint")
async def cb_show_hint(callback: types.CallbackQuery):
    state = USER_STATE.get(callback.from_user.id)
    if not state or state["state"] != "terminal":
        await callback.answer("Сначала открой терминал урока.")
        return

    lesson_idx = state["lesson_index"]
    lesson = LESSONS[lesson_idx]
    hint_idx = state.get("hint_index", 0)

    if hint_idx < len(lesson["hints"]):
        hint = lesson["hints"][hint_idx]
        state["hint_index"] = hint_idx + 1
        await callback.answer(hint, show_alert=True)
    else:
        await callback.answer("Подсказки закончились!", show_alert=True)


@dp.callback_query(lambda c: c.data == "clear_code")
async def cb_clear_code(callback: types.CallbackQuery):
    state = USER_STATE.get(callback.from_user.id)
    if not state or state["state"] != "terminal":
        await callback.answer("Сначала открой терминал урока.")
        return

    state["code_lines"] = []
    lesson_idx = state["lesson_index"]
    lesson = LESSONS[lesson_idx]

    term_text = build_terminal_text(lesson, [])
    await update_terminal_with_keyboard(callback.from_user.id, term_text)
    await callback.answer("Код очищен.")


@dp.callback_query(lambda c: c.data == "show_theory")
async def cb_show_theory(callback: types.CallbackQuery):
    state = USER_STATE.get(callback.from_user.id)
    if not state or state["state"] != "terminal":
        await callback.answer("Сначала открой терминал урока.")
        return

    lesson_idx = state["lesson_index"]
    lesson = LESSONS[lesson_idx]

    await callback.message.answer(lesson["theory"], parse_mode="HTML")
    await callback.answer()


async def update_terminal(user_id, text):
    """Обновляет терминальное сообщение пользователя (без кнопок)."""
    state = USER_STATE.get(user_id)
    if not state or state.get("terminal_msg_id") is None:
        return
    try:
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=state["terminal_msg_id"],
            text=text,
        )
    except Exception:
        pass


async def update_terminal_with_keyboard(user_id, text):
    """Обновляет терминальное сообщение с кнопками."""
    state = USER_STATE.get(user_id)
    if not state or state.get("terminal_msg_id") is None:
        return
    try:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🚀 Run Code", callback_data="run_code")],
            [InlineKeyboardButton(text="💡 Подсказка", callback_data="show_hint"),
             InlineKeyboardButton(text="🗑 Очистить", callback_data="clear_code")],
            [InlineKeyboardButton(text="📖 Теория", callback_data="show_theory"),
             InlineKeyboardButton(text="⬅️ Назад", callback_data="lessons")],
        ])
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=state["terminal_msg_id"],
            text=text,
            reply_markup=kb,
        )
    except Exception:
        pass


def build_terminal_text(lesson, code_lines):
    """Собирает текст терминала."""
    lines = [
        f"💻 Терминал — Урок {lesson['index'] + 1}: {lesson['title']}",
        "─" * 40,
        f"Задание: {lesson['expected_output']}",
        "─" * 40,
        "Код:",
    ]
    if code_lines:
        for i, line in enumerate(code_lines, 1):
            lines.append(f"{i:>3} | {line}")
    else:
        lines.append("(пусто)")
    return "\n".join(lines)


@dp.message(Command("run"))
async def cmd_run(message: Message):
    await message.answer("Используй кнопку 🚀 Run Code в терминале.")


@dp.message(Command("clear"))
async def cmd_clear(message: Message):
    await message.answer("Используй кнопку 🗑 Очистить в терминале.")


@dp.message(Command("next"))
async def cmd_next(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        user = get_or_create_user(message.from_user.id)

    lesson_idx = user.get("lesson_index", 0)
    if lesson_idx >= len(LESSONS):
        await message.answer("Все уроки пройдены!")
        return

    lesson = LESSONS[lesson_idx]
    await message.answer(
        f"Урок {lesson_idx + 1}: {lesson['title']}\n\n{lesson['theory']}\n\nНажми 💻 Терминал чтобы начать практику.",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💻 Терминал", callback_data=f"terminal_{lesson_idx}")],
        ]),
        parse_mode="HTML",
    )


@dp.message(lambda m: hasattr(m, 'web_app_data') and m.web_app_data)
async def handle_web_app_data(message: Message):
    """Обрабатывает данные из Mini App."""
    try:
        import json
        web_app_data = message.web_app_data
        data = json.loads(web_app_data.data)
        if data.get('action') == 'lesson_complete':
            lesson_idx = data.get('lessonIndex', 0)
            user_id = message.from_user.id

            # Обновляем прогресс
            update_user_progress(user_id, lesson_idx + 1, 10)

            await bot.send_message(
                user_id,
                f"✅ Урок {lesson_idx + 1} пройден! +10 XP\n\nОтличная работа!"
            )
    except Exception as e:
        print(f"Error handling web app data: {e}")


@dp.message()
async def cmd_code(message: Message):
    state = USER_STATE.get(message.from_user.id)
    if not state or state["state"] != "terminal":
        return

    # Добавляем строку в код
    if "code_lines" not in state:
        state["code_lines"] = []
    state["code_lines"].append(message.text.strip())

    # Обновляем терминал
    lesson_idx = state["lesson_index"]
    lesson = LESSONS[lesson_idx]
    term_text = build_terminal_text(lesson, state["code_lines"])
    await update_terminal_with_keyboard(message.from_user.id, term_text)


@dp.callback_query(lambda c: c.data == "leaderboard")
async def cb_leaderboard(callback: types.CallbackQuery):
    try:
        lb = get_leaderboard(10)
        text = "<b>🏆 Рейтинг</b>\n\n"
        for i, entry in enumerate(lb, 1):
            name = entry.get("username") or entry.get("first_name") or f"User{entry['user_id']}"
            xp = entry.get("xp", 0)
            level = entry.get("level", 1)
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            text += f"{medal} {name}: {xp} XP, ур. {level}\n"
        if not lb:
            text += "Пока никто не участвует!\n\n"

        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")],
        ])

        await callback.message.answer(text, parse_mode="HTML", reply_markup=kb)
    except Exception as e:
        await callback.message.answer(f"Ошибка: {e}")
    await callback.answer()


@dp.callback_query(lambda c: c.data == "stats")
async def cb_stats(callback: types.CallbackQuery):
    try:
        user = get_user(callback.from_user.id)
        if user is None:
            user = get_or_create_user(callback.from_user.id)

        text = (
            f"<b>📊 Твоя статистика</b>\n\n"
            f"⭐ Уровень: {user.get('level', 1)}\n"
            f"✨ XP: {user.get('xp', 0)}\n"
            f"🔥 Серия: {user.get('streak', 0)}\n"
            f"🏆 Лучшая серия: {user.get('best_streak', 0)}\n"
            f"📖 Урок: {user.get('lesson_index', 0) + 1}/{len(LESSONS)}\n"
            f"📅 Начал: {user.get('created_at', 'unknown')[:10]}"
        )

        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")],
        ])

        await callback.message.answer(text, parse_mode="HTML", reply_markup=kb)
    except Exception as e:
        await callback.message.answer(f"Ошибка: {e}")
    await callback.answer()


@dp.callback_query(lambda c: c.data == "back")
async def cb_back(callback: types.CallbackQuery):
    try:
        await cmd_start(callback.message)
    except Exception:
        pass
    await callback.answer()


@dp.message(Command("next"))
async def cmd_next(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        user = get_or_create_user(message.from_user.id)

    lesson_idx = user.get("lesson_index", 0)
    if lesson_idx >= len(LESSONS):
        await message.answer("Все уроки пройдены!")
        return

    lesson = LESSONS[lesson_idx]
    await message.answer(
        f"Урок {lesson_idx + 1}: {lesson['title']}\n\n{lesson['theory']}\n\nНажми 💻 Терминал чтобы начать практику.",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💻 Терминал", callback_data=f"terminal_{lesson_idx}")],
        ]),
        parse_mode="HTML",
    )


def run_user_code(code: str, lesson: dict) -> dict:
    """Выполняет код пользователя и проверяет вывод."""
    captured_output = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        exec(code, {"__builtins__": __builtins__})
    except Exception as e:
        sys.stdout = old_stdout
        return {"success": False, "output": f"Ошибка: {str(e)}"}
    finally:
        sys.stdout = old_stdout

    output = captured_output.getvalue().strip()
    expected = lesson["expected_output"].strip()

    output_norm = "\n".join(line.strip() for line in output.split("\n") if line.strip())
    expected_norm = "\n".join(line.strip() for line in expected.split("\n") if line.strip())

    if output_norm == expected_norm:
        return {"success": True, "output": output}
    else:
        return {"success": False, "output": output}


async def main():
    init_db()
    try:
        await bot.delete_webhook()
    except Exception:
        pass
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
