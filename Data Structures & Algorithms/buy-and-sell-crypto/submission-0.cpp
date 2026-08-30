class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int p = 0;
        for (int i = 1 ; i < prices.size(); i ++) {
            if (prices[i] > prices[l]) {
                p = max(p, prices[i] - prices[l]);
            }
            else {
                l = i;
            }
        }
        return p;
    }
};
