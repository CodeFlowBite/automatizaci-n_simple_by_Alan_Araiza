from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

def test_chatbot():
    print("Iniciando pruebas del chatbot...")

    print("\n [Prueba_1] Precio de acción de Microsoft")
    msft_price = obtener_precio_accion("precio de microsoft")
    print(f"Resultado: {msft_price}")

if __name__ == "__main__":
    test_chatbot()