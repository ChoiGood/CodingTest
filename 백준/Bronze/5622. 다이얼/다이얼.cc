#include <iostream>
#include <string>

using namespace std;

int main()
{
    string alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string number = "22233344455566677778889999";

    string input;
    cin >> input;

    int time = 0;
    for (char ch : input) {
        int index = alpabet.find(ch);

        if (index != string::npos) {
            time += number[index] - '0' + 1;
        }
    }

    cout << time;
    return 0;
}