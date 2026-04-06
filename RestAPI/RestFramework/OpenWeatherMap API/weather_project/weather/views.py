import requests
from django.shortcuts import render

API_KEY = "25b5944cb8a9e275a14cace2fb238f84"

def home(request):
    weather_data = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        print(data)  # 👈 DEBUG (very important)

        if response.status_code == 200 and "main" in data:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "icon": data["weather"][0]["icon"],
            }
        else:
            weather_data = {
                "error": data.get("message", "Something went wrong")
            }

    return render(request, "weather.html", {"weather": weather_data})