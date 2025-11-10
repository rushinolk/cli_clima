import os
import requests
from dotenv import load_dotenv

load_dotenv()

def buscar_coordenadas (cidade:str)-> list:
    geocoding_api_url = os.environ.get('GEOCODING_API_URL')
    params = {
        "name": f"{cidade}",
        "count":1
    }

    response = requests.get(geocoding_api_url,params=params)
    raw_data = response.json()
    results = raw_data['results']

    return results


def buscar_previsao(lat:float,long:float) -> dict:
    previsao_api_url = os.environ.get('FORECAST_API_URL')
    params_previsao = {
        "latitude": float(lat),
        "longitude": float(long),
        "daily":"temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone":"America/Sao_Paulo",
        'forecast_days':1
    }

    previsao_response = requests.get(previsao_api_url,params=params_previsao,timeout=10)
    previsao_raw = previsao_response.json()
    previsao_daily = previsao_raw['daily']

    return previsao_daily


if __name__ == '__main__':
    
    # Definindo cidade
    cidade = input("Digite sua cidade: ").lower()

    # Buscando coordenadas
    coordenadas = buscar_coordenadas(cidade)
    long = coordenadas[0]['longitude']
    lat = coordenadas[0]['latitude']


    # Buscando previsão
    previsao = buscar_previsao(lat,long)
    dia = previsao['time'][0]
    min = previsao['temperature_2m_min'][0]
    max = previsao['temperature_2m_max'][0]


    print("\n\n____Previsão do tempo____")
    print(f"Cidade: {cidade}")
    print(f"data: {dia}")
    print(f"temperatura_min: {min}")
    print(f"temperatura_max: {max}\n\n")

    