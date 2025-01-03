from telebot import TeleBot
from constants import TOKEN
from controllers import Controller

# Создаем экземпляр бота
bot = TeleBot(TOKEN)
controller = Controller(bot)

# Подключаем обработчики
controller.register_handlers()

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
