class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> ext;
        for (int i = 0; i < nums.size(); i ++) {
            if (ext.find(nums[i]) != ext.end()){
                return true;
            }
            ext.insert(nums[i]);
        }
        return false;
    }
};