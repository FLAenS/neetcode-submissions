class Solution {
public:
    int d[4][2] = {{1,0}, {-1,0}, {0,1},{0,-1}};
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        int cnt = 0;
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j ++ ){
                if (grid[i][j] == '1'){
                    bfs(grid, i, j, row, col);
                    cnt ++;
                }
            }
        }
        return cnt;
    }

    void bfs(vector<vector<char>>& grid, int i, int j, int row, int col){
        queue<pair<int, int>> q;
        grid[i][j] = '0';
        q.push({i, j});

        while(!q.empty()) {
            auto node = q.front();
            q.pop();
            int x = node.first, y = node.second;
            for (int k = 0; k < 4; k ++){
                int nx = x + d[k][0];
                int ny = y + d[k][1];
                if (nx >= 0 && ny >= 0 && nx < row && ny < col && grid[nx][ny] == '1'){
                    q.push({nx, ny});
                    grid[nx][ny] = '0';
                }
            }
        }
    }
};
