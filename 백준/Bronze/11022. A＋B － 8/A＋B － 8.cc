#include <iostream>

using namespace std;

int main()
{
    int T, A, B;
    scanf("%d", &T);
    
    for (int testcase = 1; testcase <= T; testcase++)
    {
        scanf("%d %d", &A, &B);
        printf("Case #%d: %d + %d = %d\n", testcase, A, B, A + B);
    }

    return 0;
}