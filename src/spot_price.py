import requests
import datetime

it_today = datetime.date.today() + datetime.timedelta(days=1) 
it_today = it_today.strftime("%Y-%m-%d %H:%M")
#it_tomorrow = it_today + datetime.timedelta(days=1) 
url = "https://www.elprisetjustnu.se/api/v1/prices/"
year = "2023"
month = "05"
day = "06"
price_area = "SE3"
url = f"{url}{year}/{month}-{day}_{price_area}"
now = datetime.datetime.now()


def get_spot_price():
    
    s = requests.Session()
    price_today = s.get(f"{url}.json")
    price_today = price_today.json()

    for hour in price_today:
        
        time_start = hour["time_start"]
        time_end = hour["time_end"]
        sek_per_kwh = hour["SEK_per_kWh"] * 100


        print(time_start[11:16],time_end[11:16], "-", sek_per_kwh)

        if str(now.hour) in time_start[11:13]:
            print("dagens pris", sek_per_kwh,time_start)

    
    


get_spot_price()

now = datetime.datetime.now()
print(now.hour)
print(it_today)
#today = get_spot_price()