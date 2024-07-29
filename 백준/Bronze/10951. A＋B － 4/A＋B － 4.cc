#include <iostream>

using namespace std;

int main()
{
    int A, B;
    
    // while (true)
    // {
    //     cin >> A >> B;
    //     if (cin.eof())
    //         break;
    //     else
    //         cout << A + B << endl;
    // }

    // while (cin >> A >> B) {
    //     cout << A + B << "\n";
    // }

    while (scanf("%d %d", &A, &B) != EOF) {
        printf("%d\n", A + B);
    }

    return 0;
}