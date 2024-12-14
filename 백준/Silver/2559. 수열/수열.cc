#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;

    vector<int> v(N + 1, 0);
    vector<int> s(N + 1, 0);

    for (int i = 1; i <= N; i++) {
        cin >> v[i];
        s[i] = s[i - 1] + v[i];
    }

    int maxTemp = -999999999;

    for (int i = K; i <= N; i++) {
        int curTemp = s[i] - s[i - K];
        if (maxTemp < curTemp) {
            maxTemp = curTemp;
        }
    }

    cout << maxTemp << endl;

    return 0;
}