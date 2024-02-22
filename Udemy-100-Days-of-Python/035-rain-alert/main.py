import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "your key"
account_sid = "your sid"
auth_token = "your token"

weather_parameters = {
    "lat": 60.451813,
    "lon": 22.266630,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=API_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='your phone from',
        body='you message',
        to='your phone_to'
    )

    print(message.status)
