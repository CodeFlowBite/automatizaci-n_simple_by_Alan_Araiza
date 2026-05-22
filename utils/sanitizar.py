def sanitizar(user_input):

    # Prefijos 
    prefixies = ["la", "el", "las", "los", "de", "la", "las", "los", "precio de", "clima en", "clima de", "acción de", "accion de", "precio de la acción de", "precio de la accion de", "precio de las acciones de", "precio de los acciones de"]
    
    # Entrada en Min
    name = user_input.lower()

    changed = True
    while changed:
        changed = False
        for p in prefixies:
            if name.startswith(p):
                name = name[len(p):].strip()
                changed = True
        

    return name 
