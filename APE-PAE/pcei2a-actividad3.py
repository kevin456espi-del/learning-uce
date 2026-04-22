# Parte dos
lista=[]
x=int(input("ingrese la cantidad de columnas:"))
y=int(input("ingrese la cantidad de filas:"))

for i  in range(y):
    fila=[]
    for j in range(x):
            fila.append(input(f"ingrese el elemento de x={i},y={j}:"))
    lista.append(fila)
    
def imprimir_lista():
    for i in lista:
        for j in i:
            print(j,end="")
        print()
        
o=input("¿desea ordenar la lista si/no?:")
if o == "si":
    for i in lista:
        fila.sort()
    imprimir_lista()
else:
    imprimir_lista()
        
