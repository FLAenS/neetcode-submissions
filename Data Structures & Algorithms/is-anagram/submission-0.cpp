class Solution {
public:
    bool isAnagram(string s, string t) {
        int l1 = s.length(), l2 = t.length();
        if (l1 != l2)return false;
        unordered_map<char, int> ds;
        unordered_map<char, int> dt;

        for (int i = 0; i < l1; i ++) {
            ds[s[i]] ++ ;
            dt[t[i]] ++ ;
        }
        return ds == dt;
    }
};
