import os
import time

inicio = time.time()
os.system('hashcat -a 0 -m 1000 archivo_4 diccionario_1.dict diccionario_2.dict -o archivo_salida_4 --outfile-format=2')
final = time.time()
print("el programa ha demorado: ", final-inicio)