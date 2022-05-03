from acciones import *
def run():
    running=True
    while running!=False:
        listar()
        print("[1] Agregar   [2] Eliminar   [3] Actualizar  [4] salir")
        option = int(input("Eliga una opcion: "))
        route_action(option)
        if (option==4):
            running=False

def route_action(action):
    if(action==1):
        agregar()
    elif(action==2):
        eliminar()
    elif(action==3):
        actualizar()
    

run()