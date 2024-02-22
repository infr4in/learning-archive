import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "your username"
TOKEN = "your token"
GRAPH_ID = "your graph id"
headers = {
    "X-USER-TOKEN": TOKEN,
}

# -------------------- #
#  1. CREATE ACCOUNT   #
# -------------------- #

# First, you need to create an account at https://docs.pixe.la/entry/post-user
# then update USERNAME and TOKEN
#
# # user_params = {
# #     "token": TOKEN, # TOKEN = "your new token"
# #     "username": USERNAME, # USERNAME = "your new username"
# #     "agreeTermsOfService": "yes",
# #     "notMinor": "yes",
# # }
# #
# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)

# -------------------- #
#   2. CREATE GRAPH    #
# -------------------- #

# Second, you need to create graph at https://docs.pixe.la/entry/post-graph
# then update GRAPH_ID
#
# # graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# # graph_config = {
# #     "id": "your new graph id",
# #     "name": "your new graph name",
# #     "unit": "min.",
# #     "type": "int",
# #     "color": "ajisai",
# # }
# #
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)

# ----------------------- #
#  3. SEND/UPDATE/DELETE  #
# ----------------------- #


def send_data():
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": input("What's the date? (format: 'YYYYmmdd'): "),
        "quantity": input("What's the quantity? (int num): "),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    return response.text


def update_data():
    update_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                       f"{input("What's the date? (format: 'YYYYmmdd'): ")}")
    new_pixel_data = {
        "quantity": input("What's the quantity? (int num): "),
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    return response.text


def delete_data():
    delete_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                       f"{input("What's the date? (format: 'YYYYmmdd'): ")}")
    response = requests.delete(url=delete_endpoint, headers=headers)
    return response.text


actions = {
    "send": send_data,
    "update": update_data,
    "delete": delete_data,
}

is_on = True
while is_on:
    user_choice = input("What do you want to do? (SEND/UPDATE/DELETE/EXIT): ").lower()

    if user_choice == "exit":
        print("Bye 👋")
        is_on = False
    else:
        action = actions[user_choice]
        print(f"{action()}")
        print(f"You can check your graph here: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")
