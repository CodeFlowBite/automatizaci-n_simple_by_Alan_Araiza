import re
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima as obtener_temperatura
from funciones_agente.obtener_divisas import procesar_conversion_divisas

def chatbot():
    print("*** Chatbot v1.0.0 Iniciando ***")
    print("Hola soy el chatbot v1.0.0, Puedo ayudarte a obtener información sobre precios de acciones, clima de ciudades y conversiones de divisas.")
    print("¿Qué quieres saber hoy?")

    # Ciclo infinito para mantener el chatbot corriendo
    while True:
        try:
            user_input = input("-->").strip()
            if not user_input:
                continue

            # Validar una peticion de salida
            if user_input.lower() in ["salir", "adiós", "chao", "bye", "exit"]:
                print("Chatbot: ¡Hasta luego!")
                break

            # Reglas para detectar intencion de preguntas por acciones
            stock_match = re.search(r"(?:precio|stock|acción|accion)\s+(?:de\s+)?(\w+)", user_input, re.IGNORECASE)

            # Reglas para detectar intencion de preguntas por clima
            weather_match = re.search(r"(?:clima|tiempo)\s+(?:en|de)\s+(\w+)", user_input, re.IGNORECASE)

            # Reglas para detectar intencion de preguntas por conversion de divisas
            conversion_match = re.search(r"(?:convertir|convierte|transforma|cambia|cambiar)\s+(\d+(?:\.\d+)?)\s+(\w+)\s+(?:a|en|a por|con)\s+(\w+)", user_input, re.IGNORECASE)

            #Caso 1: El usuario pregunta por acciones
            if stock_match:
                # Debemos esperar si el usario indica alguna accion
                price = obtener_precio_accion(user_input)
                if price:
                    print(f">> {price}")
                else:
                    print("Chatbot: No pude obtener el precio, ¿podrías intentar con otra acción?")

            # Caso 2: El usuario pregunta por clima
            elif weather_match:
                temp = obtener_temperatura(user_input)
                if temp:
                    print(f">> {temp}")
                else:
                    print("Chatbot: No pude obtener la temperatura, ¿podrías intentar con otra ciudad?")

            # Caso 3: El usuario pregunta por conversion de divisas
            elif conversion_match:
                resultado = procesar_conversion_divisas(user_input)
                if resultado:
                    print(f">> {resultado}")
                else:
                    print("Chatbot: No pude procesar la conversión. ¿Podrías revisar el formato?")

            # Caso 4: El usuario no ejecuta alguna peticion 
            else:
                print("Chatbot: No entendí tu petición. ¿Podrías replantearla?")
            print("\n")

        except KeyboardInterrupt:
            # Comando de salida Ctrl + C | Cmd + C
            print("\nChatbot: Hasta luego, fue un placer ayudarte")
            break


if __name__ == "__main__":
    chatbot()