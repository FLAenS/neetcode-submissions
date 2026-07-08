class Solution {
public:
    int d[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        int cnt = 0;
        for(int i = 0; i < row; i ++) {
            for(int j = 0; j < col; j ++){
                if (grid[i][j] == '1'){
                    dfs(grid, i, j, row, col);
                    cnt ++;
                }
            }
        }
        return cnt;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j, int row, int col){
        if (i < 0 || i >= row || j < 0 || j >= col || grid[i][j] == '0') return;

        grid[i][j] = '0';
        for (int k = 0; k < 4; k ++ ){
            dfs(grid, i+d[k][0], j+d[k][1], row, col);
        }
    }
};
