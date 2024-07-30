#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> arr(N + 1, 0);

    for (int t1 = 0; t1 < M; t1++) {
        int i, j, k;
        cin >> i >> j >> k;
        for (int tmp = i; tmp <= j; tmp++) {
            arr[tmp] = k;
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}