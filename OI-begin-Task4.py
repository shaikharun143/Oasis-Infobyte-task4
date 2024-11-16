import requests

# Define your OpenWeatherMap API key
API_KEY = "931f131dde3f4ae2fcbc3289fc646471"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print("Could not retrieve weather data. Please check the city name.")

def main():
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
