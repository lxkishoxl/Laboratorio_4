import pandas as pd
import argparse
from pathlib import Path

def convert_xlsx_to_csv(input_file, output_file=None, sheet_name=0, delimiter=','):
    """
    Convierte un archivo XLSX a CSV
    
    Args:
        input_file (str): Ruta del archivo XLSX de entrada
        output_file (str, optional): Ruta del archivo CSV de salida. Si no se especifica,
                                    se usará el mismo nombre que el input con extensión .csv
        sheet_name (str/int, optional): Nombre o índice de la hoja a convertir (default: primera hoja)
        delimiter (str, optional): Delimitador para el archivo CSV (default: ',')
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(input_file, sheet_name=sheet_name)
        
        # Determinar el nombre del archivo de salida si no se especifica
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.with_suffix('.csv')
        
        # Guardar como CSV
        df.to_csv(output_file, index=False, sep=delimiter, encoding='utf-8')
        
        print(f"Archivo convertido exitosamente: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
    except Exception as e:
        print(f"Ocurrió un error durante la conversión: {str(e)}")

if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Convertir archivos XLSX a CSV')
    parser.add_argument('input', help='Ruta del archivo XLSX de entrada')
    parser.add_argument('-o', '--output', help='Ruta del archivo CSV de salida (opcional)')
    parser.add_argument('-s', '--sheet', default=0, 
                        help='Nombre o índice de la hoja a convertir (default: primera hoja)')
    parser.add_argument('-d', '--delimiter', default=',', 
                        help='Delimitador para el archivo CSV (default: ",")')
    
    args = parser.parse_args()
    
    # Llamar a la función de conversión
    convert_xlsx_to_csv(
        input_file=args.input,
        output_file=args.output,
        sheet_name=args.sheet,
        delimiter=args.delimiter
    )