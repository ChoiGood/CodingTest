#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, v;
    cin >> N;

    vector<int> myList(N);

    for (int i = 0; i < N; i++) {
        cin >> myList[i];
    }

    cin >> v;
    cout << count(myList.begin(), myList.end(), v);
}