#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

map<char, int> alpabet_mp;
vector<int> v;

void Init() {
    string alpabets = "abcdefghijklmnopqrstuvwxyz";
    int n = alpabets.size();
    v.resize(n, 0);

    int idx = 0;
    for (int i = 0; i < n; i++) {
        alpabet_mp[alpabets[i]] = idx++;
    }
}


int main() 
{
    Init();

    string S; 
    cin >> S;

    for (int i = 0; i < S.size(); i++) {
        v[alpabet_mp[S[i]]]++;
    }

    for (int i : v) cout << i << " ";

    return 0;
}