import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as Lr
import matplotlib.pyplot as plt
from scipy import stats

# Experiencia 1 Potencial de frenado VS Frecuencia.
longitud_nm_0 =  [400, 410, 420, 430, 440,450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550,560]
voltaje_0 =  [0.993, 0.904, 0.836, 0.777, 0.735,0.679, 0.628, 0.583, 0.540, 0.494, 0.444, 0.406,0.356,0.311,0.261,0.219,0.105]

longitud_nm = [400,560]
voltaje = [0.993,0.105]

longitud_nm_1 = [400,410,420,430,440,450,470,490,550,560] #
voltaje_1 = [0.993,0.904,0.840,0.777,0.735,0.639,0.542,0.494,0.189,0.105] #

longitud_nm_f = [400,410,420,430,440,450,470]
voltaje_f = [0.993,0.904,0.840,0.777,0.735,0.639,0.542]

# Experiencia 2 Corriente vs Potencial de Frenado


# Datos de la rendija 1
voltaje_rendija_1 = [0.001, 0.097, 0.190, 0.287, 0.399, 0.518, 0.631, 0.772, 0.920]
corriente_rendija_1 = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]

# Datos de la rendija 2
voltaje_rendija_2 = [0.001, 0.051, 0.102, 0.150, 0.202, 0.250, 0.303, 0.355, 0.405, 0.455, 0.507, 0.553, 0.606, 0.651, 0.694]
corriente_rendija_2 = [1.45, 1.30, 1.20, 1.10, 0.95, 0.85, 0.75, 0.65, 0.55, 0.45, 0.35, 0.25, 0.20, 0.10, 0.00]

plt.figure()
plt.plot(voltaje_rendija_1, corriente_rendija_1, '-o', label='Rendija 1')
plt.plot(voltaje_rendija_2, corriente_rendija_2, '-o', label='Rendija 2')
plt.xlabel("Potencial de Frenado (V)")  
plt.ylabel("Fotocorriente (10pA)")
plt.legend()
plt.title("Fotocorriente para un $\lambda$ fijo")
plt.grid()

plt.show()

# Escalado y transformacion de datos a CSV:

nano = 1e-9 

longitud_m_0 = []
longitud_m = []
longitud_m_1 = []
longitud_m_f = []

frecuencia_0 = []
frecuencia = []
frecuencia_1 = []
frecuencia_f = []


# conversion de longitud de onda nanometro a metro
for x in longitud_nm_0:
    longitud_m_0.append(x*nano)

for x in longitud_nm:
    longitud_m.append(x*nano)

for x in longitud_nm_1:
    longitud_m_1.append(x*nano)

for x in longitud_nm_f:
    longitud_m_f.append(x*nano)


# frecuencia de cada longitud de onda
for y in longitud_m_0:
    frecuencia_0.append((3e8)/y)

for y in longitud_m:
    frecuencia.append((3e8)/y)

for y in longitud_m_1:
    frecuencia_1.append((3e8)/y)

for y in longitud_m_f:
    frecuencia_f.append((3e8)/y)

longitud_nm_0 = np.array(longitud_nm_0)
longitud_nm = np.array(longitud_nm)
longitud_nm_1 = np.array(longitud_nm_1)
longitud_nm_f = np.array(longitud_nm_f)

longitud_m_0 = np.array(longitud_m_0)
longitud_m = np.array(longitud_m)
longitud_m_1 = np.array(longitud_m_1)
longitud_m_f = np.array(longitud_m_f)

voltaje_0 = np.array(voltaje_0)
voltaje = np.array(voltaje)
voltaje_1 = np.array(voltaje_1)
voltaje_f = np.array(voltaje_f)

frecuencia_0 = np.array(frecuencia_0)
frecuencia = np.array(frecuencia)
frecuencia_1 = np.array(frecuencia_1)
frecuencia_f = np.array(frecuencia_f)



# Crear DataFrame
df0 = pd.DataFrame({

    'Lambda_0': longitud_nm_0,
    'LambdaNm_0': longitud_m_0,
    'Frecuencia_0': frecuencia_0,
    'Voltaje_0': voltaje_0
})

