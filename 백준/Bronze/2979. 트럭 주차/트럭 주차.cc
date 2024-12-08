#include <iostream>

using namespace std;

int cnt[101];

void print() {
    for (int c : cnt) {
        cout << c << " ";
    }
    cout << '\n';
}

int main() 
{
    int A, B, C;
    cin >> A >> B >> C;
    
    int fee[4] = {0, A, B, C};
    
    for (int i = 0; i < 3; i++) {
        int a, b;
        cin >> a >> b;

        for (int j = a; j < b; j++) {
            cnt[j]++;
        }
    }
   
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += fee[cnt[i]] * cnt[i];
    }
    cout << sum;


    return 0;
}