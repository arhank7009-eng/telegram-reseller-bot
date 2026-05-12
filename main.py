# ==========================================
# TELEGRAM AUTO RESELLER BOT
# QR PAYMENT + AUTO KEY DELIVERY
# ==========================================

import telebot
from telebot import types
import requests

# ==========================================
# CONFIG
# ==========================================

BOT_TOKEN = "8697358234:AAHx5aHgNn4u62Ukhupo_GbdctqWvBCDhQo"
ADMIN_ID = 7762997996

API_KEY = "7386f5665fea7a84983801e63db5ec7b"
API_URL = "https://adminpanels.shop/api/reseller_v1.php"

# QR IMAGE
QR_IMAGE = "https://i.ibb.co/6bQxY5D/sample-qr.png"

# ==========================================
# BOT START
# ==========================================

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================================
# PRODUCTS
# ==========================================

products = {

    "BR MOD FF PC VERSION": {
        "pid": "49",
        "durations": {
            "1 Day Pc Aim Silent": 100,
            "1 Day Pc Bypass + Silent": 120,
            "10 Days Pc Aim Silent": 450,
            "10 Days Pc Bypass + Silent": 500,
            "30 Days Pc Aim Silent": 1000,
            "30 Days Pc Bypass + Silent": 1200
        }
    },

    "BR MOD FF ROOT + VPHONE": {
        "pid": "67",
        "durations": {
            "1 DaYs": 80,
            "7 DaYs": 350,
            "15 DaYs": 600,
            "30 DaYs": 1000
        }
    },

    "DRIPCLIENT 8BP NONROOT": {
        "pid": "59",
        "durations": {
            "1 DaYs": 100,
            "7 DaYs": 400,
            "30 DaYs": 1200
        }
    },

    "DRIPCLIENT FF PC AIMKILL": {
        "pid": "44",
        "durations": {
            "1 DaYS PC AIMKILL": 120,
            "7 DaYS PC AIMKILL": 500,
            "15 DaYS PC AIMKILL": 800,
            "30 DaYS PC AIMKILL": 1500
        }
    },

    "DRIPCLIENT NONROOT FF": {
        "pid": "62",
        "durations": {
            "1 DaYS NONROOT": 80,
            "3 DaYS NONROOT": 150,
            "7 DaYS NONROOT": 300,
            "15 DaYS NONROOT": 500,
            "30 DaYS NONROOT": 900
        }
    },

    "DRIPCLIENT ROOT FF": {
        "pid": "63",
        "durations": {
            "1 DaYS ROOT": 100,
            "7 DaYS ROOT": 350,
            "30 DaYS ROOT": 1000
        }
    },

    "FLUORITE IOS FF PANEL": {
        "pid": "58",
        "durations": {
            "1 DAYs FluoRite FF": 200,
            "7 DAYs FluoRite FF": 700,
            "30 DAYs FluoRite FF": 2000,
            "Esgin Gbox Certificate For iOs": 1500
        }
    },

    "HAXX-CKER PRO FF ROOT + VPHONE": {
        "pid": "64",
        "durations": {
            "10 DaYs": 600
        }
    },

    "HEX BLADE FF ROOT+VPHONE": {
        "pid": "71",
        "durations": {
            "1 DaYs": 100,
            "7 DaYs": 400,
            "14 DaYs": 700,
            "30 DaYs": 1300
        }
    },

    "HG CHEATS FF NONROOT+ROOT": {
        "pid": "65",
        "durations": {
            "1 DaYs Root + Nonroot": 80,
            "7 DaYs Root+Nonroot": 300,
            "10 DaYs Root+Nonroot": 500,
            "30 DaYs Root+Nonroot": 1200
        }
    },

    "MIGUL IPHONE IOS PANEL": {
        "pid": "69",
        "durations": {
            "1 DaYs Basic": 200,
            "1 DaYs PRO": 300,
            "7 DaYs Basic": 700,
            "7 DaYs PRO": 1000,
            "30 DaYs Basic": 2000,
            "30 DaYs PRO": 3000,
            "Esgin Gbox CERTIFICATE": 1500
        }
    },

    "NEO STRIKE FF ROOT + VPHONE": {
        "pid": "70",
        "durations": {
            "1 DaYs": 80,
            "3 DaYs": 150,
            "7 DaYs": 300,
            "14 DaYs": 600
        }
    },

    "PATO TEAM FF NONROOT + ROOT": {
        "pid": "54",
        "durations": {
            "3 DaYs SaFe + Brutal": 150,
            "7 DaYs": 300,
            "7 DaYs BruTal": 350,
            "15 DaYs": 700,
            "30 DaYs": 1400
        }
    },

    "PRIME HOOK FF NONROOT": {
        "pid": "48",
        "durations": {
            "1 Days Nonroot": 70,
            "3 Days Nonroot": 130,
            "7 Days NonRoot": 250,
            "10 Days Nonroot": 400
        }
    },

    "XYZ CHEATS FF ROOT+VPHONE": {
        "pid": "66",
        "durations": {
            "3 Days": 150,
            "7 Days": 300,
            "15 Days": 700,
            "30 Days": 1400
        }
    }
}

# ==========================================
# START
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
        "🔥 WELCOME TO AUTO RESELLER BOT 🔥",
        reply_markup=markup
    )

# ==========================================
# CALLBACKS
# ==========================================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    data = call.data.split("|")

    # ======================================
    # SHOW PRODUCTS
    # ======================================

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

    # ======================================
    # SELECT PRODUCT
    # ======================================

    elif data[0] == "product":

        product_name = data[1]

        markup = types.InlineKeyboardMarkup()

        for duration, price in products[product_name]["durations"].items():

            btn = types.InlineKeyboardButton(
                f"{duration} - ₹{price}",
                callback_data=f"buy|{product_name}|{duration}"
            )

            markup.add(btn)

        bot.edit_message_text(
            f"🛒 {product_name}\n\nSelect Duration",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # ======================================
    # BUY OPTION
    # ======================================

    elif data[0] == "buy":

        product_name = data[1]
        duration = data[2]

        price = products[product_name]["durations"][duration]

        markup = types.InlineKeyboardMarkup()

        paid_btn = types.InlineKeyboardButton(
            "✅ I PAID",
            callback_data=f"paid|{product_name}|{duration}"
        )

        markup.add(paid_btn)

        caption = f"""
💸 PAYMENT DETAILS

📦 Product:
{product_name}

⏳ Duration:
{duration}

💰 Price:
₹{price}

🪙 UPI ID:
"8795734376@ybl"

⚠️ Pay And Click I PAID
"""

        bot.send_photo(
            call.message.chat.id,
            QR_IMAGE,
            caption=caption,
            reply_markup=markup
        )

    # ======================================
    # PAYMENT SUCCESS
    # ======================================

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

        # ==================================
        # SEND KEY TO USER
        # ==================================

        bot.send_message(
            call.message.chat.id,
            f"""
✅ PAYMENT SUCCESSFUL

📦 Product:
{product_name}

⏳ Duration:
{duration}

🔑 YOUR KEY:

{result}

⚠️ DO NOT SHARE YOUR KEY
"""
        )

        # ==================================
        # ADMIN LOG
        # ==================================

        bot.send_message(
            ADMIN_ID,
            f"""
🛒 NEW ORDER

👤 USER:
{call.from_user.id}

📦 PRODUCT:
{product_name}

⏳ DURATION:
{duration}

🔑 KEY:
{result}
"""
        )

# ==========================================
# RUN BOT
# ==========================================

print("Bot Started Successfully")

keep_alive()
bot.infinity_polling()
