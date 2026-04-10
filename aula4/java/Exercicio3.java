import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] A = new int[15];
        int[] B = new int[15];

        for(int i = 0; i < 15; i++){
            System.out.print("Digite um número: ");
            A[i] = sc.nextInt();
        }

        for(int i = 0; i < 15; i++){
            B[i] = A[i] * A[i];
        }

        for(int i = 0; i < 15; i++){
            System.out.println("A: " + A[i] + " B: " + B[i]);
        }

        sc.close();
    }
}
