#include <iostream>
#include <string>

using namespace std;

int main()
{
    string X, Y;
    cin >> X >> Y;

    int minCount = 999;

    for (int i = 0; i <= Y.size() - X.size(); i++) {
        int count = 0;
        for (int j = 0; j < X.size(); j++) {
            if (X[j] != Y[i + j]) {
                count += 1;
            }
        }
        if (minCount > count) {
            minCount = count;
        }
    }

    cout << minCount;


    return 0;
}