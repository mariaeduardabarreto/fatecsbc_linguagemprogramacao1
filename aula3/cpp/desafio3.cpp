#include <iostream>
using namespace std;

int main() {
    float soma = 0, nota;

    for (int i = 0; i < 5; i++) {
        cout << "Digite a nota: ";
        cin >> nota;
        soma += nota;
    }

    cout << "Média: " << soma / 5 << endl;
    return 0;
}
