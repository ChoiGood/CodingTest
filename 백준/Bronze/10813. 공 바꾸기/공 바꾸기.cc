#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> arr(N + 1, -1);

    for (int i = 1; i <= N; i++) 
        arr[i] = i;
    
    for (int t = 0; t < M; t++) {
        int i, j, temp;
        cin >> i >> j;
        
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}