def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    # nombre_completo = input("Nombre completo: ")
    nombre_strip= nombre_completo.strip()
    nombre_lower=nombre_completo.lower()
    # email = input("Email: ")
    # nota1 = input("nota: ")
    # nota2 = input("nota: ")
    # nota3 = input("nota: ")

    titulo = "    FICHA DEL ALUMNO"
    deco = "="*24
    print(f"{deco}\n{titulo}\n{deco}")

    print("Nombre: "+nombre_strip.title())
    print("Email: "+email.lower())
    print("Caracteres en nombre: "+str(len(nombre_strip)))

    espacio_nombre=nombre_strip.find(" ")
    iniciales= nombre_strip[0]+nombre_strip[espacio_nombre+1]
    print("Iniciales: "+iniciales.upper())
    apellido = nombre_strip[espacio_nombre+1:]
    nombre = nombre_strip[:espacio_nombre]
    usuario = apellido+"."+nombre
    print("Usuario: "+usuario.lower())

    print("Email valido:","@" in email)
    arroba = email.find("@")
    print("Dominio: "+email[arroba+1:].lower())

    nombre_para_archivo= nombre_strip.title().replace(" ","_")
    print("Nombre para archivo: "+nombre_para_archivo)

    cantidad_a= nombre_lower.count("a")
    print("Cantidad de a: "+str(cantidad_a))
    print("Codigo secreto: "+nombre_strip.upper()[-1::-1])

    print("Nota 1: "+ nota1)
    print("Nota 2: "+ nota2)
    print("Nota 3: "+ nota3)
    suma_notas = int(nota1)+int(nota2)+int(nota3)
    print("Suma: "+ str(suma_notas))
    promedio = float(suma_notas / 3)
    print("Promedio: "+str(promedio))
    promedio_entero = int(suma_notas // 3)
    print("Promedio entero: "+str(promedio_entero))
    print(deco)




ficha()
