def truncar_lineas(input_file, output_file, n):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for linea in infile:
            linea_truncada = linea[:n]
            outfile.write(linea_truncada + '\n')

# Parámetros de ejemplo
input_file = 'fechas_2.txt'
output_file = 'fechas_salida.txt'
n = 10  # Número de caracteres a mantener por línea

truncar_lineas(input_file, output_file, n)
