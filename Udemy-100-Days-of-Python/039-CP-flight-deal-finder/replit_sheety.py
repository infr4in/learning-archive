import requests

SHEETY_ENDPOINT = "YOUR SHEETY USERS ENDPOINT"
TOKEN = "YOUR SHEETY YOKEN"


def post_new_row(first_name, last_name, email):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)
