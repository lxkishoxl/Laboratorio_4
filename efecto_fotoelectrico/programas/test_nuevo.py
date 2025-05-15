#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 22:10:00 2025

@author: kynz
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as Lr
import matplotlib.pyplot as plt
from scipy import stats
import math


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

# Función para hacer gráficas de Potencial de Frenado vs Frecuencia:

def graficar_efecto_fotoelectrico(frecuencia, voltaje, x, modelo, slope, std_err, intercept, r, titulo, corte_exp=-14):
    """
    Genera una gráfica del efecto fotoeléctrico con anotaciones detalladas.
    
    Parámetros:
        frecuencia: array de frecuencias (Hz)
        voltaje: array de voltajes (V)
        x: array para la curva ajustada
        modelo: valores del modelo ajustado (misma longitud que x)
        slope: pendiente de la regresión
        std_err: error estándar de la pendiente
        intercept: ordenada al origen
        r: coeficiente de correlación
        titulo: título para la gráfica
        corte_exp: exponente usado para normalizar el corte (default -14)
    """
    # Constantes
    e = 1.602176634e-19  # Carga del electrón
    h_teorico = 6.62607015e-34

    # Pendiente normalizada
    exp_slope = int(math.floor(math.log10(abs(slope))))
    slope_norm = slope / (10 ** exp_slope)
    std_err_norm = std_err / (10 ** exp_slope)

    # Constante de Planck y error propagado
    h = slope * e
    h_error = std_err * e
    exp_h = int(math.floor(math.log10(abs(h))))
    h_norm = h / (10 ** exp_h)
    h_error_norm = h_error / (10 ** exp_h)

    # Error relativo
    error_relativo = (abs(h - h_teorico) / h_teorico) * 100

    # R²
    r2 = r**2

    # Texto de anotación
    texto = (
        f"Pendiente: ({slope_norm:.1f} ± {std_err_norm:.1f})e{exp_slope} V·s\n"
        f"Corte: ({intercept:.1f} ± 0.1)e{corte_exp} Hz\n"
        f"Constante de Planck (h): ({h_norm:.1f} ± {h_error_norm:.1f})e{exp_h} J·s\n"
        f"Valor teórico de h: 6.62607015e-34 J·s\n"
        f"Discrepancia: {error_relativo:.2f}%\n"
        f"Índice de correlación (R): {r:.3f}\n"
        f"Coeficiente de determinación (R²): {r2:.3f}"
    )

    # Crear figura
    plt.figure(figsize=(10, 6))
    plt.scatter(frecuencia, voltaje, color='royalblue', s=90)
    plt.plot(x, modelo, color='orangered', linewidth=2.6)
    plt.xlim(min(frecuencia)*0.98, max(frecuencia)*1.02)
    plt.ylim(0)
    plt.xlabel('Frecuencia (Hz)', fontsize=16)
    plt.ylabel("Potencial de Frenado (V)", fontsize=16)
    plt.title(titulo, fontsize=18)
    plt.tick_params(axis='both', labelsize=14)
    plt.gca().xaxis.get_offset_text().set_fontsize(14)
    plt.grid()

    # Anotación
    plt.annotate(
        texto,
        xy=(0.035, 0.65), xycoords='axes fraction',
        fontsize=12,
        ha='left', va='bottom',
        bbox=dict(boxstyle='round,pad=1', fc='white', alpha=0.8)
    )

    plt.show()


graficar_efecto_fotoelectrico(
    frecuencia=frecuencia_0,
    voltaje=voltaje_0,
    x=x,
    modelo=modelo_0,
    slope=slope_0,
    std_err=std_err_0,
    intercept=intercept_0,
    r=r_0,
    titulo="Gráfica 1: Potencial de frenado vs Frecuencia"
)

graficar_efecto_fotoelectrico(
    frecuencia=frecuencia,
    voltaje=voltaje,
    x=x,
    modelo=modelo,
    slope=slope,
    std_err=std_err,
    intercept=intercept,
    r=r,
    titulo="Gráfica 2: Potencial de frenado vs Frecuencia (dos puntos)"
)

graficar_efecto_fotoelectrico(
    frecuencia=frecuencia_1,
    voltaje=voltaje_1,
    x=x,
    modelo=modelo_1,
    slope=slope_1,
    std_err=std_err_1,
    intercept=intercept_1,
    r=r_1,
    titulo="Gráfica 3: Potencial de frenado vs Frecuencia (datos filtrados)"
)


#gráfica 4
slope_error_f = std_err_f
exp_slope = int(math.floor(math.log10(abs(slope_f))))
slope_norm_f = slope_f / (10 ** exp_slope)
std_err_norm_f= std_err_f / (10 ** exp_slope)
e = 1.602176634e-19  # C

h_f = slope_f * e
exp_h = int(math.floor(math.log10(abs(h_f))))
h_original= h_f
h_f = h_f / (10 ** exp_h)
h_error_f = slope_error_f * e
h_error_f = h_error_f / (10 ** exp_h)
error_relativo_f = (abs(h_original - 6.62607015e-34) / 6.62607015e-34) * 100
r2_f = r_f**2




# Texto para la anotación
texto_0 = (
    f"Pendiente: ({slope_norm_f:.1f} ± {std_err_norm_f:.1f})e{exp_slope} V.s\n"
    f"Corte: ({intercept_f:.1f} ± 0.1)e-14 Hz\n"
    f"Constante de Planck (h): ({h_f:.1f} ± {h_error_f:.1f})e{exp_h} J·s\n"
    f"Valor teórico de h: 6.62607015e-34 J·s\n"
    f"Discrepancia: {error_relativo_f:.2f}%\n"
    f"Indice de correlación (R): {r_f:.3f}\n"
    f"Coeficiente de determinación (R²): {r2_f:.3f}"
)
# Tamaño de la figura
plt.figure(figsize=(10, 6))
plt.scatter(frecuencia_f, voltaje_f, color='royalblue', s=70)
plt.plot(x, modelo_f, color='orangered', linewidth=2.6)
plt.xlim(5e14)
plt.ylim(0)
plt.xlabel('Frecuencia (Hz)', fontsize=16)
plt.ylabel("Potencial de Frenado (V)", fontsize=16)
plt.title("Gráfica 4: Potencial de frenado vs Frecuencia (Región de interes)", fontsize=18)
plt.tick_params(axis='both', labelsize=14)
plt.gca().xaxis.get_offset_text().set_fontsize(14)

plt.grid()


# Anotación en esquina inferior derecha
plt.annotate(
    texto_0,
    xy=(0.035, 0.65), xycoords='axes fraction',
    fontsize=12,
    ha='left', va='bottom',
    bbox=dict(boxstyle='round,pad=1', fc='white', alpha=0.8)
)

plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(frecuencia_f, voltaje_f,color='royalblue', s=70)
plt.plot(x, modelo, color='orangered', linewidth=2.6)
plt.xlim(6*10**(14))
plt.ylim(0.4)
plt.xlabel('Frecuencia (Hz)', fontsize=16)
plt.ylabel("Potencial de Frenado (V)", fontsize=16)
plt.title("Gráfica 5: Potencial de frenado vs Frecuencia (Región de interes)", fontsize=18)
plt.tick_params(axis='both', labelsize=14)
plt.gca().xaxis.get_offset_text().set_fontsize(14)
plt.grid()

# Anotación en esquina inferior derecha
plt.annotate(
    texto_0,
    xy=(0.035, 0.65), xycoords='axes fraction',
    fontsize=12,
    ha='left', va='bottom',
    bbox=dict(boxstyle='round,pad=1', fc='white', alpha=0.8)
)

plt.show()



