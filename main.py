from flask import Flask, request
from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Telegram settings
BOT_TOKEN = "7653342813:AAHwbbcVLJpqypiejgY5FsV9FQLrDeXVQOU"
CHAT_ID = "1921885707"  # Замени на свой Telegram ID, если нужно

@app.route("/", methods=["POST"])
def handle_push():
    data = request.get_json()
    text = data.get("text", "Пустое сообщение")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        r = requests.post(telegram_url, json=payload)
        return {"ok": True, "status": r.status_code}, r.status_code
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

@app.route("/", methods=["GET"])
def health_check():
    return "Lisy-pusher is live!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
