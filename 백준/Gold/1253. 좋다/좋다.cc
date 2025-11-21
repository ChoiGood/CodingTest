#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    int cnt = 0;
    for (int k = 0; k < N; k++) {
        int find = A[k];

        int i = 0, j = N - 1;

        while (i < j) {  // 투 포인터 알고리즘.
            if (A[i] + A[j] == find) {
                if (i != k && j != k) {
                    cnt++;
                    break;
                }
                else if (i == k) {
                    i++;
                }
                else if (j == k) {
                    j--;
                }
            }
            else if (A[i] + A[j] < find) {
                i++;
            }
            else {
                j--;
            }
        }
    }

    cout << cnt << "\n";

    return 0;
}