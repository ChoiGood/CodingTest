#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string word;
    cin >> word;

    string reverse_word(word);
    reverse(reverse_word.begin(), reverse_word.end());

    if (word == reverse_word) {
        cout << 1;
    } else {
        cout << 0;
    }


    return 0;
}