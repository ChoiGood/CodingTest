#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int testcase = 1; testcase <= T; testcase++) {
        int A, B;
        cin >> A >> B;
        cout << "Case #" << testcase << ": " << A + B << "\n";
    }

    return 0;
}