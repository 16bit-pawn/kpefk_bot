import telebot
from telebot import types

bot = telebot.TeleBot("6357449192:AAE046BvpaaUdeTIVIW2GcPL0zOv4Mr01Lo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    main_menu(message.chat.id, message.chat.first_name, True, message)

@bot.callback_query_handler(func=lambda call: call.data == 'vse_pro_vstup')
def vse_pro_vstup(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Етапи вступної кампанії", callback_data="admission_steps"),
        types.InlineKeyboardButton("Документи для вступу", callback_data="admission_docs")
    )
    markup.row(types.InlineKeyboardButton("Вимоги до мотиваційного листа", url="https://kpefk.com.ua/docs/vstoop/vymogy_motyvaciini_lysty_2024.pdf"))
    markup.row(types.InlineKeyboardButton("Програма вступних випробувань", callback_data="entrance_exam_program"))
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"))
    bot.edit_message_text(
        "Привіт, майбутній фаховий молодший бакалавр 👋🏻\nДізнайся більше про коледж та вступ на навчання до нього\nОберай те, що тебе цікавить:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'entrance_exam_program')
def entrance_exam_program(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("на основі 9 класів", callback_data="entrance_exam_program_9_class"),
        types.InlineKeyboardButton("на основі 11 класів", callback_data="entrance_exam_program_11_class")
    )
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="vse_pro_vstup"))
    bot.edit_message_text("Виберіть на основі якої освіти ви плануєте вступати?",
        call.message.chat.id,
        call.message.message_id, 
        reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'entrance_exam_program_9_class')
def entrance_exam_program_9_class(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Українська мова", url="https://kpefk.com.ua/docs/vstoop/pvv/prog_ua-9-2024.pdf"),
        types.InlineKeyboardButton("Математика", url="https://kpefk.com.ua/docs/vstoop/pvv/prog_math-9-2024.pdf")
    )
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="entrance_exam_program"))
    bot.edit_message_text("Виберіть освітній компонент який Вас цікавить",
        call.message.chat.id,
        call.message.message_id, 
        reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'entrance_exam_program_11_class')
def entrance_exam_program_11_class(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Українська мова", url="https://kpefk.com.ua/docs/vstoop/pvv/prog_ua-11-2024.pdf"),
        types.InlineKeyboardButton("Математика", url="https://kpefk.com.ua/docs/vstoop/pvv/prog_math-11-2024.pdf")
    )
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="entrance_exam_program"))
    bot.edit_message_text("Виберіть освітній компонент який Вас цікавить",
        call.message.chat.id,
        call.message.message_id, 
        reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'admission_steps')
def admission_steps(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("на основі 9 класів", callback_data="admission_steps_9_class"),
        types.InlineKeyboardButton("на основі 11 класів", callback_data="admission_steps_11_class")
    )
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="vse_pro_vstup"))
    bot.send_message(call.message.chat.id, "Виберіть на основі якої освіти ви плануєте вступати?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'admission_steps_9_class')
def admission_steps_9_class(call):
    with open('./9_class.png', 'rb') as photo:
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="admission_steps"))
        bot.send_photo(
            call.message.chat.id,
            photo,
            caption="🧑‍🎓 Етапи вступної кампанії на основі 9 класів (БСО)",
            reply_markup=markup
        )

@bot.callback_query_handler(func=lambda call: call.data == 'admission_steps_11_class')
def admission_steps_11_class(call):
    with open('./11_class.png', 'rb') as photo:
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="admission_steps"))
        bot.send_photo(
            call.message.chat.id,
            photo,
            caption="🧑‍🎓 Етапи вступної кампанії на основі 11 класів (ПЗСО)",
            reply_markup=markup
        )

@bot.callback_query_handler(func=lambda call: call.data == 'admission_docs')
def admission_docs(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="vse_pro_vstup"))
    bot.edit_message_text(
        "У 2024 році подача документів на навчання фахового молодшого бакалавра відбуватиметься через E-кабінет (https://vstup.edbo.gov.ua/).\n\n"
        "В який необхідно завантажити такі документи:\n\n"
        "» дані документа, що посвідчує особу;\n\n"
        "» документ про раніше здобуту освіту;\n\n"
        "» за бажанням результати НМТ (2022р.,2023р.,2024р.) / ЗНО (2021р.,) ( на основі 11 класів, заочна форма);\n\n"
        "» кольорове фото розміром 3 х 4 см (у вигляді файлу розміром до 1Мб);\n\n"
        "» мотиваційний лист;\n\n"
        "» дані (копії) документів, які дають право на пільги при вступі.",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'payment_info')
