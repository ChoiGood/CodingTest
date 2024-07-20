#include <iostream>
#include <algorithm>

using namespace std;

int main()
{   
    int a, b, c;
    cin >> a >> b >> c;

    if ((a == b) && (a == c)) // 같은 눈 3개
        cout << 10000 + a * 1000;
    else if ((a == b && a != c) | (a == c && a != b)) // 같은 눈 2개
        cout << 1000 + a * 100;
    else if (b == c && a != c) // 같은 눈 2개
        cout << 1000 + b * 100;
    else 
        cout << max({a, b, c}) * 100;

    return 0;
}