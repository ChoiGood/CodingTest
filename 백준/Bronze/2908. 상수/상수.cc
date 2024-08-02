#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string A, B;
    cin >> A >> B;

    reverse(A.begin(), A.end());
    reverse(B.begin(), B.end());

    int iA = stoi(A), iB = stoi(B);
    int answer = (iA > iB) ? iA : iB;

    cout << answer;
    return 0;
}