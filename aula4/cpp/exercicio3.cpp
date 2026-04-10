#include <iostream>
using namespace std;

int main() {
    int A[15], B[15];

    for(int i = 0; i < 15; i++){
        cout << "Digite um número: ";
        cin >> A[i];
    }

    for(int i = 0; i < 15; i++){
        B[i] = A[i] * A[i];
    }

    for(int i = 0; i < 15; i++){
        cout << "A: " << A[i] << " B: " << B[i] << endl;
    }

    return 0;
}
