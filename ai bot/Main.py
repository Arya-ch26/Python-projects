from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
client = OpenAI(api_key=api_key)

messages=[]

def completion(message):
  global messages
  messages.append(
      {
          "role": "user",
          "content": message
      }
  )
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
  )
  reply = completion.choices[0].message.content
  print(f"jarvas: {reply}")
  messages.append(
      {
          "role": "assistant",
          "content": reply
      }
  )
  # print(f"jarvas: {messages[-1]['content']}")

if __name__ == "__main__":
  print("Jarvas: Hi I'm jarvas, how can i help you?: ")
  print("Type 'exit' to end the conversation.\n")
  while True:
    user_question = input("User: ")
    if user_question.lower() == "exit":
      print("Jarvas: Goodbye!")
      break
    else:
      completion(user_question)





