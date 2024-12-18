#include <iostream>

using namespace std;

typedef long long ll;

ll Cal(const ll& a, ll b, const ll& c) 
{
    if (b == 1) {
        return a % c;
    }
    
    ll num = Cal(a, b / 2, c) % c;
    if (b % 2 == 0) {
        return (num * num) % c;
    }
    else {
        return ((a % c) * ((num * num) % c)) % c;
    }
}

int main()
{
    ll a, b, c;
    cin >> a >> b >> c;
    
    cout << Cal(a, b, c) << '\n';
    return 0;
}