package menu2;

import java.util.Scanner;
public class menu {

    public static void main(String[] args) {
        System.out.println("Menu de opciones");
        System.out.println("1. Personas");
        System.out.println("2. Vehiculos");
        System.out.println("3. Universidades");
        System.out.println("4. Notas");
        System.out.println("5. Salir");

        Scanner consola = new Scanner(System.in);
        System.out.println("Ingrese su opcion: ");
        int opcionMenu = consola.nextInt();
        switch (opcionMenu) {
            case 1:
                System.out.println("ha seleccionado la opcion Personas");
                break;
            case 2:
                System.out.println("ha seleccionado la opcion Vehiculos");
                break;
            case 3:
                System.out.println("ha seleccionado la opcion Univesidades");
                break;
            case 4:
                System.out.println("ha seleccionado la opcion Notas");
                break;
            case 5:
                System.out.println("ha seleccionado la opcion Salir");
                break;
            default:
                System.out.println("la opcion no es valida");
        }

    }
}
