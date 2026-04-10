public class Exercicio1 {
    public static void main(String[] args) {

        int[] A = {2,4,6,8,10,12,14,16};
        int[] B = new int[8];

        for(int i = 0; i < 8; i++){
            B[i] = A[i] * 3;
        }

        for(int i = 0; i < 8; i++){
            System.out.print(B[i] + " ");
        }
    }
}
