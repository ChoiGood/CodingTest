#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    string s, ori_s, pre, suf;
    cin >> ori_s;

    int pos = ori_s.find('*');
    pre = ori_s.substr(0, pos);
    suf = ori_s.substr(pos + 1);

    for (int i = 0; i < n; i++) {
        cin >> s;

        if (s.size() >= pre.size() + suf.size() && pre == s.substr(0, pre.size()) && suf == s.substr(s.size() - suf.size())) {
            cout << "DA\n";
        }
        else {
            cout << "NE\n";
        }
    }

    return 0;
}