import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double[] A = new double[20];
        double[] B = new double[20];
        double[] C = new double[20];

        for(int i = 0; i < 20; i++){
            System.out.print("Digite A: ");
            A[i] = sc.nextDouble();
        }

        for(int i = 0; i < 20; i++){
            System.out.print("Digite B: ");
            B[i] = sc.nextDouble();
        }

        for(int i = 0; i < 20; i++){
            C[i] = A[i] - B[i];
        }

        for(int i = 0; i < 20; i++){
            System.out.print(C[i] + " ");
        }

        sc.close();
    }
}
