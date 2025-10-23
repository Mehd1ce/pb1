#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Matrisin olcusunu daxil edin (n x n): ";
    cin >> n;

    int mat[100][100];

    cout << "Elementleri daxil edin:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mat[i][j];
        }
    }

    bool simmetrik = true;

    // Simmetrik olub olmadigini yoxlamaq
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[j][i]) {
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
