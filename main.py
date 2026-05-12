# ==========================================
# TELEGRAM AUTO RESELLER BOT
# FULL AUTO API + ALL PRODUCTS VERSION
# RENDER + GITHUB READY
# ==========================================

from telebot import TeleBot, types
from flask import Flask
from threading import Thread
import requests
import os

# ==========================================
# CONFIG
# ==========================================

BOT_TOKEN = "8697358234:AAEciVbGOmJgdQqGJyDl8alMO6mCASpRbKA"

API_URL = "https://adminpanels.shop/api/reseller_v1.php"

API_KEY = "YOUR_API_KEY"

UPI_ID = "8795734376@ybl"

bot = TeleBot(BOT_TOKEN)

# ==========================================
# KEEP ALIVE FOR RENDER
# ==========================================

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Running Successfully"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==========================================
# PRODUCTS
# ==========================================

products = {

    "BR MOD FF PC VERSION": {
        "pid": "49",
        "durations": [
            "1 Day Pc Aim Silent",
            "1 Day Pc Bypass + Silent",
            "10 Days Pc Aim Silent",
            "10 Days Pc Bypass + Silent",
            "30 Days Pc Aim Silent",
            "30 Days Pc Bypass + Silent"
        ]
    },

    "BR MOD FF ROOT + VPHONE": {
        "pid": "67",
        "durations": [
            "1 DaYs",
            "7 DaYs",
            "15 DaYs",
            "30 DaYs"
        ]
    },

    "DRIPCLIENT 8BP NONROOT": {
        "pid": "59",
        "durations": [
            "1 DaYs",
            "7 DaYs",
            "30 DaYs"
        ]
    },

    "DRIPCLIENT FF PC AIMKILL": {
        "pid": "44",
        "durations": [
            "1 DaYS PC AIMKILL",
            "7 DaYS PC AIMKILL",
            "15 DaYS PC AIMKILL",
            "30 DaYS PC AIMKILL"
        ]
    },

    "DRIPCLIENT NONROOT FF": {
        "pid": "62",
        "durations": [
            "1 DaYS NONROOT",
            "3 DaYS NONROOT",
            "7 DaYS NONROOT",
            "15 DaYS NONROOT",
            "30 DaYS NONROOT"
        ]
    },

    "DRIPCLIENT ROOT FF": {
        "pid": "63",
        "durations": [
            "1 DaYS ROOT",
            "7 DaYS ROOT",
            "30 DaYS ROOT"
        ]
    },

    "FLUORITE IOS FF PANEL": {
        "pid": "58",
        "durations": [
            "1 DAYs FluoRite FF",
            "7 DAYs FluoRite FF",
            "30 DAYs FluoRite FF"
        ]
    },

    "HAXX-CKER PRO FF ROOT + VPHONE": {
        "pid": "64",
        "durations": [
            "10 DaYs"
        ]
    },

    "HEX BLADE FF ROOT+VPHONE": {
        "pid": "71",
        "durations": [
            "1 DaYs",
            "7 DaYs",
            "14 DaYs",
            "30 DaYs"
        ]
    },

    "HG CHEATS FF NONROOT+ROOT": {
        "pid": "65",
        "durations": [
            "1 DaYs Root + Nonroot",
            "7 DaYs Root+Nonroot",
            "10 DaYs Root+Nonroot",
            "30 DaYs Root+Nonroot"
        ]
    },

    "MIGUL IPHONE IOS PANEL": {
        "pid": "69",
        "durations": [
            "1 DaYs Basic",
            "1 DaYs PRO",
            "7 DaYs Basic",
            "7 DaYs PRO",
            "30 DaYs Basic",
            "30 DaYs PRO"
        ]
    },

    "NEO STRIKE FF ROOT + VPHONE": {
        "pid": "70",
        "durations": [
            "1 DaYs",
            "3 DaYs",
            "7 DaYs",
            "14 DaYs"
        ]
    },

    "PATO TEAM FF NONROOT + ROOT": {
        "pid": "54",
        "durations": [
            "3 DaYs SaFe + Brutal",
            "7 DaYs",
            "7 DaYs BruTal",
            "15 DaYs",
            "30 DaYs"
        ]
    },

    "PRIME HOOK FF NONROOT": {
        "pid": "48",
        "durations": [
            "1 Days Nonroot",
            "3 Days Nonroot",
            "7 Days NonRoot",
            "10 Days Nonroot"
        ]
    },

    "XYZ CHEATS FF ROOT+VPHONE": {
        "pid": "66",
        "durations": [
            "3 Days",
            "7 Days",
            "15 Days",
            "30 Days"
        ]
    }
}

