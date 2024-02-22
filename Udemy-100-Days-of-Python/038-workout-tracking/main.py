import requests
from datetime import datetime
import os

# change it
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 192
AGE = 18

# from 'https://www.nutritionix.com/business/api'
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrionix_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRIONIX_ENDPOINT, json=nutrionix_params, headers=nutrionix_headers)
result = response.json()

SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]

# from 'https://sheety.co/'
sheet_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}",
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_headers)

    print(sheet_response.text)
