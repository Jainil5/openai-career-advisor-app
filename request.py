import requests

subject = input("\nEnter any subject of your choice: ")
interest = input("\nEnter any interest of your subject: ")
input = input("\nQuestion: ")

data = {
    "subject": subject,
    "interest":interest,
    "input":input
}

post = requests.post("http://127.0.0.1:5000/ask_gpt",json = data)

response = post.json()

res = response["response"]
print(f"\nResponse: {res}")