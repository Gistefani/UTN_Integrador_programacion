
#Caso práctico: 
# Ordenar listas de estudiantes de una comisión por las notas obtenidas en el parcial-
#Ordenamiento por selección
#definición de lista estudiantes
import time
import random
estudiantes = [
    {"nombre": "Ana", "nota": 75},
    {"nombre": "Luis", "nota": 60},
    {"nombre": "María", "nota": 95},
    {"nombre": "Juan", "nota": 80},
    {"nombre": "Sofía", "nota": 50},
    {"nombre": "Pedro", "nota": 40},
    {"nombre": "Alejo", "nota": 10},
    {"nombre": "Bruno", "nota": 65},
    {"nombre": "Tomas", "nota": 90},
    {"nombre": "Santiago", "nota":85},
    {"nombre": "Genaro", "nota": 30},
    {"nombre": "Benicio", "nota": 45},
]

estudiantes_random = [{"nombre": f"Estudiante{i}", "nota": random.randint(0, 10000)} for i in range(10000)]

#Definición por selección
#Este algoritmo compara elemento por elemento. 
# Es fácil de entender pero ineficiente con listas grandes .Tiene complejidad O(n²)

def selection_sort_objs(lista):
    a = lista.copy()#creo una copia para no modificar la original 
    n = len(a)
    for i in range(n):
        min_idx = i #asume que el estudiante actual tiene la nota mínima.
        for j in range(i + 1, n):
            if a[j]["nota"] < a[min_idx]["nota"]:#si se encuentra una nota menor, se actualiza el índice mínimo.
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a #Devuelve la lista ordenada por notas de menor a mayor.

#quick sort -complejidad O(n log n)

def quick_sort_objs(lista):
    if len(lista) <= 1:# si la lista está vacía o tiene un solo elemento, ya está ordenada.
        return lista
    pivote = lista[0]#toma el primer estudiante como referencia (pivote).
    menores = [x for x in lista[1:] if x["nota"] < pivote["nota"]]
    mayores = [x for x in lista[1:] if x["nota"] >= pivote["nota"]]
    return quick_sort_objs(menores) + [pivote] + quick_sort_objs(mayores)



#programa principal
print("Original:")
for e in estudiantes:
    print(f"{e['nombre']}: {e['nota']}")


inicio_selection = time.time()
ordenados_selection = selection_sort_objs(estudiantes)
fin_selection = time.time()
tiempo_selection = fin_selection - inicio_selection

print("\nOrdenados con Selection Sort:")
for e in ordenados_selection:
    print(f"{e['nombre']}: {e['nota']}")
print(f"Tiempo de ejecución (Selection Sort): {tiempo_selection:.10f} segundos")

inicio_selection = time.time()
ordenados_selection = selection_sort_objs(estudiantes_random)
fin_selection = time.time()
tiempo_selection_random = fin_selection - inicio_selection
print(f"\nTiempo de ejecución (Selection Sort con lista aleatoria de 10.000 elementos): {tiempo_selection_random:.10f} segundos")

inicio_quick = time.time()
ordenados_quick = quick_sort_objs(estudiantes)
fin_quick = time.time()
tiempo_quick = fin_quick - inicio_quick
print("\nOrdenados con Quick Sort:")
for e in ordenados_quick:
    print(f"{e['nombre']}: {e['nota']}")
print(f"Tiempo de ejecución (Quick Sort): {tiempo_quick:.10f} segundos")


inicio_quick_random = time.time()
ordenados_quick_random= quick_sort_objs(estudiantes_random)
fin_quick_random = time.time()
tiempo_quick_random = fin_quick_random - inicio_quick_random
print(f"\nTiempo de ejecución ( Quick con lista aleatoria de 10.000 elementos): {tiempo_quick_random:.10f} segundos")

