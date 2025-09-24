#include <iostream>

using namespace std;

int gcd(int a, int b);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        int result = a * b / gcd(a, b);       
        cout << result << "\n";
    }

    return 0;
}

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    }
}

// int gcd(int a, int b ) {
//     while (b != 0) {    // b가 0이 되면 종료
//         int r = a % b;  // 나머지 계산
//         a = b;          // 작은 수를 큰 수로 이동
//         b = r;          // 나머지를 새로운 b로
//     }
//     return a;           // 마지막 a가 최대 공약수
// }