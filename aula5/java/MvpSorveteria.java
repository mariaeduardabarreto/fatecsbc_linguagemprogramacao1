import java.util.Scanner;

public class MvpSorveteria {

    public static void exibirCabecalho() {
        System.out.println("====== SORVETERIA DO DENER ======");
    }

    public static String verificarEstoqueCritico(int quantidade) {
        if (quantidade < 5) {
            return " [REPOSIÇÃO NECESSÁRIA]";
        }
        return "";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] nomes = new String[100];
        int[] quantidades = new int[100];
        int total = 0;

        while (true) {
            exibirCabecalho();
            System.out.println("1 - Adicionar produto");
            System.out.println("2 - Listar");
            System.out.println("3 - Sair");

            int opcao = sc.nextInt();

            if (opcao == 1) {
                System.out.print("Produto: ");
                nomes[total] = sc.next();
                System.out.print("Quantidade: ");
                quantidades[total] = sc.nextInt();
                total++;
            } else if (opcao == 2) {
                for (int i = 0; i < total; i++) {
                    System.out.println("Produto: " + nomes[i] +
                            " | Estoque: " + quantidades[i] +
                            verificarEstoqueCritico(quantidades[i]));
                }
            } else if (opcao == 3) {
                break;
            }
        }

        sc.close();
    }
}
