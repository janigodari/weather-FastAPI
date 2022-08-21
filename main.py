from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import datetime
import requests
import tools
import api_key as key

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

async def get_weather(city: str):
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
    API_KEY = key.get_api_key()
    CITY = city
    
    url = BASE_URL + "&units=metric&appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    return response

@app.get("/")
async def root():
    city = tools.city_generator()
    return RedirectResponse(f"/weather?city={city}")

@app.get("/weather:city", response_class=HTMLResponse)
async def index(request: Request, city = str):
    response = await get_weather(city)

    if response['cod'] == "404":    
        return RedirectResponse("/")

    city = response['city']['name']
    country = response['city']['country']
    current_date = datetime.datetime.today()
    description = response['list'][0]['weather'][0]['description']
    temp_min = round(response['list'][0]['main']['temp_min'])
    temp_max = round(response['list'][0]['main']['temp_max'])
    feels_like = round(response['list'][0]['main']['feels_like'])
    humidity = response['list'][0]['main']['humidity']
    wind = response['list'][0]['wind']['speed']

    temp_days = [0 for i in range(5)]
    date_days = [0 for i in range(5)]
    description_icon = [0 for i in range(5)]
    icon = [0 for i in range(5)]
    
    for i in range(5):
        temp_days[i] = round(response['list'][i]['main']['temp'])
        description_icon[i] = response['list'][i]['weather'][0]['icon']
        if i == 0: date_days[i] = datetime.datetime.today()
        else: date_days[i] = datetime.datetime.today() + datetime.timedelta(days=i+1)
    
    for i in range(5):
        icon[i] = description_icon[i]

    context = {
        "request": request, 
        "current_day": date_days[0].strftime('%A'), 
        "current_date": current_date.strftime("%d/%m/%Y"), 
        "temp": temp_days[0],
        "description": description, 
        "city": city,
        "country": country,
        "feels_like": feels_like,
        "humidity": humidity,
        "wind": wind,
        "day_2": date_days[1].strftime('%a'),
        "day_3": date_days[2].strftime('%a'),
        "day_4": date_days[3].strftime('%a'),
        "day_5": date_days[4].strftime('%a'),
        "temp_day_2": temp_days[1],
        "temp_day_3": temp_days[2],
        "temp_day_4": temp_days[3],
        "temp_day_5": temp_days[4],
        "today_weather_icon": tools.generate_icon(icon[0]),
        "day_2_weather_icon": tools.generate_icon(icon[1]),
        "day_3_weather_icon": tools.generate_icon(icon[2]),
        "day_4_weather_icon": tools.generate_icon(icon[3]),
        "day_5_weather_icon": tools.generate_icon(icon[4]),
        "temp_min": temp_min,
        "temp_max": temp_max
        }
    
    return templates.TemplateResponse("index.html", context)