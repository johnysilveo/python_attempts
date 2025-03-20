import requests

API_KEY = "your_openweather_api_key"  # Replace with your API key
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

if response["cod"] == 200:
    print(f"Weather in {city}: {response['weather'][0]['description'].capitalize()}")
    print(f"Temperature: {response['main']['temp']}°C")
else:
    print("City not found!")