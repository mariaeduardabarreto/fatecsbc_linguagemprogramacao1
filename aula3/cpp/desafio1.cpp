#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        cout << i << endl;
    }

    string nomes[5] = {"Ana", "Joao", "Maria", "Lucas", "Beatriz"};

    for (int i = 0; i < 5; i++) {
        cout << nomes[i] << endl;
    }

    return 0;
}
