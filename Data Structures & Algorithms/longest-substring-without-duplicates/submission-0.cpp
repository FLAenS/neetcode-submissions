class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> res;
        int l = 0, ans = 0;
        for(int r = 0; r < s.size(); r ++) {
            while(res.find(s[r]) != res.end()) {
                res.erase(s[l]);
                l ++ ;
            }
            res.insert(s[r]);
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};