df1 = pd.DataFrame({
    'Lambda_1': longitud_nm,
    'LambdaNm_1': longitud_m,
    'Frecuencia_1': frecuencia,
    'Voltaje_1': voltaje
})

df2 = pd.DataFrame({
    'Lambda_2': longitud_nm_1,
    'LambdaNm_2': longitud_m_1,
    'Frecuencia_2': frecuencia_1,
    'Voltaje_2': voltaje_1
})

df3 = pd.DataFrame({
    'Lambda_f': longitud_nm_f,
    'LambdaNm_f': longitud_m_f,
    'Frecuencia_f': frecuencia_f,
    'Voltaje_f': voltaje_f
})

df0.to_csv('datos_experimentales_0.csv', index=False)
df1.to_csv('datos_experimentales_1.csv', index=False)
df2.to_csv('datos_experimentales_2.csv', index=False)
df3.to_csv('datos_experimentales_3.csv', index=False)

"""Grafica de los datos:"""


datos = pd.read_csv(delimiter=',' ,filepath_or_buffer = 'datos_experimentales_2.csv')


#Regresion lineal
slope_0, intercept_0, r_0, p_0, std_err_0 = stats.linregress(frecuencia_0, voltaje_0)
slope, intercept, r, p, std_err = stats.linregress(frecuencia, voltaje)
slope_1, intercept_1, r_1, p_1, std_err_1 = stats.linregress(frecuencia_1, voltaje_1)
slope_f, intercept_f, r_f, p_f, std_err_f = stats.linregress(frecuencia_f, voltaje_f)

def funcion_trabajo_0(frecuencia_0):
    return slope * frecuencia_0 + intercept

def funcion_trabajo(frecuencia):
    return slope * frecuencia + intercept

def funcion_trabajo_1(frecuencia_1):
    return slope * frecuencia_1 + intercept

def funcion_trabajo_f(frecuencia_f):
    return slope * frecuencia_f + intercept

x = np.linspace(4.499*10**(14) , frecuencia.max(), 1000)
y = np.linspace(4.499*10**(14) , frecuencia.max(), 1000)

modelo_0 = list(map(funcion_trabajo_0, x))
modelo = list(map(funcion_trabajo, x))
modelo_1 = list(map(funcion_trabajo_1, x))
modelo_f = list(map(funcion_trabajo_f, x))


#Graficas

#Grafica 0
plt.scatter(frecuencia_0, voltaje_0,color='royalblue')
plt.plot(x, modelo_0, color='orangered')
# plt.xlim(3.99*10**(14))
plt.xlim(5*10**(14))
plt.ylim(0)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Grafica 1: Potencial de frenado vs Frecuencia")
plt.grid()
plt.show()

#Grafica 1
plt.scatter(frecuencia, voltaje,color='royalblue')
plt.plot(x, modelo, color='orangered')
plt.xlim(5*10**(14))
plt.ylim(0)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Grafica 2: Potencial de frenado vs Frecuencia (dos puntos)")
plt.grid()
plt.show()

#Grafica 2
plt.scatter(frecuencia_1, voltaje_1,color='royalblue')
plt.plot(x, modelo_1, color='orangered')
plt.xlim(5*10**(14))
plt.ylim(0)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Grafica 3: Potencial de frenado vs Frecuencia (mejores datos)")
plt.grid()
plt.show()

#Grafica 3
plt.scatter(frecuencia_f, voltaje_f,color='royalblue')
plt.plot(x, modelo, color='orangered')
plt.xlim(3.99*10**(14))
# plt.xlim(6*10**(14))
# plt.ylim(0.4)
plt.xlim(5*10**(14))
plt.ylim(0)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Grafica 4: Potencial de frenado vs Frecuencia (Region de interes)")
plt.grid()
plt.show()

#Grafica 4
plt.scatter(frecuencia_f, voltaje_f,color='royalblue')
plt.plot(x, modelo, color='orangered')
plt.xlim(6*10**(14))
plt.ylim(0.4)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Grafica 5: Potencial de frenado vs Frecuencia (Region de interes)")
plt.grid()
plt.show()


