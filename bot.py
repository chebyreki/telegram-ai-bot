import telebot
import requests

BOT_TOKEN = "8238824148:AAExDYUQiv1bKzDCpZ2OFQc9-yDZ-7j5nkg"
AI_KEY = "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"

bot = telebot.TeleBot(BOT_TOKEN)

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {AI_KEY}",
    "Content-Type": "application/json"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🤖 Добро пожаловать!\n\n"
        "Я AI-бот.\n"
        "Просто напиши сообщение."
    )

@bot.message_handler(func=lambda message: True)
def chat(message):
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": message.text}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        data = response.json()
        answer = data["choices"][0]["message"]["content"]
    except Exception as e:
        answer = "⚠️ Ошибка. Попробуй позже."

    bot.send_message(message.chat.id, answer)

print("✅ Бот запущен")
bot.infinity_polling()
