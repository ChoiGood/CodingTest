#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<bool> isPass(31, false);

    for (int i = 0; i < 28; i++) {
        int attendNumber;
        cin >> attendNumber;

        isPass[attendNumber] = true;
    }

    for (int i = 1; i <= 30; i++) {
        if(!isPass[i])
            cout << i << "\n";
    }

    return 0;
}