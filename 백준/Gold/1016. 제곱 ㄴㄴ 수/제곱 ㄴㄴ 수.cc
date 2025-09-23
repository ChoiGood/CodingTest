#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long Min, Max;
    cin >> Min >> Max;
    // 최댓값과 최솟값의 차이만큼 배열 선언
    vector<bool> Check(Max - Min + 1);

    // 의 제곱수인 4부터 max 보다 작거나 같은 값까지 반복
    for (long i = 2; i * i <= Max; i++) {
        long pow = i * i;  // 제곱수
        long start_index = Min / pow;

        if (Min % pow != 0) {
            // 나머지가 있으면 1을 더해주어야 Min보다 큰 제곱수부터 시작됨
            start_index++;
        }
        for(long j = start_index; pow * j <= Max; j++) {  // 제곱수를 true로 변경
            Check[(int)((j * pow) - Min)] = true;
        }
    }

    int count = 0;

    for (int i = 0; i <= Max - Min; i++) {
        if(!Check[i]) {
            count++;
        }
    }

    cout << count << "\n";

    return 0;
}