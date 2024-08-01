#include <iostream>
#include <string>

using namespace std;

int main()
{
    string word;
    cin >> word;

    for (char ch = 'a'; ch <= 'z'; ch++) {
        int idx = word.find(ch);

        if (idx == string::npos)
            cout << -1 << " ";
        else
            cout << idx << " ";
    }

    return 0;
}