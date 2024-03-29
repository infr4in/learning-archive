import requests

SHEETY_PRICES_ENDPOINT = "YOUT SHEETY PRICES ENDPOINT"
SHEETY_USERS_ENDPOINT = "YOUT USERS PRICES ENDPOINT"
TOKEN = "YOUR TOKEN"
SHEETY_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            url=SHEETY_USERS_ENDPOINT,
            headers=SHEETY_HEADERS
        )
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
