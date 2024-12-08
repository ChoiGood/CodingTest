#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string str;
    cin >> str;

    string str_copy(str);
    reverse(str_copy.begin(), str_copy.end());

    if (str == str_copy) {
        cout << 1;
    } else {
        cout << 0;
    }

    return 0;
}