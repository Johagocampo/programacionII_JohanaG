package vectores;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Vectores {
    public static void main(String[] args) {
        String Vacio [] = {};
        System.out.println("Lista : " + Arrays.toString(Vacio));
        
        System.out.println("La longitud de la Primera lista es: " + Vacio.length);
        
        String B [] ={"Instagram" , "X" , "Telegram" , "Epson" , "Indrive"};
        System.out.println("Lista de 5 elementos :" + Arrays.toString(B));
        
        System.out.println("La longitud de la Segunda lista es: " + B.length);
        
        
        System.out.println("Elementos: ");
        System.out.println("El Primer Elemento Es: " + B[0]);
        System.out.println("El Elemento De En Medio Es: " + B[2]);
        System.out.println("El Ultimo Elemento Es: " + B[4]);
        
        
        ArrayList<String> datos_personales = new ArrayList<>();
        datos_personales.add("Johana");
        datos_personales.add("18");
        datos_personales.add("1.69");
        datos_personales.add("soltera");
        datos_personales.add("Los cerezos");
        System.out.println("Datos Personales : " + datos_personales);
        
        
   ArrayList<String> it_companies = new ArrayList<>();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");
        it_companies.add(0, "Asus");
        System.out.println(it_companies);
        
        boolean does_exist = it_companies.contains("Samsung");
        System.out.println("La respuesta de si este elemento se encuentra es la lista es: " + does_exist);
        

        Collections.sort(it_companies);
        System.out.println("Lista Ordenada: " + it_companies);
        
        System.out.println("Lista invertida: " + it_companies.reversed());
        
        it_companies.remove(0); 
           System.out.println("lista sin la primera empresa informatica queda asi: " + it_companies);

         it_companies.clear();
            System.out.println("Limpiar lista ahora esta vacia: " + it_companies);

    }
}

