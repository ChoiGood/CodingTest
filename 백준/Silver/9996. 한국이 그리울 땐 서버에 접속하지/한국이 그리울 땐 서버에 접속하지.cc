#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<string> Split(string &input, string delimeter) {
    vector<string> result;

    auto start = 0;
    auto end = input.find(delimeter);

    while (end != string::npos) {
        result.push_back(input.substr(start, end - start));
        start = end + delimeter.size();
        end = input.find(delimeter, start);
    }

    result.push_back(input.substr(start));
    return result;
}

int main()
{   
    int N;
    cin >> N;
    
    vector<string> patterns;
    string bufferflush, fildName;
    
    getline(cin, bufferflush);
    getline(cin, fildName);

    patterns = Split(fildName, "*");

    reverse(patterns[1].begin(), patterns[1].end());    

    for (int i = 0; i < N; i++) {
        string str;
        getline(cin, str);

        string reverse_str = str;
        reverse(reverse_str.begin(), reverse_str.end());
        
        if (str.size() >= (patterns[0].size() + patterns[1].size()) &&(str.find(patterns[0]) == 0) && (reverse_str.find(patterns[1]) == 0)) {
            cout << "DA" << '\n';
        }
        else {
            cout << "NE" << '\n';
        }
    }

    return 0;
}