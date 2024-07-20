#include <iostream>

using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;

    int H, M;
    H = (A + (B + C) / 60) % 24;
    M = (B + C) % 60;

    cout << H << " " << M;

    return 0;
}