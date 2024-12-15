#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T;  // 테스트 케이스 수
    cin >> T;

    for (int testcase = 0; testcase < T; testcase++) {
        int n;  // 의상의 수
        cin >> n;

        map<string, int> mp;

        for (int i = 0; i < n; i++) {
            string s1, s2;
            cin >> s1 >> s2;

            if (mp[s2]) {
                mp[s2]++;
            }
            else {
                mp[s2] = 1;
            }
        }

        int cnt = 1;
        for (auto it : mp) {
            cnt *= (it.second + 1);
        }
        cnt--;

        cout << cnt << '\n';
    }


    return 0;
}