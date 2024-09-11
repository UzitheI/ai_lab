#include <iostream>
#include <queue>
#include <cstring> // For memset

using namespace std;

#define V 6

int h[V] = {6, 4, 7, 2, 3, 0}; 

struct Node {
    int id;      
    int cost;     

    // Constructor to initialize Node
    Node(int i, int c) : id(i), cost(c) {}

    bool operator>(const Node& other) const {
        return (cost + h[id]) > (other.cost + h[other.id]);
    }
};

void aStarSearch(int start, int goal, int graph[V][V]) {

    priority_queue<Node, vector<Node>, greater<Node> > pq;

    bool visited[V];
    memset(visited, false, sizeof(visited));

    int parent[V];
    memset(parent, -1, sizeof(parent));

    pq.push(Node(start, 0));

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();

        if (current.id == goal) {
            cout << "Path to goal: ";
            int node = goal;
            while (node != -1) {
                cout << node << " ";
                node = parent[node];
            }
            cout << "\nTotal cost: " << current.cost << endl;
            return;
        }

        if (visited[current.id]) continue;
        visited[current.id] = true;

        for (int neighbor = 0; neighbor < V; neighbor++) {
            if (graph[current.id][neighbor] && !visited[neighbor]) {

                int newCost = current.cost + graph[current.id][neighbor];

                pq.push(Node(neighbor, newCost));

                parent[neighbor] = current.id;
            }
        }
    }

    cout << "No path found to the goal!" << endl;
}

int main() {
    int graph[V][V] = {
        {0, 1, 1, 0, 0, 0},  // Node 0 connected to 1, 2
        {1, 0, 0, 4, 3, 0},  // Node 1 connected to 0, 3, 4
        {1, 0, 0, 0, 2, 0},  // Node 2 connected to 0, 4
        {0, 4, 0, 0, 1, 5},  // Node 3 connected to 1, 4, 5
        {0, 3, 2, 1, 0, 2},  // Node 4 connected to 1, 2, 3, 5
        {0, 0, 0, 5, 2, 0}   // Node 5 (Goal) connected to 3, 4
    };

    int start = 0;  
    int goal = 5;   
    aStarSearch(start, goal, graph);

    return 0;
}
