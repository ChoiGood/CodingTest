#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string s;
    cin >> s;

    int cnt[26] = {0, };

    for (char c : s) {
        cnt[c - 'A']++;
    }

    string result = "";
    string prefix = "";
    string odd_char = "";

    int odd_cnt = 0;
    bool isPelindrome = true;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] % 2 == 0) {
            for (int j = 0; j < cnt[i] / 2; j++) {
                prefix += i + 'A';
            }
        }
        else {
            odd_cnt++;
            odd_char += i + 'A';
            for (int j = 0; j < (cnt[i] - 1) / 2; j++) {
                prefix += i + 'A';
            }
        }

        if (odd_cnt >= 2) {
            isPelindrome = false;
            break;
        }
    }

    result += prefix;
    result += odd_char;

    string subfix = prefix;
    reverse(subfix.begin(), subfix.end());
    result += subfix;

    if (isPelindrome) {
        cout << result << '\n';
    }
    else {
        cout << "I'm Sorry Hansoo\n"; 
    }


    return 0;
}