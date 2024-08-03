#include <iostream>
#include <vector>

using namespace std;

int main()
{

    vector<int> whiteChessPieces = {1, 1, 2, 2, 2, 8};
    vector<int> myPieces;
    
    int n;
    while (cin >> n) {
        myPieces.push_back(n);
    }

    for (int i = 0; i < 6; i++) {
        cout << whiteChessPieces[i] - myPieces[i] << " ";
    }

    return 0;
}