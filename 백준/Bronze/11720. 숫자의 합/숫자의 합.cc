#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    string numbers;

    cin >> N >> numbers;

    int sum = 0;

    for (char num : numbers) {
        sum += num - '0';
    }

    cout << sum;
}