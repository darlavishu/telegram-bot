from telegram.ext import ApplicationBuilder, CommandHandler
from datetime import time

TOKEN = "8777445549:AAGe7zQADcKpHC5IqhlZZwv7tcgMU-YZG_w"
CHAT_ID = 6547255197

TASKS = [
    "✅ Review Skol contract updates",
    "✅ Check Bugesera Airport scaffolding status",
    "✅ Follow up with Mota Engil",
    "✅ Review Project 1 AI emails",
    "✅ Check investment portfolio",
]

async def send_briefing(context):
    message = "☀️ *Good Morning Vish — Daily Briefing*\n\n"
    message += "\n".join(TASKS)
    message += "\n\n💪 Let's get it."
    await context.bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

async def start(update, context):
    await update.message.reply_text("Morning briefing bot active ✅")

async def test(update, context):
    message = "☀️ *Good Morning Vish — Daily Briefing*\n\n"
    message += "\n".join(TASKS)
    message += "\n\n💪 Let's get it."
    await update.message.reply_text(message, parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("test", test))
app.job_queue.run_daily(send_briefing, time=time(5, 0))  # 7am Kigali

app.run_polling()