# Resultados:

# Resultados 0
print("################  GRAFICA 1  #################")
print("Pendiente: ", slope_0," Error: ", std_err_0)
print("Corte: ", intercept_0, " Error: 0.0137865")
print("R: ", r_0," P: ", p_0)

# Datos de tu regresión 0
slope_error_0 =  std_err_0  # Error en la pendiente
e = 1.602176634e-19  # Carga del electrón (C)

# Cálculo de h en J·s
h_0 = slope_0 * e  # Conversión directa a J·s
h_error_0 = slope_error_0 * e  # Propagación del error


# Resultados 0
print(f"Constante de Planck (h): {h_0:.4e} J·s")
print(f"Error en h: ±{h_error_0:.4e} J·s")
print(f"Valor teorico de h: 6.62607015e-34 J·s")

# Comparación con el valor aceptado
error_relativo_0 = (abs(h_0 - 6.62607015e-34) / 6.62607015e-34) * 100
print(f"\nDiferencia relativa: {error_relativo_0:.2f}%\n")

# Resultados 1
print("################  GRAFICA 2  #################")
print("Pendiente: ", slope," Error: ", std_err)
print("Corte: ", intercept, " Error: 0.0137865")
print("R: ", r," P: ", p)

# Datos de tu regresión 1
slope_error =  std_err  # Error en la pendiente
e = 1.602176634e-19  # Carga del electrón (C)

# Cálculo de h en J·s
h = slope * e  # Conversión directa a J·s
h_error = slope_error * e  # Propagación del error


# Resultados 1
print(f"Constante de Planck (h): {h:.4e} J·s")
print(f"Error en h: ±{h_error:.4e} J·s")
print(f"Valor teorico de h: 6.62607015e-34 J·s")

# Comparación con el valor aceptado
error_relativo = (abs(h - 6.62607015e-34) / 6.62607015e-34) * 100
print(f"\nDiferencia relativa: {error_relativo:.2f}%\n")

# Resultados 2
print("################  GRAFICA 3  #################")
print("Pendiente: ", slope_1," Error: ", std_err_1)
print("Corte: ", intercept_1, " Error: 0.0137865")
print("R: ", r_1," P: ", p_1)

# Datos de tu regresión 2
slope_error_1 =  std_err_1  # Error en la pendiente
e = 1.602176634e-19  # Carga del electrón (C)

# Cálculo de h en J·s
h_1 = slope_1 * e  # Conversión directa a J·s
h_error_1 = slope_error_1 * e  # Propagación del error


# Resultados 2
print(f"Constante de Planck (h): {h_1:.4e} J·s")
print(f"Error en h: ±{h_error_1:.4e} J·s")
print(f"Valor teorico de h: 6.62607015e-34 J·s")

# Comparación con el valor aceptado
error_relativo_1 = (abs(h_1 - 6.62607015e-34) / 6.62607015e-34) * 100
print(f"\nDiferencia relativa: {error_relativo_1:.2f}%\n")


# Resultados 3
print("################  GRAFICA 4  #################")
print("Pendiente: ", slope_f," Error: ", std_err_f)
print("Corte: ", intercept_f, " Error: 0.0137865")
print("R: ", r_f," P: ", p_f)

# Datos de tu regresión 3
slope_error_f =  std_err_f  # Error en la pendiente
e = 1.602176634e-19  # Carga del electrón (C)

# Cálculo de h en J·s
h_f = slope_f * e  # Conversión directa a J·s
h_error_f= slope_error_f * e  # Propagación del error


# Resultados 3
print(f"Constante de Planck (h): {h_f:.4e} J·s")
print(f"Error en h: ±{h_error_f:.4e} J·s")
print(f"Valor teorico de h: 6.62607015e-34 J·s")

# Comparación con el valor aceptado
error_relativo_f = (abs(h_f - 6.62607015e-34) / 6.62607015e-34) * 100
print(f"\nDiferencia relativa: {error_relativo_f:.2f}%\n")