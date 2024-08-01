#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
    string str;
    getline(cin, str);
    

    istringstream ss(str);
    string stringBuffer;
    vector<string> x;
    x.clear();

    while (getline(ss, stringBuffer, ' ')) {
        x.push_back(stringBuffer);
    }

    cout << x.size() - count(x.begin(), x.end(), "");
}