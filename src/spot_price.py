import requests

url = "https://www.elprisetjustnu.se/api/v1/prices/"
year = "2023"
month = "05"
day = "06"
price_area = "SE3"
url = f"{url}{year}/{month}-{day}_{price_area}"
def get_spot_price():
    price_today = requests.get(f"{url}.json")
    print(url)
    return price_today



today = get_spot_price()

print(today.json())