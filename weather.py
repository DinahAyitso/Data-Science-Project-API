import requests
import os
import csv
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("API_KEY")
city = "Nairobi,KE"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("=== NAIROBI WEATHER ===")
print(f"Temp: {data['main']['temp']} °C")
print(f"Weather: {data['weather'][0]['description']}")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Wind: {data['wind']['speed']} m/s")

record = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "time": datetime.now().strftime("%H:%M:%S"),
    "temp": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"]
}

csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nairobi_weather.csv")
file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=record.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(record)

print(f"Data saved to {csv_file}") 

