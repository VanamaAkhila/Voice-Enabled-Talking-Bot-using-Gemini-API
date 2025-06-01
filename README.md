
## 🔊 Voice-Enabled Talking Bot using Gemini API

This project is an intelligent, voice-enabled chatbot that leverages **Google's Gemini API** to generate human-like responses based on user input. It supports two main interaction modes:

* 🎤 **Voice Interaction** (via microphone and text-to-speech)
* 💬 **Text-Based Chat via Telegram Bot**

---

### 🧠 Features

* **Speech Recognition**: Converts spoken input to text using `speech_recognition`.
* **Text-to-Speech**: Uses `pyttsx3` to convert Gemini responses to spoken output.
* **Google Gemini 1.5 Flash**: Powers the conversational AI with high-quality, context-aware responses.
* **Telegram Bot Integration**: Users can chat with the bot directly via Telegram.
* **Multimodal Interface**: Supports both voice and text interactions for flexibility.

---

### ⚙️ Technologies Used

* Python
* [Google Generative AI SDK (Gemini)](https://ai.google.dev/gemini-api/docs/get-started/python)
* `speech_recognition` (Voice input)
* `pyttsx3` (Voice output)
* `telebot` (Telegram bot API)

---

### 🚀 How to Run

1. **Install dependencies**:

   pip install google-generativeai speechrecognition pyttsx3 pytelegrambotapi
  

2. **Set up environment variables**:
   Create a `.env` file with your keys:

   GEMINI_API_KEY=your_google_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_token
   

3. **Run voice bot**:

   python New.py

4. **Run Telegram bot**:

   python BOT1.py


---

### 📌 Use Cases

* Educational assistant
* Personal productivity/chat tool
* Voice-controlled virtual assistant
* Telegram-based conversational AI
