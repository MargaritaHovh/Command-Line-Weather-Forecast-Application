import requests

api_key = '03e0b73b12344958443bb248c4f83796'  # Replace with your actual API key

def get_weather(city, units='metric'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data, units='Celsius'):
    if 'main' in data and 'weather' in data and 'wind' in data:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {data['name']}:")
        print(f"Temperature: {temperature} {units}")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} meter/sec")
    else:
        print("Failed to fetch weather data. Please try again.")

def main():
    city = input("Enter the name of the city: ").capitalize()
    units = input("Choose temperature units (C for Celsius, F for Fahrenheit): ").upper()

    if units not in ['C', 'F']:
        print("Invalid choice for temperature units. Defaulting to Celsius.")
        units = 'C'

    weather_data = get_weather(city, units='metric' if units == 'C' else 'imperial')
    display_weather(weather_data, units='Celsius' if units == 'C' else 'Fahrenheit')

if __name__ == "__main__":
    main()
