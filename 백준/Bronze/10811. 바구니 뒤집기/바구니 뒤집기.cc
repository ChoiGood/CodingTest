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

    vector<int> arr;

    for (int i = 0; i <= N; i++) {
        arr.push_back(i);
    }

    for (int _ = 0; _ < M; _++) {
        int i, j;
        cin >> i >> j;

        reverse(arr.begin() + i, arr.begin() + j + 1);
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}