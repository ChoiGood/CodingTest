#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;

void DFS(int v);
void BFS(int v);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, start;
    cin >> N >> M >> start;

    graph.resize(N + 1);
    visited.resize(N + 1, false);

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= N; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    DFS(start);
    cout << "\n";
    fill(visited.begin(), visited.end(), false);
    
    BFS(start);

    return 0;
}

void DFS(int v)
{
    visited[v] = true;
    cout << v << " ";

    for (int w : graph[v]) {
        if (!visited[w]) {
            DFS(w);
        }
    }
}

void BFS(int v)
{
    queue<int> myqueue;
    visited[v] = true;
    myqueue.push(v);

    while (!myqueue.empty()) {
        int c_node = myqueue.front();
        myqueue.pop();
        cout << c_node << " ";

        for (int n_node : graph[c_node]) {
            if (!visited[n_node]) {
                myqueue.push(n_node);
                visited[n_node] = true;
            }
        }
    }
}