#include <iostream>
using namespace std;

int main() {
    int A[8] = {2,4,6,8,10,12,14,16};
    int B[8];

    for(int i = 0; i < 8; i++){
        B[i] = A[i] * 3;
    }

    for(int i = 0; i < 8; i++){
        cout << B[i] << " ";
    }

    return 0;
}
