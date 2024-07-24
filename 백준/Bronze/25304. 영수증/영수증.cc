#include <iostream>

using namespace std;

int main()
{
    int X, N;
    cin >> X >> N;

    int tmp_sum = 0;

    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        tmp_sum += a * b;
    }

    string answer = (tmp_sum == X) ? "Yes" : "No";
    cout << answer;

    return 0;
}