import re
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima as obtener_temperatura
from funciones_agente.obtener_divisas import procesar_conversion_divisas

def chatbot():
    print("\033[92m")  # Verde
    print("*** Chatbot v1.0.0 Iniciando ***")
    print("Hola soy el chatbot v1.0.0, Puedo ayudarte a obtener información sobre precios de acciones, clima de ciudades y conversiones de divisas.")
    print("¿Qué quieres saber hoy?")
    print("\033[0m")  # Reset

    # Ciclo infinito para mantener el chatbot corriendo
    while True:
        try:
            print("\033[91m")  # rojo
            user_input = input("USER: ").strip()
            if not user_input:
                continue
            print("\033[0m")  # Reset

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

                print("\033[92m")  # Verde
                if price:
                    # color diferente para el chatbot
                    print(f"Chatbot: {price}")
                else:
                    print("Chatbot: No pude obtener el precio, ¿podrías intentar con otra acción?")
                print("\033[0m")  # Reset

            # Caso 2: El usuario pregunta por clima
            elif weather_match:
                temp = obtener_temperatura(user_input)
                
                print("\033[92m")  # Verde
                if temp:
                    print(f"Chatbot: {temp}")
                else:
                    print("Chatbot: No pude obtener la temperatura, ¿podrías intentar con otra ciudad?")
                    
                print("\033[0m")  # Reset

            # Caso 3: El usuario pregunta por conversion de divisas
            elif conversion_match:
                resultado = procesar_conversion_divisas(user_input)
                
                print("\033[92m")  # Verde
                if resultado:
                    print(f"Chatbot: {resultado}")
                else:
                    print("Chatbot: No pude procesar la conversión. ¿Podrías revisar el formato?")

                print("\033[0m")  # Reset
            # Caso 4: El usuario no ejecuta alguna peticion 
            else:
                print("Chatbot: No entendí tu petición. ¿Podrías replantearla?")

        except KeyboardInterrupt:
            # Comando de salida Ctrl + C | Cmd + C
            print("\033[92m")  # Verde
            print("\nChatbot: Hasta luego, fue un placer ayudarte")
            print("\033[0m")  # Reset
            break


if __name__ == "__main__":
    chatbot()