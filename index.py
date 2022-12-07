import pandas as pd
import os
# TXT
with open("reporte.txt", "r", encoding="utf8") as file:
    data = file.read()
arrayTxT = data.split(";")

# Excel(tienen que estar en formato xlsx)
input_cols = [14]
df = pd.read_excel("resumen.xlsx",
                   header=6,
                   usecols=input_cols)

arrayExcel = df.to_string().split('\n')

# Tamaño del array
dimension = len(arrayTxT)
cedulasEncontradas = []
cedulasNoEncontradas = []

for y in arrayExcel:
    print(y[-8:])
    if y[-8:] in arrayTxT:
        cedulasEncontradas.append(y[-8:])
    else:
        cedulasNoEncontradas.append(y[-8:])

# Esto es porque el primer valor no es una cedula
cedulasNoEncontradas.remove("regunta8")

# Generar archivo txt con las cedulas que no fueron encontradas
if not os.path.exists('Salida/'):
    os.makedirs('Salida/')

f = open('Salida/CedulasNoEncontradas.txt', 'a')
f.write("Estas son las cedulas que NO fueron encontradas en el archivo de texto :" +
        str(cedulasNoEncontradas))
f.close()
