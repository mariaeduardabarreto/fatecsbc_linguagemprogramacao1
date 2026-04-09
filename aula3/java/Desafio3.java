import java.util.Scanner;

public class Desafio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double soma = 0;

        for (int i = 0; i < 5; i++) {
            System.out.print("Digite a nota: ");
            soma += scanner.nextDouble();
        }

        System.out.println("Média: " + soma / 5);
        scanner.close();
    }
}
