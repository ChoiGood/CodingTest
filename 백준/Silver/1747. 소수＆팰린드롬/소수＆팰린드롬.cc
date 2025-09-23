#include <iostream>
#include <cmath>
#include <string>

using namespace std;

bool isPalindrome(int target);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long N;
    cin >> N;
    long A[10000001];

    for (int i = 2; i < 10000001; i++) {
        A[i] = i;
    }
    for (int i = 2; i <= sqrt(10000001); i++) { // 제곱근까지만 수행
        if (A[i] == 0) {
            continue;
        }
        for (int j = i + i; j < 10000001; j = j + i) {  // 배수 지우기
            A[j] = 0;
        }
    }

    int i = N;

    while (true) {  // N부터 1씩 증가하면서 소수와 팰린드롬 수가 맞는지 확인
        if (A[i] != 0) {
            int result = A[i];
            if (isPalindrome(result)) {
                cout << result << "\n";
                break;
            }
        }
        i++;
    }


    return 0;
}

bool isPalindrome(int target) {  // 팰린드롬 수 판별 함수
    string temp_str = to_string(target);    // 숫자를 문자열로 변환
    char const* temp = temp_str.c_str();    // 문자열을 배열로 변환
    int s = 0;
    int e = temp_str.size() - 1;

    while (s < e) {
        if (temp[s] != temp[e]) {
            return false;
        }
        s++;
        e--;
    }
    return true;
}