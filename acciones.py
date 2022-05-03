from multiprocessing.sharedctypes import Value


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
    while(True):
        try:
            nombre=str(input("introduce el nombre del producto: "))
            break;
        except ValueError:
            print("el valor ingresado es erroneo")

    while(True):
        try:
            precio=round(float(input("introduce el precio del producto: ")),2)
            if precio>0:
                break;
        except ValueError:
            print("Ingresa un valor numerico positivo")
    while(True):
        try:
            stock=int(input("introduce la cantidad del producto: "))
            if stock>0:        
                break;
        except ValueError:
            print("Ingresa un valor numerico positivo")
    
    Productos[list(Productos)[-1]+1]=nombre
    Precios[list(Precios)[-1]+1]=precio
    Stock[list(Stock)[-1]+1]=stock

def eliminar():
    while(True):
        try:
            indice=int(input("introduce el id del producto que quieres eliminar: "))
            if (Productos.get(indice,0)==0):
                print("Valor de id no existe vuelve a intentarlo")
            else:
                break
        except ValueError:
            print("el id debe ser un numero entero positivo")
    Productos.pop(indice)
    Precios.pop(indice)
    Stock.pop(indice)

def actualizar():
    while(True):
        try:
            indice=int(input("introduce el id del producto que quieres actualizar: "))
            if (Productos.get(indice,0)==0):
                print("Valor de id no existe vuelve a intentarlo")
            else:
                break
        except:
            print("el id debe ser un numero entero positivo")
    while(True):
        try:
            nombre=str(input("introduce el nuevo nombre del producto: "))
            break;
        except ValueError:
            print("el valor ingresado es erroneo")

    while(True):
        try:
            precio=round(float(input("introduce el nuevo precio del producto: ")),2)
            if precio>0:
                break;
        except ValueError:
            print("Ingresa un valor numerico positivo")
    while(True):
        try:
            stock=int(input("introduce la nueva cantidad del producto: "))
            if stock>0:        
                break;
        except ValueError:
            print("Ingresa un valor numerico positivo")
    Productos[indice]=nombre
    Precios[indice]=precio
    Stock[indice]=stock
