import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    "X-RapidAPI-Key": "e41fb42417msh9ad0dc2786e5fa6p16e150jsne7b5b7eb8cc2",
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
