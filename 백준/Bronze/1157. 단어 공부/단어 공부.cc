#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

bool cmp(const pair<char, int>& v1, const pair<char, int>& v2) {
    if (v1.second == v2.second) {
        return v1.first < v2.first;
    }

    return v1.second > v2.second;
}

int main() 
{
    string word;
    cin >> word;

    // 딕셔너리 카운팅
    map<char, int> m;
    for(int i = 0; i < word.length(); i++) {
        char ch = char(toupper(word[i]));
        if (m.find(ch) != m.end()) {
            m[ch]++;
        } else {
            m[ch] = 1;
        }
    }

    // map 의 value 값을 기준으로 정렬시키기
    // 자료구조 map은 key값을 기준을 정렬되어 집니다.
    // 이를 value 값을 기준으로 정렬시키기 위해서는 아쉽지만 vector로의 변환 이후 정렬이 가능합니다.

    // map을 vector 로 변환.
    // map의 key와 value를 pair 형태를 갖는 vector 로 변경할 수 있습니다.

    vector<pair<char, int>> result(m.begin(), m.end());
    sort(result.begin(), result.end(), cmp);

    if (result.size() == 1) {
        cout << result[0].first;
    } else {
        if (result[0].second == result[1].second) {
            cout << "?";
        } else {
            cout << result[0].first;
        }
    }

    return 0;
}