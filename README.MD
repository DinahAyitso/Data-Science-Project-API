# Nairobi Weather Data Automation

## Overview
This project is a Python-based weather data automation script that fetches real-time weather information for Nairobi using the OpenWeatherMap API. The script collects weather data such as temperature, humidity, weather description, and wind speed, then stores the data in a CSV file for tracking and analysis.

The project also includes automation through a scheduler that runs daily at 12:00 noon to continuously update the dataset.

---

## Features
- Fetches live weather data from the OpenWeatherMap API
- Stores weather data in a CSV file
- Automatically appends new weather records
- Saves:
  - Date
  - Time
  - Temperature
  - Humidity
  - Weather description
  - Wind speed
- Uses environment variables to securely store API keys
- Automated daily weather data collection

---

## Technologies Used
- Python
- Requests
- CSV
- Python-dotenv
- Datetime
- OpenWeatherMap API

---

## Project Structure

```bash
├── weather.py
├── nairobi_weather.csv
├── .env
├── requirements.txt
└── README.md
```

---

## How the Script Works
1. Loads the API key from the `.env` file
2. Connects to the OpenWeatherMap API
3. Fetches Nairobi weather data
4. Extracts important weather information
5. Saves the data into `nairobi_weather.csv`
6. Automatically updates the CSV daily at 12 noon using a scheduler

---

## Example Output

```bash
=== NAIROBI WEATHER ===
Temp: 24 °C
Weather: broken clouds
Humidity: 65%
Wind: 3.5 m/s

Data saved to nairobi_weather.csv
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd <your-project-folder>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Add your API key:

```env
API_KEY=your_api_key_here
```

---

## Run the Script

```bash
python weather.py
```

---

## CSV Data Stored

| Column | Description |
|---|---|
| date | Current date |
| time | Current time |
| temp | Temperature in °C |
| humidity | Humidity percentage |
| description | Weather condition |
| wind_speed | Wind speed in m/s |

---

## Future Improvements
- Add support for multiple cities
- Create weather visualizations using Matplotlib
- Store data in a database
- Build a dashboard using Streamlit
- Deploy the automation to the cloud

---

## Author
Dinah Ayitso