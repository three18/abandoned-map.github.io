import asyncio
import logging
import json
import time
import hashlib
import hmac
import os
import uuid
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.exceptions import TelegramForbiddenError
from aiohttp import web
from werkzeug.security import generate_password_hash, check_password_hash

# ================= НАСТРОЙКИ =================
TOKEN = "7740543552:AAEzVw2YQUySG4D4qh0lWmDSqYQREJr7U0Q"
ADMIN_GROUP_ID = -1003749438451
WEB_SERVER_PORT = 8080

# ⚠️ ВАЖНО: Вставь свой Telegram ID (супер-админ)
SUPER_ADMIN_ID = 5656488184

DATA_DIR = "data"
UPLOAD_DIR = "uploads"
FILES = {
    "users": f"{DATA_DIR}/users.json",
    "objects": f"{DATA_DIR}/objects.json",
    "reviews": f"{DATA_DIR}/reviews.json",
    "bans": f"{DATA_DIR}/bans.json",
    "admins": f"{DATA_DIR}/admins.json"
}

# Создаём папки
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================= СОСТОЯНИЯ =================
class RegForm(StatesGroup):
    nick = State()
    password = State()
    role = State()

class AddAdminForm(StatesGroup):
    user_id = State()
    role = State()

# ================= РАБОТА С ФАЙЛАМИ =================
def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        if filename == FILES["users"] or filename == FILES["objects"] or filename == FILES["reviews"]:
            return []
        return {}

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ================= ПРОВЕРКИ =================
def is_banned(user_id):
    bans = load_json(FILES["bans"])
    if str(user_id) in bans:
        expire = bans[str(user_id)]
        if expire == -1 or expire > time.time():
            return True
    return False

def is_super_admin(user_id):
    return user_id == SUPER_ADMIN_ID

def is_admin(user_id):
    if is_super_admin(user_id):
        return True
    admins = load_json(FILES["admins"])
    for admin in admins:
        if admin.get('id') == user_id and admin.get('status') == 'active':
            return True
    return False

def is_moderator(user_id):
    if is_super_admin(user_id):
        return True
    admins = load_json(FILES["admins"])
    for admin in admins:
        if admin.get('id') == user_id and admin.get('role') in ['admin', 'moderator'] and admin.get('status') == 'active':
            return True
    return False

def get_user_role(user_id):
    if is_super_admin(user_id):
        return 'admin'
    admins = load_json(FILES["admins"])
    for admin in admins:
        if admin.get('id') == user_id:
            return admin.get('role', 'stalker')
    return 'stalker'

def get_user_by_nickname(nickname):
    users = load_json(FILES["users"])
    for user in users:
        if user.get('nickname', '').lower() == nickname.lower():
            return user
    return None

def create_user(nickname, password, telegram_id=None):
    users = load_json(FILES["users"])
    for user in users:
        if user.get('nickname', '').lower() == nickname.lower():
            return None, "Пользователь существует"
    new_user = {
        'id': len(users) + 1,
        'nickname': nickname,
        'password_hash': generate_password_hash(password),
        'telegram_id': telegram_id,
        'role': 'stalker',
        'created_at': time.time(),
        'status': 'active'
    }
    users.append(new_user)
    save_json(FILES["users"], users)
    return new_user, None

def add_admin(target_id, role, added_by):
    admins = load_json(FILES["admins"])
    for admin in admins:
        if admin.get('id') == target_id:
            admin['role'] = role
            admin['added_by'] = added_by
            admin['status'] = 'active'
            save_json(FILES["admins"], admins)
            return False
    admins.append({
        'id': target_id,
        'role': role,
        'added_by': added_by,
        'status': 'active',
        'added_at': time.time()
    })
    save_json(FILES["admins"], admins)
    return True

def remove_admin(target_id):
    admins = load_json(FILES["admins"])
    admins = [a for a in admins if a.get('id') != target_id]
    save_json(FILES["admins"], admins)

