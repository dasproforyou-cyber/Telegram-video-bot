import os
import telebot
import yt_dlp

BOT_TOKEN = os.getenv("8113362819:AAHvdxS86fgXajwbqhmsMilVs7P1HoFqTkM")
if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN topilmadi")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "🎥 YouTube yoki Instagram link yuboring")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text.strip()

    ydl_opts = {
        "format": "mp4/best",
        "outtmpl": "video.%(ext)s",
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for f in os.listdir():
            if f.startswith("video."):
                with open(f, "rb") as v:
                    bot.send_video(message.chat.id, v)
                os.remove(f)

    except:
        bot.reply_to(message, "❌ Yuklab bo‘lmadi")

bot.infinity_polling()