#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int value;
    vector<int> arr;

    while (cin >> value) {
        arr.push_back(value);
    }
    arr.insert(arr.begin(), -1);

    int max_index = max_element(arr.begin(), arr.end()) - arr.begin();

    cout << arr[max_index] << "\n" << max_index;    
    
    return 0;
}