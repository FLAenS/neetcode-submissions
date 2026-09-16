class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1;
        int p = 0;
        while(r < prices.size()) {
            if (prices[l] < prices[r]) {
                p = max(p, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r ++ ;
        }
        return p;
    }
};
