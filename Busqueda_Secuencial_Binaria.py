import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("Empleados.xlsx")

#Secuencial
def busqueda_secuencial(df, numero_empleado):
    for i in range(len(df)):    #Se recorren los indices por posicion 
        if df.iloc[i]["No. de empleado"] == numero_empleado:    #Da la fila por posicion i en la columna de No. de empleado   
            return df.iloc[i]   #Si coincide regresa
    return None #Si no coincide sigue iterando


#Binaria
def busqueda_binaria(df, numero_empleado):
    df_ordenado = df.sort_values(by="No. de empleado").reset_index(drop=True)   #Se crea copia ascendente, Reindexa la copia desde 0 a N-1 (reset_index(drop=True))
    inicio = 0
    fin = len(df_ordenado) - 1  #Establecen limites de los extremos

    while inicio <= fin:    #Mientras el intevalo no este vacio
        medio = (inicio + fin) // 2 #Calculo del medio
        valor_medio = df_ordenado.loc[medio, "No. de empleado"]     #Se lee el medio (en este caso el empleado del medio)

        if valor_medio == numero_empleado:  #Si encontramos al empleado retorna la fila
            return df_ordenado.loc[medio]
        elif valor_medio < numero_empleado: #El empleado existe en la mitad superior
            inicio = medio + 1
        else:
            fin = medio - 1     #Esta es la mitad inferior

    return None


#main
num_buscar = int(input("Ingresa el No. de empleado a buscar: "))

resultado_sec = busqueda_secuencial(df, num_buscar)
resultado_bin = busqueda_binaria(df, num_buscar)

print("\nResultado de búsqueda secuencial:")
print(resultado_sec if resultado_sec is not None else "No encontrado")

print("\nResultado de búsqueda binaria:")
print(resultado_bin if resultado_bin is not None else "No encontrado")
