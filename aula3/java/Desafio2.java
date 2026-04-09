import java.util.Scanner;

public class Desafio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero = 0;

        while (numero <= 10) {
            System.out.print("Digite um número: ");
            numero = scanner.nextInt();
        }

        System.out.println("Obrigado!");
        scanner.close();
    }
}
