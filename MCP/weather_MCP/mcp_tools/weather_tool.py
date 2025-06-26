import requests

API_KEY = "8cce8633444d67e6e02d3e6dae6dba46"

def weather(params: dict) -> dict:
    city = params.get("city")
    if not city:
        return {"error": "Missing 'city' parameter."}

    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?q={city}"
            f"&appid={API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return {"error": data.get("message", "Failed to fetch weather")}

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        return {
            "city": city,
            "temperature_celsius": temp,
            "condition": condition,
            "message": f"The weather in {city} is {condition} with {temp}°C temperature."
        }

    except Exception as e:
        return {"error": str(e)}
