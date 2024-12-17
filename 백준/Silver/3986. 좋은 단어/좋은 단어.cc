#include <iostream>
#include <string>
#include <stack>

using namespace std;

int n, ret;
string s;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        stack<char> st;
        for (char c : s) {
            if(st.size() && st.top() == c)
                st.pop();
            else
                st.push(c);
        }

        if(st.size() == 0)
            ret++;
    }

    cout << ret << '\n';

    return 0;
}