#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<int> arr(N);
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int maxValue = *max_element(arr.begin(), arr.end());
    int minValue = *min_element(arr.begin(), arr.end());

    cout << minValue << " " << maxValue;

    return 0;
}