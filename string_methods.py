def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""
    print("Strip: "+nombre.strip())
    print("Lstrip: "+nombre.lstrip())
    print("Rstrip: "+nombre.rstrip())
    print("Upper: "+frase.upper())
    print("Lower: "+frase.lower())
    print("Title: "+frase.title())
    print("Find: "+ str(frase.find("gran")))
    print("Replace: "+frase.replace("programacion","desarrollo"))
    print("Count: "+str(frase.count("a")))
    print("Contiene Python:", "Python" in frase)
    print("Contiene Java:", "Java" in frase)
    print("Slice: "+frase[:6])
    print("Paso: "+frase[:6:2])
    print("Reverso: "+frase[5::-1])
    print(f"Formato: {nombre.strip()} sabe {frase[:6]}" )
    print(multilinea)

#string_methods()