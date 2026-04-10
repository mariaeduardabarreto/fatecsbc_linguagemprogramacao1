int main() {
    float A[20], B[20], C[20];

    for(int i = 0; i < 20; i++){
        cout << "Digite A: ";
        cin >> A[i];
    }

    for(int i = 0; i < 20; i++){
        cout << "Digite B: ";
        cin >> B[i];
    }

    for(int i = 0; i < 20; i++){
        C[i] = A[i] - B[i];
    }

    for(int i = 0; i < 20; i++){
        cout << C[i] << " ";
    }

    return 0;
}
