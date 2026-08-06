class Solution {
public:
    int dir[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        int cnt = 0;
        for (int i = 0; i < row; i ++){
            for (int j = 0; j < col; j ++ ){
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    cnt ++;
                }
            }
        }
        return cnt;
    }

    void dfs(vector<vector<char>>& grid, int i, int j) {
        int row = grid.size(), col = grid[0].size();
        if (i < 0 || j < 0 || i >= row || j >= col || grid[i][j] == '0') return;

        grid[i][j] = '0';
        for(int k = 0; k < 4; k ++){
            dfs(grid, i + dir[k][0], j + dir[k][1]);
        }
    }
};
