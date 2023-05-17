import telegram
from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters
import requests

from displayStudio.settings import TELEGRAM_PASSWORD, TELEGRAM_TOKEN



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Добро пожаловать в служебный бот компании shutters.su! \n'
                                    f'Если вы не являетесь сотрудником, пожалуйста перейдите на сайт shutters.su для получения наших услуг\n'
                                    f'Если вы являетесь сотрудником, введите пароль в ответ на это сообщение')

async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Добро пожаловать в служебный бот компании shutters.su! \n'
                                    f'Если вы не являетесь сотрудником, пожалуйста перейдите на сайт shutters.su для получения наших услуг\n')


async def handel_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user['username']
    text: str = update.message.text
    chat_id: int = update.message.chat.id
    print(f'User_id: {chat_id}')

    if text == TELEGRAM_PASSWORD:
        # user, created = BotTrustedUsers.objects.get_or_create(name=user, user_id= chat_id)
        # user.save()
        requests.post(f'http://localhost:8000/register-telegram/{user}/{chat_id}')
        responce = 'Вы были авторизированны в системе и будете получать поступающие заявки'
    else:
        responce = 'Вы ввели неправильный пароль'

    await update.message.reply_text(responce)

# send images to user from DB
async def send(chat, msg):
    await telegram.Bot(TELEGRAM_TOKEN).sendMessage(chat_id=chat, text=msg)


if __name__ == '__main__':
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages

    app.add_handler(MessageHandler(filters.TEXT, handel_password))

    app.run_polling()