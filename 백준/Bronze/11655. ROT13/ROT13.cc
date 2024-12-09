#include <iostream>
#include <string>

using namespace std;

int main()
{
    string S;
    getline(cin, S);

    string result = "";

    for (char c : S) {
        if (c >= 'A' && c <= 'Z') {
            result += char((((c - 'A') + 13 ) % 26) + 'A');
        }
        else if (c >= 'a' && c <= 'z') {
            result += char((((c - 'a') + 13 ) % 26) + 'a');
        } else {
            result += c;
        }
    }

    cout << result << endl;

    return 0;
}