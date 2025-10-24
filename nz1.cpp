#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Matrisin olcusunu daxil et (n): ";
    cin >> n;

    int A[100][100], B[100][100];

    cout << "Matris elementlerini daxil et:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }

    // Transpoz (ters) matris hesablamaq
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            B[i][j] = A[j][i];
        }
    }

    cout << "\nTers (transpoz) matris:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << B[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}