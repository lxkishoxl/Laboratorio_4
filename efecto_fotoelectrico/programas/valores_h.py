import numpy as np

# Datos de tu regresión
slope = 4.063880956034182e-15   # Pendiente (V/Hz)
slope_error =  1.0022976854345655e-16  # Error en la pendiente
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