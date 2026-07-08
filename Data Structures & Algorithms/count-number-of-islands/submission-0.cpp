class Solution {
public:
    int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int numIslands(vector<vector<char>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();
        int islands = 0;
        for (int i = 0; i < ROWS; i ++ ){
            for (int j = 0; j < COLS; j ++ ){
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    islands ++ ;
                }
            }
        }

        return islands;
    }

    void dfs(vector<vector<char>>& grid, int i, int j){
        int ROWS = grid.size(), COLS = grid[0].size();
        if (i < 0 || j < 0 || i >= ROWS || j >= COLS || grid[i][j] == '0') {
            return ;
        }
        grid[i][j] = '0';
        for (int k = 0; k < 4; k ++ ){
            dfs(grid, i + direction[k][0], j + direction[k][1]);
        }
    }
};
