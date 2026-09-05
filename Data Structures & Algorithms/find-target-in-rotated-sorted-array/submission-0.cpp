class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() -1;
        while (l < r) {
            int m = (l + r)/2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        int p = l;
        int res = bsearch(nums, target, 0, p - 1);
        if (res != -1) {
            return res;
        }
        return bsearch(nums, target, p, nums.size() - 1);
    }

    int bsearch(vector<int>& nums, int target, int l, int r){
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target){
                return mid;
            } else if(nums[mid] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }
};
