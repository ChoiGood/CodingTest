#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main() 
{
    int N;
    map<char, int> mp;
    string s = "";

    cin >> N;
    for (int i = 0; i < N; i++) {
        string word;
        cin >> word;

        if (mp[word[0]]) {
            mp[word[0]]++;
        } else {
            mp[word[0]] = 1;
        }
    }

    for(auto it : mp) {
        if (it.second >= 5) {
            s += it.first;
        }
    }

    if (s.size() == 0) {
        cout << "PREDAJA" << endl;
    } else {
        cout << s << endl;
    }

}