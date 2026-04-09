import java.util.Scanner;

public class Estoque {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nome;
        int quantidade;
        double preco;

        // Entrada
        System.out.print("Digite o nome do produto: ");
        nome = scanner.nextLine();

        System.out.print("Digite a quantidade em estoque: ");
        quantidade = scanner.nextInt();

        System.out.print("Digite o preço do produto: ");
        preco = scanner.nextDouble();

        // Validação
        if (quantidade < 0) {
            System.out.println("Erro: A quantidade não pode ser negativa. Tente novamente.");
        } else {
            // Saída
            System.out.println("\nProduto cadastrado com sucesso!");
            System.out.println("Nome: " + nome);
            System.out.println("Quantidade: " + quantidade);
            System.out.println("Preço: R$ " + preco);
        }

        scanner.close();
    }
}
