import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

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
        icon_code = data["weather"][0]["icon"]
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
            "icon_code": icon_code
        }
    else:
        return None

def display_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        temp_label.config(text=f"Temperature: {weather['temperature']}°C")
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        desc_label.config(text=f"Condition: {weather['description'].capitalize()}")
        
        # Load and display the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{weather['icon_code']}@2x.png"
        icon_response = requests.get(icon_url)
        icon_image = Image.open(io.BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo  # Store a reference to prevent garbage collection
    else:
        messagebox.showerror("Error", "Could not retrieve weather data. Please check the city name.")

# Set up the main application window
app = tk.Tk()
app.title("Weather App")

# City Entry and Labels
city_label = tk.Label(app, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=display_weather)
get_weather_button.pack()

temp_label = tk.Label(app, text="Temperature: N/A")
temp_label.pack()

humidity_label = tk.Label(app, text="Humidity: N/A")
humidity_label.pack()

desc_label = tk.Label(app, text="Condition: N/A")
desc_label.pack()

icon_label = tk.Label(app)
icon_label.pack()

app.mainloop()
