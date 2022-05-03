Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}


def listar():
    lista=[]
    print("==============================")
    print("Lista de productos")
    print("==============================")
    for i in range(1,list(Productos)[-1]+1):
        if (Productos.get(i,0)!=0):
            lista.append([i,Productos[i],Precios[i],Stock[i]])
        
    
    print ("{:<8} {:<15} {:<15} {:<10}".format('id','Producto','Precio','Cantidad'))

    for v in lista: 
        id, Producto, Precio, Cantidad = v
        print ("{:<8} {:<15} {:<15} {:<10}".format(id, Producto, Precio, Cantidad))
    
    print("==============================")

def agregar():
    nombre=str(input("introduce el nombre del producto: "))
    precio=round(float(input("introduce el precio del producto: ")),2)
    stock=int(input("introduce la cantidad del producto: "))
    Productos[list(Productos)[-1]+1]=nombre
    Precios[list(Precios)[-1]+1]=precio
    Stock[list(Stock)[-1]+1]=stock

def eliminar():
    while(True):
        indice=int(input("introduce el id del producto que quieres eliminar: "))
        if (Productos.get(indice,0)==0):
            print("Valor de id no existe vuelve a intentarlo")
        else:
            break
    Productos.pop(indice)
    Precios.pop(indice)
    Stock.pop(indice)

def actualizar():
    while(True):
        indice=int(input("introduce el id del producto que quieres actualizar: "))
        if (Productos.get(indice,0)==0):
            print("Valor de id no existe vuelve a intentarlo")
        else:
            break
    nombre=input("introduce el nuevo nombre del producto: ")
    precio=round(float(input("introduce el nuevo precio del producto: ")),2)
    stock=int(input("introduce la nueva cantidad del producto: "))
    Productos[indice]=nombre
    Precios[indice]=precio
    Stock[indice]=stock
