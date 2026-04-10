#include <iostream>
using namespace std;

void exibirCabecalho() {
    cout << "====== SORVETERIA DO DENER ======" << endl;
}

string verificarEstoqueCritico(int quantidade) {
    if (quantidade < 5) {
        return " [REPOSICAO NECESSARIA]";
    }
    return "";
}

int main() {
    string nomes[100];
    int quantidades[100];
    int total = 0;
    int opcao;

    while (true) {
        exibirCabecalho();
        cout << "1 - Adicionar produto\n2 - Listar\n3 - Sair\n";
        cin >> opcao;

        if (opcao == 1) {
            cout << "Produto: ";
            cin >> nomes[total];
            cout << "Quantidade: ";
            cin >> quantidades[total];
            total++;
        }
        else if (opcao == 2) {
            for (int i = 0; i < total; i++) {
                cout << "Produto: " << nomes[i]
                     << " | Estoque: " << quantidades[i]
                     << verificarEstoqueCritico(quantidades[i]) << endl;
            }
        }
        else if (opcao == 3) {
            break;
        }
    }

    return 0;
}
