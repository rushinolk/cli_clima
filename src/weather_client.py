import os
import requests
import logging
from dotenv import load_dotenv


load_dotenv()

def search_city(city:str)-> list[dict] | None:
    geocoding_api_url = os.environ.get('GEOCODING_API_URL')
    if not geocoding_api_url:
        logging.error("Variavel geocoding_api_url não definida")
        return None


    params = {"name": f"{city}","count":1}
    try:
        response = requests.get(geocoding_api_url,params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logging.error(f"Falha na conexão com API geocoding: {exc}")
        return None
    
    raw_data = response.json()
    results = raw_data.get('results') or []

    if not results:
        logging.warning(f"Nenhuma coordenada encontrada para a cidade: {city}")
        return None

    return results


def search_forecast(lat:float,long:float) -> dict | None:
    previsao_api_url = os.environ.get('FORECAST_API_URL')
    if not previsao_api_url:
        logging.error("Variavel previsao_api_url não definida")
        return None
    

    params_previsao = {
        "latitude": float(lat),
        "longitude": float(long),
        "daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone":"America/Sao_Paulo",
        'forecast_days':1
    }

    try:
        previsao_response = requests.get(previsao_api_url,params=params_previsao,timeout=10)
        previsao_response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logging.error(f"Falha na conexão com API forecast {exc}")
        return None

    previsao_raw = previsao_response.json()
    previsao_daily = previsao_raw.get('daily') or {}

    if not previsao_daily:
        logging.warning(f"Nenhuma previsão encontrada para a coordenada lat: {lat} / long: {long}")
        return None

    return previsao_daily


def get_forecast_for_city(city:str) -> dict | None:
    
    coordinates = search_city(city)

    if not coordinates:
        logging.error(f"Erro ao procurar coordenadas da cidade: {city}")
        return None

    long = coordinates[0]['longitude']
    lat = coordinates[0]['latitude']


    forecast = search_forecast(lat,long)
    if not forecast:
        logging.error(f"Nenhuma previsão encontrada para a cidade: {city}")
        return None

    return forecast