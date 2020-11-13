import bcrypt
import time

# Hashear contraseñas de archivo_salida_1
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