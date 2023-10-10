import requests


input = input("\nQuestion: ")

data = {
    "input":input
}

post = requests.post("http://127.0.0.1:5000/ask_gpt",json = data)

response = post.json()

res = response["response"]
print(f"\nResponse: {res}")