#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int n, m;
vector<int> armorIds;
int cnt;

void dfs(int start, vector<int> &v) {
    if (v.size() == 2) {
        int sum = 0;
        for (auto i : v) 
            sum += armorIds[i];

        if (sum == m)
            cnt++;
            
        return;
    }

    for (int i = start; i < n; i++) {
        v.push_back(i);
        dfs(i + 1, v);
        v.pop_back();
    }
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        armorIds.push_back(temp);
    }

    vector<int> v;
    dfs(0, v);

    cout << cnt;

    return 0;
}