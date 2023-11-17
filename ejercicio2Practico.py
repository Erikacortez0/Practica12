def invertir_cadenas(cadenas):
   
    if len(cadenas) <= 1:
        return cadenas
    
    else:
        return cadenas[-1] + invertir_cadenas(cadenas[1:-1]) + cadenas[0]


mi_cadena = "Hola, mundo!"
resultado = invertir_cadenas(mi_cadena)
print(f"La cadena original: {mi_cadena}")
print(f"La cadena invertida: {resultado}")