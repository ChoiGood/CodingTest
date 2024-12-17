#include<iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    int a[15001];
    for(int i = 0; i < N; i++) {
        cin >> a[i];
    }

    int cnt = 0;
    for(int i = 0; i < N; i++) {
        for(int j = i + 1; j < N; j++) {
            if (a[i] + a[j] == M)
                cnt++;
        }
    }

    cout << cnt;

    return 0;
}