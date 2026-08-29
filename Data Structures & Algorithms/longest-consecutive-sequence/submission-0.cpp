class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numset(nums.begin(), nums.end());
        int res = 0;
        for (int i : nums){
            if (numset.find(i - 1) == numset.end()) {
                int length = 1;
                while (numset.find(i + length) != numset.end()) {
                    length ++ ;
                }
                res = max(res, length);
            }
        }
        return res;
    }
};
