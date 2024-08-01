#include <iostream>
#include <string>

using namespace std;

int main()
{   
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int T;
    cin >> T;

    for (int _ = 0; _ < T; _++) {
        int R; string S;
        cin >> R >> S;

        for (char ch : S) {
            for (int i = 0; i < R; i++) {
                cout << ch;
            }
        }
        cout << "\n";
    }

    return 0;
}