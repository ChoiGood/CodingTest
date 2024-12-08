#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N = 9;
    int sum = 0;
    vector<int> v(N);

    for (int i = 0; i < N; i++) {
        cin >> v[i];
        sum += v[i];
    }

    sort(v.begin(), v.end());

    int diff = sum - 100;
    int lier1, lier2;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (v[i] + v[j] == diff) {
                lier1 = i;
                lier2 = j;
            }
        }
    }

    for(int i = 0; i < N; i++) {
        if (i == lier1 || i == lier2)
            continue;

        cout << v[i] << '\n';
    }

    return 0;
}