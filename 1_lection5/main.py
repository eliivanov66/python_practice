# py -m venv .folder / python -m venv .folder - папка для локального экземпляра интерпритатора
# pip install <library name>
# pip install --upgrade pip Обновить pip
# файл name.txt - содержит требования библиотек для проекта например pyTelegramBotAPI==4.7.1 с локальным интерпритатором
# файл чтобы установить эти библиотеки pip install -r name.txt 

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     #time.sleep(1)
#     bar.next()
# bar.finish()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# print(emoji.is_emoji("👍"))

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Updater, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'For the Emperor {update.effective_user.first_name}')

app = Updater("5551738625:AAFE5AXjwLN0Deu7YqhZCQITpeP-YcQDQ04")
print("Emperor protects")
app.dispatcher.add_handler(CommandHandler("hello", hello))
app.start_polling()
app.idle()