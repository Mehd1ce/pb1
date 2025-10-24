#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Matrisin olcusunu daxil et: ";
    cin >> n;

    int A[100][100];

    cout << "Matris elementlerini daxil et:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }

    bool simmetrik = true;  // əvvəlcə simmetrik olduğunu fərz edirik

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (A[i][j] != A[j][i]) {
                simmetrik = false;
                break;
            }
        }
        if (!simmetrik) break;
    }

    if (simmetrik)
        cout << "Matris simmetrikdir." << endl;
    else
        cout << "Matris simmetrik deyil." << endl;

    return 0;
}