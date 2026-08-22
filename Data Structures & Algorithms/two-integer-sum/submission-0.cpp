class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> preMap;
        for (int i = 0; i < nums.size(); i ++ ){
            int diff = target - nums[i];
            if (preMap.find(diff) != preMap.end()){
                return {preMap[diff], i};
            }
            preMap.insert({nums[i], i});
        }
        return {};
    }
};
