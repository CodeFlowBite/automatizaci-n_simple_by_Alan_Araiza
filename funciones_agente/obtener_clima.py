import requests

def obtener_clima(input_user):
    
    city = input_user.lower().replace("clima", "").replace("temperatura", "").replace("en", "").replace("de", "").strip()

    try:
        response = requests.get(f"http://wttr.in/{city}?format=%t", timeout=10)

        if response.status_code == 200:
            return f"La temperatura actual en {city.title()} es de {response.text.strip()}."
        else:
            return f"No pude obtener el clima para {city.title()}. Por favor, intenta con otra ciudad."
    except requests.RequestException as e:
        return f"Error al obtener el clima: {str(e)}"