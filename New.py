"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr

import os

import google.generativeai as genai

genai.configure(api_key="place_your_genai_api_key")


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


def speechToText():
  r = sr.Recognizer()
  with sr.Microphone(device_index=1) as source:
    print("Say something!")
    r.pause_threshold = 1
    audio = r.listen(source)

  print("Done")
  query = r.recognize_google(audio, language='en-in')
  response = chat_session.send_message(f"limit to 100 words\n{query}")
  engine.say(response.text)
  engine.runAndWait()
  print(f'You said: {query}\n')
  return query
speechToText()

