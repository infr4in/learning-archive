import requests
from twilio.rest import Client

FROM_NUMBER = "your from number"
TO_NUMBER = "your to number"
ACCOUNT_SID = "your sid"
AUTH_TOKEN = "your token"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "your key"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "extended_hours": "false",
    "apikey": STOCK_API_KEY,
}

NEWS_API_KEY = "your key"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# Get data from 'alphavantage'
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# Get yesterday's and the day before yesterday's closing stock price
yesterday = float(stock_data_list[0]["4. close"])
day_before_yesterday = float(stock_data_list[1]["4. close"])

# Find difference
difference = yesterday - day_before_yesterday
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# If difference percentage is greater than 5 then take news and send messages
diff_percentage = difference / yesterday * 100
if abs(diff_percentage) > 5:
    # Get first 3 articles from 'newsapi'
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"][:3]

    # Formatted articles
    articles = [(f"{STOCK_NAME}: {up_down}{diff_percentage}%\n"
                 f"Headline: {article['title']}. \n"
                 f"Brief: {article['description']}")
                for article in news_data]

    # Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
