import os
import time

inicio = time.time()
os.system('hashcat -a 0 -m 10 archivo_2 diccionario_1.dict diccionario_2.dict -o archivo_salida_2 --outfile-format=2')
final = time.time()
print("el programa ha demorado: ", final-inicio)