# ==========================================
# START COMMAND
# ==========================================

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()

    btn = types.InlineKeyboardButton(
        "🛒 BUY PRODUCTS",
        callback_data="products"
    )

    markup.add(btn)

    bot.send_message(
        message.chat.id,
        """
🔥 WELCOME TO AUTO RESELLER BOT 🔥

✅ Instant Key Delivery
💳 UPI Payment Available
🛒 Premium Products Available
        """,
        reply_markup=markup
    )

# ==========================================
# CALLBACKS
# ==========================================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    data = call.data.split("|")

    if call.data == "products":

        markup = types.InlineKeyboardMarkup()

        for product in products:

            btn = types.InlineKeyboardButton(
                product,
                callback_data=f"product|{product}"
            )

            markup.add(btn)

        bot.edit_message_text(
            "📦 SELECT PRODUCT",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif data[0] == "product":

        product_name = data[1]

        markup = types.InlineKeyboardMarkup()

        for duration in products[product_name]["durations"]:

            btn = types.InlineKeyboardButton(
                duration,
                callback_data=f"buy|{product_name}|{duration}"
            )

            markup.add(btn)

        bot.edit_message_text(
            f"""
🛒 PRODUCT SELECTED

📦 {product_name}

⏳ SELECT DURATION
            """,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif data[0] == "buy":

        product_name = data[1]
        duration = data[2]

        markup = types.InlineKeyboardMarkup()

        paid_btn = types.InlineKeyboardButton(
            "✅ PAID",
            callback_data=f"paid|{product_name}|{duration}"
        )

        markup.add(paid_btn)

        bot.edit_message_text(
            f"""
💳 PAYMENT REQUIRED

📦 Product:
{product_name}

⏳ Duration:
{duration}

💰 PAY ON THIS UPI:

`{UPI_ID}`

✅ AFTER PAYMENT CLICK PAID BUTTON
            """,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=markup
        )

    elif data[0] == "paid":

        product_name = data[1]
        duration = data[2]

        pid = products[product_name]["pid"]

        payload = {
            "api_key": API_KEY,
            "action": "buy",
            "product_id": pid,
            "duration": duration
        }

        try:

            response = requests.post(
                API_URL,
                data=payload
            )

            result = response.text

        except Exception as e:

            bot.send_message(
                call.message.chat.id,
                f"❌ API ERROR\n\n{e}"
            )

            return

        bot.send_message(
            call.message.chat.id,
            f"""
✅ PAYMENT SUCCESSFUL

📦 PRODUCT:
{product_name}

⏳ DURATION:
{duration}

🔑 YOUR KEY:

{result}

🔥 THANKS FOR BUYING
            """
        )

# ==========================================
# AUTO REPLY SYSTEM
# ==========================================

@bot.message_handler(func=lambda message: True)
def auto_reply(message):

    text = message.text.lower()

    if text in ["hi", "hello", "hey", "hlo"]:

        bot.reply_to(
            message,
            """
👋 HELLO BRO

🔥 WELCOME TO AUTO RESELLER BOT

📌 TYPE /start
            """
        )

    elif "buy" in text:

        bot.reply_to(
            message,
            "🛒 TO BUY PRODUCTS TYPE /start"
        )

    elif "payment" in text:

        bot.reply_to(
            message,
            f"""
💳 PAYMENT AVAILABLE

UPI:
{UPI_ID}
            """
        )

    elif "price" in text:

        bot.reply_to(
            message,
            "💰 ALL PRICES AVAILABLE INSIDE BOT\n\nTYPE /start"
        )

    else:

        bot.reply_to(
            message,
            """
🤖 AUTO REPLY BOT

📌 TYPE /start
            """
        )

# ==========================================
# RUN BOT
# ==========================================

print("BOT RUNNING...")

keep_alive()

bot.infinity_polling()
