import requests

city = input("Enter a city name")
api_key = "01b379fa6e59e84c0f1ed5ce89135f35"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
vastaus = requests.get(pyyntö).json()
print(vastaus)
