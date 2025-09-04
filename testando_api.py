import requests

url = "https://www.google.com"

respostas = requests.get(url)

print(respostas)
print(respostas.text)
