#include <iostream>
#include <queue>

using namespace std;

void BFS(int start, int adj[][5], int V) {
    bool visited[5] = {false};  
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int i = 0; i < V; i++) {
            if (adj[node][i] == 1 && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main() {
    int V = 5; 
    int adj[5][5] = { 
        {0, 1, 1, 0, 0},
        {1, 0, 0, 1, 1},
        {1, 0, 0, 0, 0},
        {0, 1, 0, 0, 0},
        {0, 1, 0, 0, 0}
    };

    cout << "BFS starting from node 0: ";
    BFS(0, adj, V);

    return 0;
}
