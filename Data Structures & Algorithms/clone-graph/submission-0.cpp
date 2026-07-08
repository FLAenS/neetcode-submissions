/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> h;
    Node* cloneGraph(Node* node) {
        if (!node) return NULL;
        return dfs(node);
    }
    Node* dfs(Node* node) {
        if (h.count(node)) return h[node];
        Node* copy = new Node(node->val);
        h[node] = copy;
        for (Node* next : node -> neighbors) {
            copy->neighbors.push_back(dfs(next));
        }
        return copy;
    }
};
