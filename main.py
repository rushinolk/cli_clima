import logging
from src.weather_client import  get_forecast_for_city


logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato da mensagem
    datefmt='%Y-%m-%d %H:%M:%S', # Formato da data
    handlers=[
        logging.FileHandler("logs/pipeline.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()            # Também exibe o log no console
    ]
)

if __name__ == '__main__':
    
    # Definindo cidade
    while True:
        try:    
            menu = int(input("--------MENU--------\n\n1 - Pesquisar cidade\n0 - sair\n"))
        except ValueError as exc:
            logging.error(f"Opção invalida. Por favor digite uma opção do menu")
            continue
        
        if menu == 1:
            city = input("Digite sua cidade: ").lower()

            forecast = get_forecast_for_city(city)

            if forecast is None:
                logging.error("Não foi possivel obter previsão. Verifique o nome da cidade ou tente novamente mais tarde")
                

            day = forecast['time'][0]
            min = forecast['temperature_2m_min'][0]
            max = forecast['temperature_2m_max'][0]


            logging.info("____Previsão do tempo____")
            logging.info(f"Cidade: {city}")
            logging.info(f"data: {day}")
            logging.info(f"temperatura_min: {min}")
            logging.info(f"temperatura_max: {max}\n\n")

        elif menu == 0:
            break
        else:
            logging.error("Opção inexistente. Digite 0 ou 1.")

