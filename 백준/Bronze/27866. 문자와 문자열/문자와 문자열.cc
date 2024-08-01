#include <iostream>
#include <string>

using namespace std;

int main()
{
    string word;
    int index;

    cin >> word >> index;
    cout << word[index - 1];

    return 0;
}