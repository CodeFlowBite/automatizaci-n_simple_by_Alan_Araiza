import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
driver = webdriver.Chrome(service=Service(driver_path))

driver.get("https://www.google.com")
sleep(2)
driver.get("https://hybridge.education")
sleep(2)
driver.get("https://openai.com")
sleep(2)