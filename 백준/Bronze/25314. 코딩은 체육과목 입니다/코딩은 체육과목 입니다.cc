#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;

    string answer = "";
    for (int i = 0; i < N / 4; i++) {
        answer += "long ";
    }
    answer += "int";

    cout << answer;

    return 0;
}