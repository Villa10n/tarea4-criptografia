import bcrypt
import time

# Hashear contraseñas de archivo_salida_1
archivo = open("archivo_salida_1", 'r')
archivo_salida = open("archivo_salida_1_bcrypt.txt", 'w')
tiempo_archivo1_inicio = time.time()
for linea in archivo:
    # Leemos una linea del archivo
    contraseña = linea.rstrip()
    # Creamos el hash
    pass_texto_plano = contraseña.encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal).decode()
    print(pass_hasheada)
    # Escribimos en el txt
    archivo_salida.write(pass_hasheada)
    archivo_salida.write("\n")
archivo.close()
archivo_salida.close()
tiempo_archivo1_final = time.time()
print("El tiempo total de archivo 1 es: ", tiempo_archivo1_final - tiempo_archivo1_inicio)

# Hashear contraseñas de archivo_salida_2
archivo = open("archivo_salida_2", 'r')
archivo_salida = open("archivo_salida_2_bcrypt.txt", 'w')
tiempo_archivo2_inicio = time.time()
for linea in archivo:
    # Leemos una linea del archivo
    contraseña = linea.rstrip()
    # Creamos el hash
    pass_texto_plano = contraseña.encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal).decode()
    print(pass_hasheada)
    # Escribimos en el txt
    archivo_salida.write(pass_hasheada)
    archivo_salida.write("\n")
archivo.close()
archivo_salida.close()
tiempo_archivo2_final = time.time()
print("El tiempo total de archivo 2 es: ", tiempo_archivo2_final - tiempo_archivo2_inicio)

# Hashear contraseñas de archivo_salida_3
archivo = open("archivo_salida_3", 'r')
archivo_salida = open("archivo_salida_3_bcrypt.txt", 'w')
tiempo_archivo3_inicio = time.time()
for linea in archivo:
    # Leemos una linea del archivo
    contraseña = linea.rstrip()
    # Creamos el hash
    pass_texto_plano = contraseña.encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal).decode()
    print(pass_hasheada)
    # Escribimos en el txt
    archivo_salida.write(pass_hasheada)
    archivo_salida.write("\n")
archivo.close()
archivo_salida.close()
tiempo_archivo3_final = time.time()
print("El tiempo total de archivo 3 es: ", tiempo_archivo3_final - tiempo_archivo3_inicio)

# Hashear contraseñas de archivo_salida_4
archivo = open("archivo_salida_4", 'r')
archivo_salida = open("archivo_salida_4_bcrypt.txt", 'w')
tiempo_archivo4_inicio = time.time()
for linea in archivo:
    # Leemos una linea del archivo
    contraseña = linea.rstrip()
    # Creamos el hash
    pass_texto_plano = contraseña.encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal).decode()
    print(pass_hasheada)
    # Escribimos en el txt
    archivo_salida.write(pass_hasheada)
    archivo_salida.write("\n")
archivo.close()
archivo_salida.close()
tiempo_archivo4_final = time.time()
print("El tiempo total de archivo 4 es: ", tiempo_archivo4_final - tiempo_archivo4_inicio)

# Hashear contraseñas de archivo_salida_5
archivo = open("archivo_salida_5", 'r')
archivo_salida = open("archivo_salida_5_bcrypt.txt", 'w')
tiempo_archivo5_inicio = time.time()
for linea in archivo:
    # Leemos una linea del archivo
    contraseña = linea.rstrip()
    # Creamos el hash
    pass_texto_plano = contraseña.encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal).decode()
    print(pass_hasheada)
    # Escribimos en el txt
    archivo_salida.write(pass_hasheada)
    archivo_salida.write("\n")
archivo.close()
archivo_salida.close()
tiempo_archivo5_final = time.time()
print("El tiempo total de archivo 5 es: ", tiempo_archivo5_final - tiempo_archivo5_inicio)