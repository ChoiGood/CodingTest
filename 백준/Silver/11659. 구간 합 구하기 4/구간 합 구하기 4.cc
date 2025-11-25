#include <iostream>
#include <vector>

using namespace std;


// 구간합
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> A(N + 1);
    vector<int> S(N + 1, 0);

    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        S[i] = S[i - 1] + A[i];
    }

    for (int i = 0; i < M; i++) {
        int start, end;
        cin >> start >> end;

        cout << S[end] - S[start - 1] << "\n";
    }

    return 0;
}