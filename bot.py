import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

stocks = ["AAPL", "TSLA", "NVDA"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def get_news():
    message = "📊 Обзор рынка:\n\n"
    for stock in stocks:
        message += f"🔹 {stock} — проверить новости и тренд\n"
    return message

if __name__ == "__main__":
    news = get_news()
    send_message(news)
