import numpy as np
import pandas as pd


# longitud_nm = [350, 360, 370, 380, 390, 400, 410, 420, 430, 440,
#                450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]
longitud_nm =  [400, 410, 420, 430, 440,450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550,560]
#330 1.493 530 0.434
# voltaje = [1.305, 1.282, 1.174, 1.105, 1.057, 0.993, 0.904, 0.836, 0.777, 0.735,
#            0.679, 0.628, 0.583, 0.540, 0.494, 0.444, 0.406,0.356,0.311,0.261,0.219]
voltaje =  [0.993, 0.904, 0.836, 0.777, 0.735,
           0.679, 0.628, 0.583, 0.540, 0.494, 0.444, 0.406,0.356,0.311,0.261,0.219,0.105]

nano = 1e-9
longitud_m = []
frecuencia = []

# conversion de longitud de onda nanometro a metro
for x in longitud_nm:
    longitud_m.append(x*nano)
    # print(f'Este es el valor: {x}')

# frecuencia de cada longitud de onda
for y in longitud_m:
    frecuencia.append((3e8)/y)

print(f'array con la longitud lambda en m: {longitud_m}')
print(f'array con la frecuencia de cada longitud de onda: {frecuencia}')

longitud_nm = np.array(longitud_nm)
longitud_m = np.array(longitud_m)
voltaje = np.array(voltaje)
frecuencia = np.array(frecuencia)

# Crear DataFrame

df = pd.DataFrame({
    'Lambda': longitud_nm,
    'LambdaNm': longitud_m,
    'Frecuencia': frecuencia,
    'Voltaje': voltaje
})

df.to_csv('datos_expeirmentales.csv', index=False)


