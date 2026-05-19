import requests

def procesar_conversion_divisas(user_input: str):
    # Pasamos todo a mayúsculas para evitar problemas con 'usd' o 'usd'
    comando = user_input.upper().split()
    
    # Buscamos un formato simple basado en reglas: ["CONVERTIR", "100", "USD", "A", "MXN"]
    comandos_ceros = ["CONVERTIR", "CONVIERTE", "TRANSFORMA", "CAMBIA", "CAMBIAR"]
    comandos_a = ["A", "EN", "A POR" ,"CON"]
    if len(comando) == 5 and (comando[0] in comandos_ceros) and (comando[3] in comandos_a):
        try:
            monto = float(comando[1])
            moneda_origen = comando[2]
            moneda_destino = comando[4]
            
            # Llamada a la API de Frankfurter
            url = f"https://api.frankfurter.app/latest?amount={monto}&from={moneda_origen}&to={moneda_destino}"
            respuesta = requests.get(url, timeout=10)
            
            if respuesta.status_code == 200:
                datos = respuesta.json()
                resultado = datos["rates"][moneda_destino]
                return f"{monto} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}."
            
            elif respuesta.status_code == 404:
                return "Lo siento, no encontré alguna de esas monedas. Asegúrate de usar códigos válidos como USD, EUR, MXN, etc."
            else:
                return "Hubo un problema con el servidor de divisas. Intenta más tarde."
                
        except ValueError:
            return "Por favor, asegúrate de que el monto sea un número válido. Ejemplo: 'convertir 50 USD a EUR'"
        except Exception:
            return "Ups, algo salió mal al procesar la conversión."
            
    return None # Si el texto no coincide con la regla de conversión