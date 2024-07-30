#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, X;
    cin >> N >> X;

    vector<int> myList(N);
    
    for (int i = 0; i < N; i++)
        cin >> myList[i];
    
    for (int num : myList) {
        if (num < X)
            cout << num << " ";
    }

    return 0;
}