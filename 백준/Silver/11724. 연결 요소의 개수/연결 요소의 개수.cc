#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;
void DFS(int v);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    graph.resize(N + 1);
    visited.resize(N + 1, false);

    for(int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int cnt = 0;
    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            cnt++;
            DFS(i);
        }
    }

    cout << cnt;

    return 0;
}

void DFS(int v) {
    visited[v] = true;

    for (int w : graph[v]) {
        if (!visited[w]) {
            DFS(w);
        }
    }
}