def payment_info(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"))
    bot.edit_message_text(
        "Цікавить вартість навчання на контрактній формі ? 🤷‍♂️\n\n"
        "Спеціальність 133(Галузеве машинобудування) -\tЗа рік - 16000\n"
        "Спеціальність 274(Автомобільний транспорт) -\tЗа рік - 18000\n"
        "Спеціальність 071(Облік і оподаткування) -\tЗа рік - 18000\n"
        "Спеціальність 073(Менеджмент) -\tЗа рік - 18000\n"
        "Спеціальність 122(Комп'ютерні науки) -\tЗа рік - 20000\n"
        "Спеціальність 275(Транспортні технології 275.03 на автомобільному транспорті) -\tЗа рік - 20000\n\n",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'contacts')
def contacts(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"))
    bot.edit_message_text(
        "Маєш питання стосовно вступу або потребуєш консультації ? 🤯\n\n"
        "Звертайся до приймальної комісії:\n📞 Тел./Viber/Telegram: +38 (093) 322-09-28\nабо телефонуй до нас за номером:  📞 +38 (03352) 4-97-37",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'social_networks')
def social_networks(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Нш сайт", url="https://kpefk.com.ua"),
        types.InlineKeyboardButton("Telegram", url="https://t.me/kpefk")
    )
    markup.row(
        types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/kpefk_lntu/"),
        types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/kpefklntu")
    )
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"))
    bot.edit_message_text(
        "Щоб ближче познайомитись з ВСП \"КПЕФК ЛНТУ\" приєднуйся до нас в соціальних мережах 🥰",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def main_menu(call):
    main_menu(call.message.chat.id, call.message.chat.first_name, False, call)

@bot.callback_query_handler(func=lambda call: call.data == 'specialties')
def specialties(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("Спеціальність 133 (Галузеве машинобудування)", url="https://kpefk.com.ua/structure/nashi-specialnosti/galuzeve-mashinobuduvannya/"))
    markup.row(types.InlineKeyboardButton("Спеціальність 274 (Автомобільний транспорт)", url="https://kpefk.com.ua/structure/nashi-specialnosti/avtomobilnij-transport/"))
    markup.row(types.InlineKeyboardButton("Спеціальність 071 (Облік і оподаткування)", url="https://kpefk.com.ua/structure/nashi-specialnosti/oblik-i-opodatkuvannya/"))
    markup.row(types.InlineKeyboardButton("Спеціальність 073 (Менеджмент)", url="https://kpefk.com.ua/structure/nashi-specialnosti/menedzhment/"))
    markup.row(types.InlineKeyboardButton("Спеціальність 122 (Комп'ютерні науки)", url="https://kpefk.com.ua/structure/nashi-specialnosti/kompyuterni-nauki/"))
    markup.row(types.InlineKeyboardButton("Спеціальність 275 (Транспортні технології)", url="https://kpefk.com.ua/structure/nashi-specialnosti/transportni-texnologiї/"))
    markup.row(types.InlineKeyboardButton("⬅️ Назад", callback_data="main_menu"))
    bot.edit_message_text(
        "Вибери спеціальність, з якою хочеш познайомитись детальніше 🤓",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

def main_menu(chat_id, first_name, new_message, call=None):
    welcome_message = f"Привіт 👋, {first_name}, я допоможу тобі обрати найкращу спеціальність у ВСП \"КПЕФК ЛНТУ\" 👻"
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("#Все_про_вступ", callback_data="vse_pro_vstup"),
        types.InlineKeyboardButton("Плата за навчання 💸", callback_data="payment_info")
    )
    markup.row(types.InlineKeyboardButton("Наші спеціальності 🎓", callback_data="specialties"))
    markup.row(
        types.InlineKeyboardButton("Контакти ☎️", callback_data="contacts"),
        types.InlineKeyboardButton("Соціальні мережі 💙", callback_data="social_networks")
    )

    if new_message:
        bot.send_message(chat_id, welcome_message, reply_markup=markup)
    else:
        message_id = call.message.message_id if call else None
        bot.edit_message_text(welcome_message, chat_id, message_id, reply_markup=markup)

bot.polling()