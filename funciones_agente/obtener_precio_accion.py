import yfinance as yf
from utils.sanitizar import sanitizar

# Diccionario con las empresas y sus acciones

COMPANY_TICKERS = {
    "apple": "AAPL",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "google": "GOOGL",
    "facebook": "META",
    "tesla": "TSLA",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "adobe": "ADBE",
    "intel": "INTC"
}

def obtener_precio_accion(user_input):
    company_name = sanitizar(user_input)
    ticker = COMPANY_TICKERS.get(company_name)

    # Buscar si el nombre de la empresa esta en el diccionario

    if ticker:
        try:
            stock = yf.Ticker(ticker)

            data = stock.history(period="1d")
            if not data.empty:
                price = data["Close"].iloc[-1]
                return f"El precio actual de {company_name.title()} ({ticker}) es de ${price:.2f}."
            else:
                return None

        except Exception as e:
            return f"Error al obtener el precio de la acción: {str(e)}"
    else:
        return f"No pude encontrar la acción para {company_name.title()}. Por favor, intenta con otra empresa."