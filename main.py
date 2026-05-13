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

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_URL = "https://adminpanels.shop/api/reseller_v1.php"

API_KEY = os.getenv("API_KEY")

UPI_ID = "8795734376@ybl"

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN not found")

if not API_KEY:
    raise Exception("API_KEY not found")

bot = TeleBot(BOT_TOKEN, parse_mode="HTML")
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
# PRODUCTS WITH PRICE
# ==========================================

products = {

    "BR MOD FF PC VERSION": {
        "pid": "49",
        "durations": {
            "1 Day Pc Aim Silent": 99,
            "1 Day Pc Bypass + Silent": 149,
            "10 Days Pc Aim Silent": 399,
            "10 Days Pc Bypass + Silent": 499,
            "30 Days Pc Aim Silent": 799,
            "30 Days Pc Bypass + Silent": 999
        }
    },

    "BR MOD FF ROOT + VPHONE": {
        "pid": "67",
        "durations": {
            "1 DaYs": 99,
            "7 DaYs": 299,
            "15 DaYs": 499,
            "30 DaYs": 899
        }
    },

    "DRIPCLIENT 8BP NONROOT": {
        "pid": "59",
        "durations": {
            "1 DaYs": 99,
            "7 DaYs": 299,
            "30 DaYs": 799
        }
    },

    "DRIPCLIENT FF PC AIMKILL": {
        "pid": "44",
        "durations": {
            "1 DaYS PC AIMKILL": 149,
            "7 DaYS PC AIMKILL": 399,
            "15 DaYS PC AIMKILL": 699,
            "30 DaYS PC AIMKILL": 999
        }
    },

    "DRIPCLIENT NONROOT FF": {
        "pid": "62",
        "durations": {
            "1 DaYS NONROOT": 99,
            "3 DaYS NONROOT": 199,
            "7 DaYS NONROOT": 299,
            "15 DaYS NONROOT": 499,
            "30 DaYS NONROOT": 899
        }
    },

    "DRIPCLIENT ROOT FF": {
        "pid": "63",
        "durations": {
            "1 DaYS ROOT": 99,
            "7 DaYS ROOT": 299,
            "30 DaYS ROOT": 799
        }
    },

    "FLUORITE IOS FF PANEL": {
        "pid": "58",
        "durations": {
            "1 DAYs FluoRite FF": 149,
            "7 DAYs FluoRite FF": 399,
            "30 DAYs FluoRite FF": 999
        }
    },

    "HAXX-CKER PRO FF ROOT + VPHONE": {
        "pid": "64",
        "durations": {
            "10 DaYs": 499
        }
    },

    "HEX BLADE FF ROOT+VPHONE": {
        "pid": "71",
        "durations": {
            "1 DaYs": 99,
            "7 DaYs": 299,
            "14 DaYs": 499,
            "30 DaYs": 899
        }
    },

    "HG CHEATS FF NONROOT+ROOT": {
        "pid": "65",
        "durations": {
            "1 DaYs Root + Nonroot": 99,
            "7 DaYs Root+Nonroot": 299,
            "10 DaYs Root+Nonroot": 499,
            "30 DaYs Root+Nonroot": 899
        }
    },

    "MIGUL IPHONE IOS PANEL": {
        "pid": "69",
        "durations": {
            "1 DaYs Basic": 149,
            "1 DaYs PRO": 249,
            "7 DaYs Basic": 499,
            "7 DaYs PRO": 699,
            "30 DaYs Basic": 999,
            "30 DaYs PRO": 1499
        }
    },

    "NEO STRIKE FF ROOT + VPHONE": {
        "pid": "70",
        "durations": {
            "1 DaYs": 99,
            "3 DaYs": 199,
            "7 DaYs": 399,
            "14 DaYs": 699
        }
    },

    "PATO TEAM FF NONROOT + ROOT": {
        "pid": "54",
        "durations": {
            "3 DaYs SaFe + Brutal": 299,
            "7 DaYs": 499,
            "7 DaYs BruTal": 599,
            "15 DaYs": 899,
            "30 DaYs": 1499
        }
    },

    "PRIME HOOK FF NONROOT": {
        "pid": "48",
        "durations": {
            "1 Days Nonroot": 99,
            "3 Days Nonroot": 199,
            "7 Days NonRoot": 399,
            "10 Days Nonroot": 599
        }
    },

    "XYZ CHEATS FF ROOT+VPHONE": {
        "pid": "66",
        "durations": {
            "3 Days": 199,
            "7 Days": 399,
            "15 Days": 699,
            "30 Days": 1199
        }
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

    if not call.data:
        return

    data = str(call.data).split("|")

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

data = call.data.split("|")

if data[0] == "product":

    product_name = data[1]

    markup = types.InlineKeyboardMarkup()

    # DURATION BUTTONS WITH PRICE
    for duration, price in products[product_name]["durations"].items():

        btn = types.InlineKeyboardButton(
            f"{duration} - ₹{price}",
            callback_data=f"buy|{product_name}|{duration}|{price}"
        )

        markup.add(btn)

    bot.edit_message_text(
        f"📡 PRODUCT SELECTED\n\n📦 {product_name}\n\n⏳ SELECT DURATION",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
# ==========================================
# BUY
# ==========================================

elif data[0] == "buy":

    product_name = data[1]
    duration = data[2]
    price = data[3]

    markup = types.InlineKeyboardMarkup()

    paid_btn = types.InlineKeyboardButton(
    "✅ PAID",
    callback_data=f"paid|{product_name}|{duration}|{price}"
    )

    markup.add(paid_btn)

   bot.edit_message_text(
        f"""
💳 PAYMENT REQUIRED

📦 Product:
{product_name}

⏳ Duration:
{duration}

💵 Price:
₹{price}

📌 PAY ON THIS UPI:
yourupi@upi
        """,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

elif data[0] == "paid": 
    product_name = data[1]
    duration = data[2]
    price = data[3]

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
