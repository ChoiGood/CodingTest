#include <iostream>
#include <cmath>

using namespace std;


// 개별 n에 대해 구하는 방법
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long n;
    cin >> n;
    long result = n;

    for (long p = 2; p <= sqrt(n); p++) {   // 제곱근까지만 진행
        if (n % p == 0) {   // p가 소인수인지 확인
            result = result - result / p;   // 결과값 업데이트
            // 해당 소인수 지우기 (2^7*11 이라면 2^7 없애고 11만 남김)
            while (n % p == 0) {
                n /= p;
            }
        }
    }

    if (n > 1) {  // 아직 소인수 구성이 남아있는 경우
        // 반복문에서 제곱근까지만 탐색했기 때문에 1개의 소인수가 누락되는 케이스
        result = result  - result / n;
    }
    cout << result << "\n";

    return 0;
}

// // 에라토스테네스 체 방식 (범위 전체 구하기)
// #include <iostream>
// #include <vector>

// using namespace std;

// int main()
// {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N;
//     cin >> N;

//     vector<int> phi(N + 1);
//     for (int i = 0; i <= N; i++) {
//         phi[i] = i;     // 초기화 
//     }

//     for (int i = 2; i <= N; i++) {
//         if (phi[i] == i) {  // i 가 소수라면
//             for (int j = i; j <= N; j += i) {
//                 phi[j] -= phi[j] / i;       // 배수들에 대해 갱신
//             }
//         }
//     }

//     // 예시 출력
//     for (int i = 1; i <= N; i++) {
//         cout << "phi(" << i << ") = " << phi[i] << "\n";
//     }

//     return 0;
// }