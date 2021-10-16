import requests


def get_forecast(location_data):
    location = location_data['name']
    temp = round(location_data['main']['temp'], 2) - 273
    pressure = location_data['main']['pressure']
    weather = location_data['weather'][0]['main']
    weather_desc = location_data['weather'][0]['description']
    wind = location_data['wind']['speed']
    print("-" * 22)
    print(f'Location: {location}')
    print(f'Temperature: {temp} Celcius degrees')
    print(f'Pressure: {pressure} hPa')
    print(f'Weather: {weather} ({weather_desc})')
    print(f'Wind speeed: {wind} m/s')
    print("-" * 22)


def get_location(text, key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={text}&appid={key}"
    location_data = requests.get(url)
    return location_data.json()


def main():
    api_key = "f00927bf08ce68c86cbb1a262c3e173a"
    while True:
        n = 0
        city = input("Enter name of the city (in eng): ")
        location_data = get_location(city, api_key)
        n = 1
        if location_data['cod'] != 200 and n != 0:
            print("There is no such a city in our database! Try again.")
        else:
            break
    get_forecast(location_data)
    print("Do you want to check another city?")
    decision = input("Yes/No: ")
    print()
    if decision in ("yes", "YES", "Yes", "Y", "y"):
        main()
    else:
        return 0


if __name__ == "__main__":
    main()
