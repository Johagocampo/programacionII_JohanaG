hola=True
def menu():
    print("1.Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")
while(hola):
    menu()
    x=int(input("Digite opcion: "))
    if(x==1):
        print("ha seleccionado la opcion Personas")

    if(x==2):
        print("ha seleccionado la opcion Vehiculos")

    if(x==3):
        print("ha seleccionado la opcion Universidades")

    if(x==4):
        print("ha seleccionado la opcion Notas")

    if(x==5):
        print("ha seleccionado la opcion Salir")
        exit()
    if(x>5 or x<1 ):
        print("La opcion no es valida")