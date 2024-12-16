#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool GoodWord(const string& input)
{
    stack<char> st;

    for(char c : input) {
        if (st.size() == 0) {
            st.push(c);
        }
        else {
            if (st.top() == c) {
                st.pop();
            }
            else {
                st.push(c);
            }
        }
    }

    return st.size() == 0;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        if(GoodWord(s)) {
            cnt++;
        }
    }

    cout << cnt << '\n';

    return 0;
}