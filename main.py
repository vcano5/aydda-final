import pandas as pd

def binary_search(dataframe, target, key):
    arr = dataframe[key].tolist()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sequential_search(dataframe, target, key):
    arr = dataframe[key].tolist()
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def sort_mergesort_dataframe(dataframe, key):
    if len(dataframe) <= 1:
        return dataframe

    mitad = len(dataframe) // 2
    izquierda = dataframe.iloc[:mitad]
    derecha = dataframe.iloc[mitad:]

    # Llamadas recursivas para cada mitad
    izquierda_ordenada = sort_mergesort_dataframe(izquierda, key)
    derecha_ordenada = sort_mergesort_dataframe(derecha, key)

    # Mezclar ambas mitades ordenadas
    resultado = []
    i = j = 0

    while i < len(izquierda_ordenada) and j < len(derecha_ordenada):
        if izquierda_ordenada.iloc[i][key] <= derecha_ordenada.iloc[j][key]:
            resultado.append(izquierda_ordenada.iloc[i])
            i += 1
        else:
            resultado.append(derecha_ordenada.iloc[j])
            j += 1

    # Agregar los elementos restantes
    while i < len(izquierda_ordenada):
        resultado.append(izquierda_ordenada.iloc[i])
        i += 1
    
    while j < len(derecha_ordenada):
        resultado.append(derecha_ordenada.iloc[j])
        j += 1

    return pd.DataFrame(resultado, columns=dataframe.columns).reset_index(drop=True)


if __name__ == "__main__":
    while True:
        df = pd.read_excel("data.xlsx", dtype=str)
        print("Datos originales: ")
        print(df)

        print("\nMenú de opciones:")
        print("1. Realizar búsqueda binaria")
        print("2. Realizar búsqueda secuencial")
        print("3. Salir")
        choice = input("Seleccione una opción (1-3): ")
        if choice == '3':
            print("Saliendo del programa.")
            break
        elif choice != '1' and choice != '2':
            print("Opción no válida. Intente de nuevo.")
            continue
        key_column = input("Ingrese el criterio de búsqueda (por ejemplo, 'Nombre'): ")
        target_value = input("Ingrese el valor a buscar: ")
        df_ordenado = sort_mergesort_dataframe(df, key_column)
        index = -1
        if choice == '1':
            index = binary_search(df_ordenado, target_value, key_column)
        if choice == '2':
            index = sequential_search(df_ordenado, target_value, key_column)
        print("Resultados de la búsqueda: ", index)
        print(df_ordenado[index:index+1] if index != -1 else "No se encontró el valor.")