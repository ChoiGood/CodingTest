#include <iostream>
#include <string>

using namespace std;

int main()
{
    
    string A, B;
    cin >> A >> B;

    cout << stoi(A) * (B[2] - '0') << endl;
    cout << stoi(A) * (B[1] - '0') << endl;
    cout << stoi(A) * (B[0] - '0') << endl;
    cout << stoi(A) * stoi(B);
    
    return 0;
}