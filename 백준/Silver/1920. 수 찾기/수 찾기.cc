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

    vector<int> A;
    for(int i = 0; i < N; i++) {
        int num;
        cin >> num;
        A.push_back(num);
    }

    sort(A.begin(), A.end());

    int M;
    cin >> M;

    for (int k = 0; k < M; k++) {
        int find;
        cin >> find;

        // 이진 탐색 (while문으로 구현)
        int i = 0, j = N - 1;
        bool isFind = false;

        while (i <= j) {
            int mid = (i + j) / 2;

            if (A[mid] == find) {
                isFind = true;
                break;
            }
            else if (A[mid] > find) {
                j = mid - 1;
            }
            else {  // A[mid] < find
                i = mid + 1;
            }
        }

        if (isFind) {
            cout << 1 << "\n";
        }
        else {
            cout << 0 << "\n";
        }
    }

    return 0;
}