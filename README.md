# 🌦️ CLI de Previsão do Tempo (cli_clima)

> Um script de console (CLI) em Python que busca a previsão do tempo para qualquer cidade, consumindo duas APIs REST diferentes em cadeia.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é demonstrar a capacidade de consumir, processar e encadear APIs externas, tratando as respostas JSON e gerenciando variáveis de ambiente de forma segura.

## 🛠️ Tecnologias e Habilidades Demonstradas

* **Python 3.10+**
* **`requests`**: Para realizar chamadas HTTP (`GET`) às APIs.
* **`json`**: Para fazer o "parse" (análise) das respostas JSON.
* **`python-dotenv`**: Para carregar e gerenciar variáveis de ambiente (URLs de API) de forma segura, sem "chumbar" (hardcode) no código.
* **Type Hinting**: Para documentação e robustez do código.
* **Lógica de Engenharia**:
    * **Encadeamento de API**: O resultado da API de Geocoding (latitude/longitude) é usado como entrada para a API de Previsão.
    * **Tratamento de Erros**: Verificação se a cidade foi encontrada antes de prosseguir (o "Bug de Nárnia").

## 🚀 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [SEU_LINK_GIT]
    cd cli_clima
    ```

2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou .venv\Scripts\activate no Windows
    pip install -r requirements.txt
    ```
    *(Nota: Crie um `requirements.txt` contendo `requests` e `python-dotenv`)*

3.  Configure seu ambiente:
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione as URLs das APIs que você está usando:
    ```ini
    GEOCODING_API_URL="httpsDEC://[api-de-geocoding.com/search](https://api-de-geocoding.com/search)"
    FORECAST_API_URL="[https://api-de-previsao.com/forecast](https://api-de-previsao.com/forecast)"
    ```

4.  Execute o script:
    ```bash
    python main.py
    ```

5.  O script solicitará o nome da cidade.
