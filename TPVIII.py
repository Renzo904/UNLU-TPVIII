def problema1():
    palabra = ""
    while(palabra != "parar"):
        palabra = input("Ingrese una palabra: ")
        print(palabra)
    print("--- TERMINADO ---")

def problema2():
    sumatotal = 0
    cantidadnotas = 0
    notaingresada = 0
    while(notaingresada != -1):
        notaingresada = int(input("Ingrese la nota(o -1 para terminar): "))
        if(notaingresada != -1):
            sumatotal = sumatotal + notaingresada
            cantidadnotas = cantidadnotas + 1
    promedio = sumatotal / cantidadnotas
    print(f"El promedio de notas es {promedio}")

problema1()
problema2()
