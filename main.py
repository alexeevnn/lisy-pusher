from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Получаем токен и Chat ID из переменных окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["POST"])
def push():
    data = request.get_json()
    text = data.get("text", "Сообщение пустое")

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
def ping():
    return "Лисичка живёт на этом сервере."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
