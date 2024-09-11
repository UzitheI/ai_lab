#include <iostream>

using namespace std;

void DFSUtil(int node, int adj[][5], bool visited[], int V) {
    visited[node] = true;
    cout << node << " ";


    for (int i = 0; i < V; i++) {
        if (adj[node][i] == 1 && !visited[i]) {
            DFSUtil(i, adj, visited, V);
        }
    }
}

void DFS(int start, int adj[][5], int V) {
    bool visited[5] = {false};  
    DFSUtil(start, adj, visited, V);
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

    cout << "DFS starting from node 0: ";
    DFS(0, adj, V);

    return 0;
}
