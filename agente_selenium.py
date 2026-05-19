import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Importación de las funciones del agente y utilidades
from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
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