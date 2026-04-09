#include <iostream>
using namespace std;

int main() {
    string nome;
    int quantidade;
    float preco;

    // Entrada
    cout << "Digite o nome do produto: ";
    cin >> nome;

    cout << "Digite a quantidade em estoque: ";
    cin >> quantidade;

    cout << "Digite o preço do produto: ";
    cin >> preco;

    // Validação
    if (quantidade < 0) {
        cout << "Erro: A quantidade não pode ser negativa. Tente novamente.";
    } else {
        // Saída
        cout << "\nProduto cadastrado com sucesso!\n";
        cout << "Nome: " << nome << endl;
        cout << "Quantidade: " << quantidade << endl;
        cout << "Preço: R$ " << preco << endl;
    }

    return 0;
}
