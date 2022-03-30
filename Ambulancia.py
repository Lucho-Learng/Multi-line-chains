CantAmbulancias = int(input("Ingrese la cantidad de ambulancias que hay: "))
Corx1 = float(input("Ingrese la coordenada x de donde se encuentra: "))
Cory1 = float(input("Ingrese la coordenada y de donde se encuentra: "))
print(Corx1, Cory1)

print(range(CantAmbulancias))

for i in range(CantAmbulancias):
    Corx2 = float(input("Ingrese la coordenada en x de la ambulancia  "+str(i)))
    Cory2 = float(input("Ingrese la coordenada en y de la ambulancia  "+str(i)))

    if (i==0):
        distancia=(((Cory2-Cory1)**2)+((Corx2-Corx1)**2))**(0.5)
        print(distancia)
        masCErca = distancia
        CorXc = Corx2
        CorYc = Cory2

    else:
        distancia=(((Cory2-Cory1)**2)+((Corx2-Corx1)**2))**(0.5)
        if(distancia < masCErca):
            masCErca=distancia
            CorXc = Corx2
            CorYc  = Cory2
print("La ambulancia mas cercana esta a una distancia de: "+str(masCErca) +"  Con coordenadas: "+str(CorXc)+","+str(CorYc))