def ban_user(user_id, duration_days):
    bans = load_json(FILES["bans"])
    if duration_days == -1:
        bans[str(user_id)] = -1
    else:
        bans[str(user_id)] = time.time() + (duration_days * 24 * 60 * 60)
    save_json(FILES["bans"], bans)

def unban_user(user_id):
    bans = load_json(FILES["bans"])
    if str(user_id) in bans:
        del bans[str(user_id)]
    save_json(FILES["bans"], bans)

# ================= ЭКРАНИРОВАНИЕ =================
def escape_markdown(text):
    if text is None:
        return ""
    text = str(text)
    chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in chars:
        text = text.replace(char, f'\\{char}')
    return text

# ================= ПРОВЕРКА ПРАВ В ГРУППЕ =================
async def check_admin_rights(chat_id=ADMIN_GROUP_ID):
    try:
        member = await bot.get_chat_member(chat_id=chat_id, user_id=bot.id)
        return member.status in ['administrator', 'creator']
    except:
        return False

# ================= КЛАВИАТУРЫ =================
def get_reg_keyboard():
    kb = [[KeyboardButton(text="📤 Отправить")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

def get_role_keyboard():
    kb = [
        [InlineKeyboardButton(text="🎒 Сталкер", callback_data="role_stalker")],
        [InlineKeyboardButton(text="❄️ Зимник", callback_data="role_winter")],
        [InlineKeyboardButton(text="🏢 Руфер", callback_data="role_roofer")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_main_menu_keyboard(user_id):
    kb = [
        [InlineKeyboardButton(text="📝 Регистрация", callback_data="start_register")],
        [InlineKeyboardButton(text="🗺️ Открыть карту", web_app={"url": "https://твоя-ссылка.onrender.com"})],
        [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")]
    ]
    if is_admin(user_id):
        kb.insert(0, [InlineKeyboardButton(text="🛡 Админ-панель", callback_data="admin_panel")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_admin_panel_keyboard(user_id):
    role = get_user_role(user_id)
    kb = [
        [InlineKeyboardButton(text="📋 Проверка регистраций", callback_data="check_users")],
        [InlineKeyboardButton(text="👥 Добавить админа/модера", callback_data="add_admin_start")]
    ]
    if role in ['admin']:
        kb.append([InlineKeyboardButton(text="📊 Список админов", callback_data="admin_list")])
    kb.append([InlineKeyboardButton(text="🔙 В меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_admin_keyboard(user_id):
    kb = [
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"admin_accept:{user_id}"),
            InlineKeyboardButton(text="❌ Отклонить", callback_data=f"admin_reject:{user_id}")
        ],
        [
            InlineKeyboardButton(text="🔨 Забанить", callback_data=f"admin_ban_menu:{user_id}"),
            InlineKeyboardButton(text="🕊️ Разбанить", callback_data=f"admin_unban:{user_id}")
        ],
        [InlineKeyboardButton(text="🔙 Отмена", callback_data=f"admin_cancel:{user_id}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_ban_duration_keyboard(user_id):
    kb = [
        [
            InlineKeyboardButton(text="1 день", callback_data=f"ban_time:1:{user_id}"),
            InlineKeyboardButton(text="7 дней", callback_data=f"ban_time:7:{user_id}")
        ],
        [InlineKeyboardButton(text="Навсегда", callback_data=f"ban_time:-1:{user_id}")],
        [InlineKeyboardButton(text="🔙 Отмена", callback_data=f"admin_cancel:{user_id}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_add_admin_role_keyboard(target_id):
    kb = [
        [InlineKeyboardButton(text="👑 Админ", callback_data=f"set_role_admin:{target_id}")],
        [InlineKeyboardButton(text="🛡️ Модератор", callback_data=f"set_role_moderator:{target_id}")],
        [InlineKeyboardButton(text="🔙 Отмена", callback_data=f"admin_cancel_add:{target_id}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

# ================= ОБРАБОТЧИКИ БОТА =================
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    if is_banned(message.from_user.id):
        await message.answer("🚫 Вы заблокированы администрацией.")
        return
    await message.answer(
        "👋 Привет! Это бот для сообщества сталкеров.\n\n"
        "🗺️ **Карта заброшек:**\n"
        "Добавляй объекты, смотри карту, общайся!\n\n"
        "Нажми кнопку ниже:",
        reply_markup=get_main_menu_keyboard(message.from_user.id),
        parse_mode="Markdown"
    )
    await state.clear()

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📖 **Помощь**\n\n"
        "📝 **Регистрация:**\n"
        "1. Нажми /start\n"
        "2. Выбери 'Регистрация'\n"
        "3. Придумай ник и пароль\n"
        "4. Эти данные для входа на сайт!\n\n"
        "🗺️ **Карта:**\n"
        "• Добавляй объекты с координатами\n"
        "• Отмечай опасности\n"
        "• Смотри заброшки\n\n"
        "🔧 **Для админов:**\n"
        "• /admin - панель администратора\n"
        "• /check - статистика",
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "start_register")
async def start_register_handler(callback: types.CallbackQuery, state: FSMContext):
    if is_banned(callback.from_user.id):
        await callback.answer("🚫 Вы заблокированы.", show_alert=True)
        return
    
    users = load_json(FILES["users"])
    for user in users:
        if user.get('telegram_id') == callback.from_user.id:
            await callback.answer("✅ Вы уже зарегистрированы!", show_alert=True)
            return
    
    await callback.message.answer(
        "📝 **Регистрация**\n\n"
        "1️⃣ **Придумай никнейм**\n"
        "Минимум 3 символа:",
        parse_mode="Markdown"
    )
    await callback.answer()
    await state.set_state(RegForm.nick)

@dp.message(RegForm.nick)
async def process_nick(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer("❌ Минимум 3 символа:")
        return
    await state.update_data(nick=message.text)
    await message.answer(
        "✅ Ник принят!\n\n"
        "2️⃣ **Придумай пароль**\n"
        "Минимум 4 символа:\n"
        "⚠️ Запомни его! Это для входа на сайт!"
    )
    await state.set_state(RegForm.password)

@dp.message(RegForm.password)
async def process_password(message: types.Message, state: FSMContext):
    if len(message.text) < 4:
        await message.answer("❌ Минимум 4 символа:")
        return
    await state.update_data(password=message.text)
    await message.answer(
        "✅ Пароль сохранён!\n\n"
        "3️⃣ **Кто ты?**",
        reply_markup=get_role_keyboard()
    )
    await state.set_state(RegForm.role)

@dp.callback_query(RegForm.role, F.data.startswith("role_"))
async def process_role(callback: types.CallbackQuery, state: FSMContext):
    role = callback.data.split("_")[1]
    role_names = {"stalker": "Сталкер", "winter": "Зимник", "roofer": "Руфер"}
    await state.update_data(role=role_names[role])
    
    data = await state.get_data()
    user_id = callback.from_user.id
    
    # Создаём пользователя
    user, error = create_user(data['nick'], data['password'], user_id)
    
    if error:
        await callback.message.answer(f"❌ Ошибка: {error}")
        await state.clear()
        return
    
    # Сохраняем дополнительные данные
    users = load_json(FILES["users"])
    for u in users:
        if u.get('id') == user['id']:
            u['role_choice'] = role_names[role]
            break
    save_json(FILES["users"], users)
    
    await callback.message.answer(
        f"✅ **Регистрация завершена!**\n\n"
        f"👤 **Ник:** `{data['nick']}`\n"
        f"🎒 **Роль:** {role_names[role]}\n\n"
        f"🔐 **Эти данные для входа на сайт!**\n"
        f"Открой карту в меню.",
        parse_mode="Markdown"
    )
    
    # Уведомляем админов
    admin_text = (
        f"🆕 **Новый пользователь!**\n\n"
        f"👤 **ID:** `{user_id}`\n"
        f"🏷 **Ник:** {escape_markdown(data['nick'])}\n"
        f"🎒 **Роль:** {escape_markdown(role_names[role])}"
    )
    
    try:
        await bot.send_message(
            chat_id=ADMIN_GROUP_ID,
            text=admin_text,
            parse_mode="Markdown"
        )
    except:
        pass
    
    await state.clear()
    await callback.answer()

# ================= АДМИН ПАНЕЛЬ =================
@dp.callback_query(F.data == "admin_panel")
async def admin_panel_handler(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав", show_alert=True)
        return
    await callback.message.edit_text(
        "🛡 **Панель администратора**\n\n"
        f"Ваша роль: `{get_user_role(callback.from_user.id)}`",
        parse_mode="Markdown",
        reply_markup=get_admin_panel_keyboard(callback.from_user.id)
    )
    await callback.answer()

@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "👋 Главное меню:",
        reply_markup=get_main_menu_keyboard(callback.from_user.id)
    )
    await callback.answer()

# ================= ДОБАВЛЕНИЕ АДМИНА =================
@dp.callback_query(F.data == "add_admin_start")
async def add_admin_start_handler(callback: types.CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав", show_alert=True)
        return
    await callback.message.answer(
        "👥 **Добавление админа/модератора**\n\n"
        "Отправь ID пользователя:",
        parse_mode="Markdown"
    )
    await callback.answer()
    await state.set_state(AddAdminForm.user_id)

@dp.message(AddAdminForm.user_id)
async def process_add_admin_id(message: types.Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        await message.answer("❌ Нет прав")
        return
    try:
        target_id = int(message.text.strip())
    except:
        await message.answer("❌ Неверный ID:")
        return
    await state.update_data(target_id=target_id)
    await message.answer(
        f"✅ ID: `{target_id}`\n\nВыбери роль:",
        parse_mode="Markdown",
        reply_markup=get_add_admin_role_keyboard(target_id)
    )
    await state.set_state(AddAdminForm.role)

@dp.callback_query(AddAdminForm.role, F.data.startswith("set_role_"))
async def process_add_admin_role(callback: types.CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав", show_alert=True)
        return
    parts = callback.data.split(":")
    role = parts[1]
    target_id = int(parts[2])
    
    if not is_super_admin(callback.from_user.id) and role == 'admin':
        await callback.answer("❌ Только супер-админ!", show_alert=True)
        return
    
    is_new = add_admin(target_id, role, callback.from_user.id)
    
    await callback.message.answer(
        f"✅ **{'Добавлен' if is_new else 'Обновлён'}!**\n\n"
        f"ID: `{target_id}`\nРоль: `{role}`",
        parse_mode="Markdown"
    )
    
    try:
        await bot.send_message(
            target_id,
            f"🎉 **Вас назначили!**\n\nРоль: `{role}`",
            parse_mode="Markdown"
        )
    except:
        pass
    
    await state.clear()
    await callback.answer()

@dp.callback_query(F.data.startswith("admin_cancel_add"))
async def cancel_add_admin(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        "🛡 **Панель администратора**",
        reply_markup=get_admin_panel_keyboard(callback.from_user.id)
    )
    await callback.answer()

# ================= АДМИН ДЕЙСТВИЯ =================
@dp.callback_query(F.data.startswith("admin_"))
async def admin_actions(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав", show_alert=True)
        return
    
    parts = callback.data.split(":")
    if len(parts) < 2:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    try:
        action = parts[0].replace("admin_", "")
        user_id = int(parts[1])
    except:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    await callback.answer()

    if action == "accept":
        await callback.message.edit_text(f"{callback.message.text}\n\n✅ **ПРИНЯТ**", parse_mode="Markdown")
    elif action == "reject":
        await callback.message.edit_text(f"{callback.message.text}\n\n❌ **ОТКЛОНЕН**", parse_mode="Markdown")
    elif action == "ban_menu":
        await callback.message.edit_reply_markup(reply_markup=get_ban_duration_keyboard(user_id))
    elif action == "unban":
        unban_user(user_id)
        try:
            await bot.send_message(user_id, "🕊️ **Разблокирован!**")
        except:
            pass
        await callback.answer("✅ Разбанен")
    elif action == "cancel":
        await callback.message.edit_reply_markup(reply_markup=get_admin_keyboard(user_id))

@dp.callback_query(F.data.startswith("ban_time"))
async def ban_duration_handler(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав", show_alert=True)
        return
    
    parts = callback.data.split(":")
    if len(parts) < 3:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    try:
        days = int(parts[1])
        user_id = int(parts[2])
    except:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    ban_user(user_id, days)
    days_text = "Навсегда" if days == -1 else f"{days} дн."
    
    try:
        await bot.send_message(user_id, f"🚫 **Бан на {days_text}.**")
    except:
        pass
    
    await callback.answer(f"Забанен на {days_text}")

# ================= ВЕБ-СЕРВЕР (API) =================
async def validate_telegram_data(data, token):
    received_hash = data.pop('hash', None)
    if not received_hash:
        return False
    data_check_arr = []
    for key in sorted(data.keys()):
        data_check_arr.append(f"{key}={data[key]}")
    data_check_string = "\n".join(data_check_arr)
    secret_key = hashlib.sha256(token.encode()).digest()
    hash_check = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    return hash_check == received_hash

async def handle_auth(request):
    """Вход через Telegram"""
    try:
        data = await request.post()
        auth_data = dict(data)
        if not await validate_telegram_data(auth_data, TOKEN):
            return web.json_response({"success": False, "error": "Invalid auth"}, status=401)
        
        telegram_id = int(auth_data.get('id'))
        users = load_json(FILES["users"])
        user = next((u for u in users if u.get('telegram_id') == telegram_id), None)
        
        if not user:
            return web.json_response({"success": False, "needRegister": True})
        
        if is_banned(telegram_id):
            return web.json_response({"success": False, "error": "Banned"})
        
        return web.json_response({
            "success": True,
            "user": {
                "id": user['id'],
                "nickname": user['nickname'],
                "role": user.get('role', 'stalker'),
                "telegram_id": telegram_id
            }
        })
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_login(request):
    """Вход по нику/паролю"""
    try:
        data = await request.json()
        nickname = data.get('nickname')
        password = data.get('password')
        
        user = get_user_by_nickname(nickname)
        if not user:
            return web.json_response({"success": False, "error": "Пользователь не найден"}, status=404)
        
        if not check_password_hash(user['password_hash'], password):
            return web.json_response({"success": False, "error": "Неверный пароль"}, status=401)
        
        if is_banned(user.get('telegram_id', user['id'])):
            return web.json_response({"success": False, "error": "Заблокирован"}, status=403)
        
        return web.json_response({
            "success": True,
            "user": {
                "id": user['id'],
                "nickname": user['nickname'],
                "role": user.get('role', 'stalker')
            }
        })
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_register(request):
    """Регистрация на сайте"""
    try:
        data = await request.json()
        nickname = data.get('nickname')
        password = data.get('password')
        
        user, error = create_user(nickname, password)
        if error:
            return web.json_response({"success": False, "error": error}, status=400)
        
        return web.json_response({
            "success": True,
            "user": {
                "id": user['id'],
                "nickname": user['nickname'],
                "role": 'stalker'
            }
        })
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_objects_get(request):
    """Получить объекты"""
    objects = load_json(FILES["objects"])
    return web.json_response({"success": True, "objects": objects})

async def handle_objects_post(request):
    """Добавить объект"""
    try:
        data = await request.json()
        user_id = data.get('user_id')
        
        if not user_id:
            return web.json_response({"success": False, "error": "Нет авторизации"}, status=401)
        
        objects = load_json(FILES["objects"])
        new_object = {
            "id": len(objects) + 1,
            "title": data.get('title'),
            "category": data.get('category'),
            "lat": data.get('lat'),
            "lng": data.get('lng'),
            "description": data.get('description'),
            "difficulty": data.get('difficulty'),
            "photos": data.get('photos', []),
            "status": "pending" if not is_moderator(user_id) else "approved",
            "author_id": user_id,
            "author_name": data.get('author_name'),
            "created_at": time.time()
        }
        objects.append(new_object)
        save_json(FILES["objects"], objects)
        
        return web.json_response({"success": True, "object": new_object})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_moderate_object(request):
    """Модерация объекта"""
    try:
        data = await request.json()
        user_id = data.get('user_id')
        
        if not is_moderator(user_id):
            return web.json_response({"success": False, "error": "Нет прав"}, status=403)
        
        objects = load_json(FILES["objects"])
        object_id = data.get('object_id')
        
        for obj in objects:
            if obj.get('id') == object_id:
                obj['status'] = data.get('status')
                if data.get('description'):
                    obj['description'] = data.get('description')
                if data.get('difficulty'):
                    obj['difficulty'] = data.get('difficulty')
                break
        
        save_json(FILES["objects"], objects)
        return web.json_response({"success": True})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_reviews_get(request):
    """Получить отзывы"""
    object_id = request.query.get('object_id')
    reviews = load_json(FILES["reviews"])
    if object_id:
        reviews = [r for r in reviews if r.get('object_id') == int(object_id)]
    return web.json_response({"success": True, "reviews": reviews})

async def handle_reviews_post(request):
    """Добавить отзыв"""
    try:
        data = await request.json()
        reviews = load_json(FILES["reviews"])
        new_review = {
            "id": len(reviews) + 1,
            "object_id": data.get('object_id'),
            "user_id": data.get('user_id'),
            "user_name": data.get('user_name'),
            "content": data.get('content'),
            "password": data.get('password'),  # Опционально
            "created_at": time.time()
        }
        reviews.append(new_review)
        save_json(FILES["reviews"], reviews)
        return web.json_response({"success": True})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_upload(request):
    """Загрузка фото"""
    try:
        reader = await request.multipart()
        field = await reader.next()
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join(UPLOAD_DIR, filename)
        
        with open(filepath, 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                f.write(chunk)
        
        return web.json_response({"success": True, "filename": filename})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def handle_static(request):
    file_path = os.path.join("static", request.path.strip("/"))
    if not os.path.exists(file_path):
        file_path = os.path.join("static", "index.html")
    return web.FileResponse(file_path)

async def on_startup(app):
    await bot.set_webhook("")
    is_admin = await check_admin_rights(ADMIN_GROUP_ID)
    if is_admin:
        logging.info(f"✅ Бот - админ в группе {ADMIN_GROUP_ID}")
    logging.info(f"👑 Супер-админ ID: {SUPER_ADMIN_ID}")
    print(f"🌐 Сервер запущен на http://localhost:{WEB_SERVER_PORT}")

async def on_shutdown(app):
    await bot.close()

async def main():
    app = web.Application()
    
    # API routes
    app.router.add_post('/api/auth', handle_auth)
    app.router.add_post('/api/login', handle_login)
    app.router.add_post('/api/register', handle_register)
    app.router.add_get('/api/objects', handle_objects_get)
    app.router.add_post('/api/objects', handle_objects_post)
    app.router.add_post('/api/moderate', handle_moderate_object)
    app.router.add_get('/api/reviews', handle_reviews_get)
    app.router.add_post('/api/reviews', handle_reviews_post)
    app.router.add_post('/api/upload', handle_upload)
    
    # Static files
    app.router.add_get('/{path:.*}', handle_static)
    
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", WEB_SERVER_PORT)
    await site.start()
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("🤖 Бот запущен...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Остановлен")
