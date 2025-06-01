import telebot
import google.generativeai as genai
bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


genai.configure(api_key="GEMINI_API_KEY")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
 
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hi",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hi there! How can I help you today? \n",
      ],
    },
  ]
)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Start a new chat session for each incoming message
    chat_session = model.start_chat(
        history=[
        ]
    )

    # Generate a response from GenAI based on the incoming message
    response = chat_session.send_message(message.text)

    # Print the response to console (optional)
    print(response.text)

    # Reply to the user with the generated response
    bot.reply_to(message, response.text)

# Start polling for messages
bot.infinity_polling()
