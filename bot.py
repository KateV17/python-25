
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import TOKEN


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)+30s [%(lineno)4d] - %(message)s'
)
logging.getLogger('httpx').setLevel(logging.WARNING)
log = logging.getLogger(__name__)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """функция, которая будет на команды / hello"""
    user = update.effective_user
    log.info(f'Функция hello вызвана пользователем {user}')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """функция, которая реагтрует эхом на любое сообщение"""
    user = update.effective_user
    message = update.message
    log.info(f'Функция echo вызвана пользователем {user}\n' + ' ' * 73 + f'{message = }')
    await update.message.reply_text(f'{update.message.text}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Рассказывает, какие есть возможности у бота"""
    user = update.effective_user
    message = update.message
    log.info(f'Функция help вызвана пользователем {user}\n')
    text = [

        f'Привет, {user.first_name}',
        'Я - школьный бот, который умеет реагировать на следующие команды:',
        '/hello - отвечаю приветствием',
        '/start /help - покажу список доступных команд'
    ]
    text = '\n'.join(text)

    await update.message.reply_text(f'{text}')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello)) #регистрация обработчика
app.add_handler(CommandHandler(["help", "start"], help))
app.add_handler(MessageHandler(filters.ALL, echo))

app.run_polling()
