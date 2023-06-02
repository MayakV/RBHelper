import os
import flask

import uuid

model = "ada:ft-personal:<YOUR_MODEL_HERE>"


app = flask.Flask(__name__)

OPENAI_API_KEY = os.getenv("RBH_OpenAI_Token")
if not OPENAI_API_KEY:
    print("Please set OPENAI_API_KEY environment variable")
    exit()

TG_TOKEN = os.getenv("GeorgiaHelpBot_Token")
if not TG_TOKEN:
    print("Please set TG_TOKEN environment variable")
    exit()

# AUTH_TOKEN = os.environ.get("AUTH_TOKEN", None)
# if not AUTH_TOKEN:
#     raise ValueError("AUTH_TOKEN must be set")

# Generate random secret
# PREMIUM_SECRET = os.environ.get(
#     "PREMIUM_SECRET", uuid.uuid4())
# print(f"Bot secret: {PREMIUM_SECRET}")

# print("1")

# if __name__ == '__main__':
#    app.run()
#
#
# @app.route("/", methods=["POST", "GET"])
# def index():
#     if flask.request.method == "POST":
#         resp = flask.request.get_json()
#         msgtext = resp["message"]["text"]
#         sendername = resp["message"]["from"]["first_name"]
#         chatid = resp["message"]["chat"]["id"]
#         send_message(chatid)
#     return "Done"
#
#
# def send_message(chatid):
#     url = "https://api.telegram.org/bot{}/sendMessage".format(key)
#     payload = {
#         "text":"heyy",
#         "chat_id":chatid
#     }
#     resp = requests.get(url, params=payload)