lista=[]
filas=int(input("ingrese numero de filas: "))
columnas=int(input("ingrese numero de columnas:" ))

for i in range(filas):
    fila=[]
    for j in range (columnas):
        while True:
            fi=int(input(f"ingrese un valor {i}{j}: "))
            if fi % 2 == 0:
                fila.append(fi)
                break
            else:
                print("ingrese un numero par")
    lista.append(fila)

for i in lista:
    lista.sort()
    for j in i:
        i.sort()
        
for i in lista:
    print(i)
  si verdad?
