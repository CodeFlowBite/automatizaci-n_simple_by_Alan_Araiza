import os
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Importación de las funciones del agente y utilidades
from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_divisas import procesar_conversion_divisas
from utils.sanitizar import sanitizar

# --- Configuración de Selenium ---
# Se utilizan opciones para ejecutar el navegador de forma silenciosa (headless)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# Simulación de un User-Agent real para evitar bloqueos por parte de algunos sitios
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')

# --- Gestión del Driver (ChromeDriver) ---
# Se utiliza webdriver-manager para descargar automáticamente el driver compatible
driver_path = ChromeDriverManager().install()

# Corrección de ruta: Algunos sistemas devuelven la ruta de un archivo de licencia en lugar del binario
if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")
    if os.path.exists(binary_path):
        driver_path = binary_path

# Asegurar que el archivo tenga permisos de ejecución (importante en sistemas Mac/Linux)
os.chmod(driver_path, 0o755)

# Inicialización del navegador Chrome con las opciones configuradas
driver = webdriver.Chrome(service=Service(driver_path), options=options)

def procesar_input_usuario(user_input: str):
    # Sanitizar la entrada del usuario para evitar problemas de seguridad
    user_input = sanitizar(user_input)

    # Aquí se pueden agregar reglas para detectar intenciones específicas
    if "precio" in user_input.lower() or "stock" in user_input.lower() or "acción" in user_input.lower():
        return obtener_precio_accion(user_input)
    elif "clima" in user_input.lower() or "tiempo" in user_input.lower() or "temperatura" in user_input.lower():
        return obtener_clima(user_input)
    elif any(keyword in user_input.lower() for keyword in ["convertir", "convierte", "transforma", "cambia", "cambiar"]):
        return procesar_conversion_divisas(user_input)
    else:
        return None

print("Agente Selenium inicializado. Listo para procesar preguntas...")

def chatbot_request(user_input: str):
    if not user_input:
        return "Chatbot: Por favor, ingresa una pregunta válida."

    # Validar una peticion de salida
    if user_input.lower() in ["salir", "adiós", "chao", "bye", "exit"]:
        driver.quit()  # Cerrar el navegador antes de salir
        return None

    respuesta = procesar_input_usuario(user_input)
    if respuesta:
        return f"Chatbot: {respuesta}"
    else:
        return "Chatbot: Lo siento, no entendí tu pregunta. Solo entiendo preguntas sobre precios de acciones, clima o conversiones de divisas."


if __name__ == "__main__":
    while True:
        try:
            user_input = input("USER: ").strip()
            if not user_input:
                continue

            respuesta = chatbot_request(user_input)
            if respuesta is None:
                print("Chatbot: ¡Hasta luego!")
                break
            else: print(respuesta)

        except KeyboardInterrupt:
            print("\nChatbot: ¡Hasta luego!")
            break

        except Exception as e:
            print(f"Chatbot: Ocurrió un error al procesar tu solicitud. Detalles: {str(e)}")
            # Cerrar el navegador al finalizar
            driver.quit()

    # Al finalizar el programa, aseguramos cerrar el navegador para liberar recursos
    driver.quit()