import requests
from pprint import pprint

TOKEN = '7617005963:AAEMA5DGh7gP-Rydou4FVtq-Ut9P9_Q2Jx4'
# WEBHOOK_URL = 'https://kitobxon-marafoni.xayrli.uz/webhook/'
url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"

response = requests.get(url)
pprint(response.json())


