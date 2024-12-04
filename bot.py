from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Функция для обработки команды /vopros
async def handle_vopros(update: Update, context: CallbackContext) -> None:
    if context.args:
        # Текст вопроса
        vopros_text = ' '.join(context.args)
        
        # Кнопки "Решен" и "Не решен"
        keyboard = [
            [
                InlineKeyboardButton("✅ Решен", callback_data="resolved"),
                InlineKeyboardButton("❌ Не решен", callback_data="not_resolved")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Отправляем вопрос с кнопками
        await update.message.reply_text(
            f"Ваш вопрос: {vopros_text}\nВыберите статус:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("Пожалуйста, напишите текст вопроса после команды /vopros.")

# Функция для обработки выбора кнопки
async def handle_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Отвечаем Telegram, что запрос обработан

    # Изменяем сообщение в зависимости от выбора
    if query.data == "resolved":
        await query.edit_message_text("Статус вопроса обновлен: ✅ Решен")
    elif query.data == "not_resolved":
        await query.edit_message_text("Статус вопроса обновлен: ❌ Не решен")

# Основная функция для запуска бота
def main():
    TOKEN = "7929287968:AAFzDNyQ3ek96X5pEQd3MYNV0WdU0F347BY"  # Ваш токен бота

    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("vopros", handle_vopros))
    application.add_handler(CallbackQueryHandler(handle_button_click))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
