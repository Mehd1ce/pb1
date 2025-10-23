#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nece eded daxil edeceksiniz? ";
    cin >> n;

    int arr[100]; // maksimum 100 element
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int min = arr[0], max = arr[0];

    // min və max tapmaq
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }

    // qalanları 0 etmək
    for (int i = 0; i < n; i++) {
        if (arr[i] != min && arr[i] != max)
            arr[i] = 0;
    }

    // nəticəni çap etmək
    cout << "Netice: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0;
}
