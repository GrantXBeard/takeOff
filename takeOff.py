import os
import openai
openai.api_key = os.getenv("TAKEOFF_KEY")

while True:
  question = input("\033[34mWhat is your question?\n\033[0m")
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant. Answer the given question."},
      {"role": "user", "content": question}
    ]
  )
  print("\033[32m" + completion.choices[0].message.content + "\n")