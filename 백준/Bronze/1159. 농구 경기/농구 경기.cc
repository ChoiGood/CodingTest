#include <iostream>
#include <string>

using namespace std;

int main()
{
    string word, ret;
    int N;
    cin >> N;
    int cnt[26] = {0, };

    for (int i = 0; i < N; i++) {
        cin >> word;
        cnt[word[0] - 'a']++;
    }

    for(int i = 0; i < 26; i++) {
        if (cnt[i] >= 5)
            ret += (i + 'a');
    }

    if (ret.size())
        cout << ret << "\n";
    else
        cout << "PREDAJA" << "\n";

    return 0;
}