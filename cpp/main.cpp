#include <iostream>
using namespace std;

int main() {
    float num1, num2, resultado;
    char operacao;

    cout << "Digite o primeiro número: ";
    cin >> num1;

    cout << "Digite o segundo número: ";
    cin >> num2;

    cout << "Digite a operação (+, -, *, /): ";
    cin >> operacao;

    if (operacao == '+') {
        resultado = num1 + num2;
        cout << "Resultado: " << resultado;
    } else if (operacao == '-') {
        resultado = num1 - num2;
        cout << "Resultado: " << resultado;
    } else if (operacao == '*') {
        resultado = num1 * num2;
        cout << "Resultado: " << resultado;
    } else if (operacao == '/') {
        if (num2 != 0) {
            resultado = num1 / num2;
            cout << "Resultado: " << resultado;
        } else {
            cout << "Erro: divisão por zero";
        }
    } else {
        cout << "Operação inválida";
    }

    return 0;
}
