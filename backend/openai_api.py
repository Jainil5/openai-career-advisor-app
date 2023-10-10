import openai
from keyfile import key
import os

openai.api_key = str(key).strip()
# os.environ["OPENAI_API_KEY"] = "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"



def generate(input):
        
        messages = []
        pre_prompt = f"""
                You are my assistant. You need to help me with suggestions and advice for my career. I will ask you questions and you need to generate 
                replies in form of a string only.  
             """
        messages.append({"role":"assistant","content":pre_prompt})

        text = str(input).strip()
        prompt = f"""
            {text} 
        """
        messages.append({"role":"user","content":prompt})
        response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages, temperature = 1)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role":"assistant" , "content":"reply"})
        print(f"Reply:{reply}")
        
        return reply