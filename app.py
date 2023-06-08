import os
import flask
import azure.functions as func

import uuid

# model = "ada:ft-personal:<YOUR_MODEL_HERE>"
import bot
from telebot.types import Update as Update

WEBHOOK_HOST = '<ip/host where the bot is running>'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (bot.TG_TOKEN)

app = flask.Flask(__name__)


# OPENAI_API_KEY = os.getenv("RBH_OpenAI_Token")
# if not OPENAI_API_KEY:
#     print("Please set OPENAI_API_KEY environment variable")
#     exit()
#
# TG_TOKEN = os.getenv("GeorgiaHelpBot_Token")
# if not TG_TOKEN:
#     print("Please set TG_TOKEN environment variable")
#     exit()

# AUTH_TOKEN = os.environ.get("AUTH_TOKEN", None)
# if not AUTH_TOKEN:
#     raise ValueError("AUTH_TOKEN must be set")

# Generate random secret
# PREMIUM_SECRET = os.environ.get(
#     "PREMIUM_SECRET", uuid.uuid4())
# print(f"Bot secret: {PREMIUM_SECRET}")

# print("1")


# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Hey'


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


def send_message(chatid):
    url = "https://api.telegram.org/bot{}/sendMessage".format(key)
    payload = {
        "text": "heyy",
        "chat_id": chatid
    }
    # resp = requests.get(url, params=payload)


if __name__ == "__main__":
    print("server started")
    app.run()
