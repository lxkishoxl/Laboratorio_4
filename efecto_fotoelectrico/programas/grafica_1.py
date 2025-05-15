import numpy as np
from sklearn.linear_model import LinearRegression as Lr
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Datos
datos = pd.read_csv(delimiter=',' ,filepath_or_buffer = 'datos_expeirmentales.csv')

f = np.array(datos['Frecuencia'])
v_1 = np.array(datos['Voltaje'])


#Regresion lineal
slope, intercept, r, p, std_err = stats.linregress(f, v_1)

def funcion_trabajo(f):
    return slope * f + intercept

x = np.linspace(4.499*10**(14) , f.max(), 1000)
y = np.linspace(4.499*10**(14) , f.max(), 1000)
modelo = list(map(funcion_trabajo, x))

#Graficas
plt.scatter(f, v_1,color='royalblue')
plt.plot(x, modelo, color='orangered')
plt.xlim(3.99*10**(14))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel("Potencial de Frenado (V)")
plt.title("Potencial de frenado vs Frecuencia")
plt.grid()

# plt.figure()
# plt.plot(voltajes,intensidades, '-o')
# plt.xlabel("Potencial de Frenado (V)")  
# plt.ylabel("Fotocorriente (10pA)")
# plt.legend(['Rendija 1', 'Rendija 2', 'Rendija 3'])
# plt.title("Fotocorriente para un $\lambda$ fijo")
# plt.grid()

plt.show()

# Datos de la regresion
print("Pendiente: ", slope," Error: ", std_err)
print("Corte: ", intercept, " Error: 0.0137865")
print("R: ", r," P: ", p)

slope_error =  std_err  # Error en la pendiente
e = 1.602176634e-19  # Carga del electrón (C)

# Cálculo de h en J·s
h = slope * e  # Conversión directa a J·s
h_error = slope_error * e  # Propagación del error

# Resultados
print(f"Constante de Planck (h): {h:.4e} J·s")
print(f"Error en h: ±{h_error:.4e} J·s")
print(f"Valor aceptado de h: 6.62607015e-34 J·s (CODATA 2018)")

# Comparación con el valor aceptado
error_relativo = (abs(h - 6.62607015e-34) / 6.62607015e-34) * 100
print(f"\nDiferencia relativa: {error_relativo:.2f}%")