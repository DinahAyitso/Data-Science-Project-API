import requests
import os
import csv
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv("API_KEY")
city = "Nairobi,KE"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

response = requests.get(url)
data = response.json()

print("=== NAIROBI WEATHER ===")
print("Temp:", data["main"]["temp"])
print("Weather:", data["weather"][0]["description"])
print("Humidity:", data["main"]["humidity"])
print("Wind:", data["wind"]["speed"])

record = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "time": datetime.now().strftime("%H:%M:%S"),
    "temp": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"]
}

csv_file = r"C:\Users\Dinah\Documents\Data-Science-project\nairobi_weather.csv"
exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=record.keys())
    if not exists:
        w.writeheader()
    w.writerow(record)

print("Saved to", csv_file)