import requests

# for india indore time

latitude = 22.72
longitude = 75.85

# latitude = 48.85
# longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"


response = requests.get(url)
data = response.json()
# print(data)  # Print the entire JSON response


temperature = data["current_weather"]["temperature"]
# print(f"Temperature in Indore: {temperature}°C")
# Output: Temperature in Indore: 20.0°C


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
indore_temp = get_weather(22.72, 75.85)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"Indore: {indore_temp}°C")
