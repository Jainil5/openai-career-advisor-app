import chainlit as cl
from chainlit import *
import requests


@cl.on_message
async def main(message: str):
       
       data = {"input":message}
       post = requests.post("http://127.0.0.1:5000/ask_gpt",json = data)
       response = post.json()
       answer = response["response"]
       if answer!="":
              await cl.Message(content=answer).send()
       