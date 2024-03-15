def menu():
    print("1.Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")
menu()
x=int(input("Digite opcion: "))
if(x==1):
    print("ha seleccionado la opcion Personas")
elif(x==2):
        print("ha seleccionado la opcion Vehiculos")
elif(x==3):
    print("ha seleccionado la opcion Universidades")
elif(x==4):
    print("ha seleccionado la opcion Notas")
elif(x==5):
    print("ha seleccionado la opcion Salir")
else:
    print("La opcion no es valida")