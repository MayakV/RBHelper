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