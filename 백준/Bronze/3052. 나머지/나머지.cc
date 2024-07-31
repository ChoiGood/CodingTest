#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<bool> check(43, false);

    for (int i = 0; i < 10; i ++) {
        int tmp; 
        cin >> tmp;
        check[tmp % 42] = true;
    }

    cout << count(check.begin(), check.end(), true);

    return 0;
}