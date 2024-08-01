#include <iostream>
#include <string>

using namespace std;

int main()
{
    char a[100];
    int b[26] = {0}, i = 0;
    scanf("%s", a);
    
    while(a[i]) {
        if(b[a[i] - 97] == 0)
            b[a[i] - 97] = i + 1;
        i++;
    }

    for (i = 0; i < 26; i++) {
        printf("%d ", b[i] - 1);
    }

    return 0;
}