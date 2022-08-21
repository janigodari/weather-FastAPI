import random

def generate_icon(icon_code: str):

    icons = {
    "01d": "fa-solid fa-sun",
    "01n": "fa-solid fa-sun",
    "02d": "fa-solid fa-cloud-sun",
    "02n": "fa-solid fa-cloud-sun",
    "03d": "fa-solid fa-cloud",
    "03n": "fa-solid fa-cloud",
    "04d": "fa-solid fa-cloud",
    "04n": "fa-solid fa-cloud",
    "09d": "fa-solid fa-cloud-showers-heavy",
    "09n": "fa-solid fa-cloud-showers-heavy",
    "10d": "fa-solid fa-cloud-rain",
    "10n": "fa-solid fa-cloud-rain",
    "11d": "fa-solid fa-cloud-bolt",
    "11n": "fa-solid fa-cloud-bolt",
    "13d": "fa-solid fa-snowflake",
    "13n": "fa-solid fa-snowflake",
    "50d": "fa-solid fa-smog",
    "50n": "fa-solid fa-smog"
    }
  
    return icons[icon_code]

def city_generator():
    cities = [
        "Pogradec",
        "Tirana",
        "Jijel",
        "Saida",
        "Berlin",
        "Bucharest",
        "Tel Aviv",
        "Madrid",
        "Bari",
        "Acerno",
        "Alberoni"
    ]
    
    return cities[random.randint(0,len(cities)-1)]