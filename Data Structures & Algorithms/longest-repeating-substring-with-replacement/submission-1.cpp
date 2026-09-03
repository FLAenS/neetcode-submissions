class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0;
        unordered_set<char> cset(s.begin(), s.end());

        for (char c: cset) {
            int cnt = 0, l = 0;
            for (int r = 0; r < s.size(); r ++ ){
                if (s[r] == c) cnt ++;
                while ((r - l + 1) - cnt > k) {
                    if (s[l] == c) cnt --;
                    l ++ ;
                }
                res = max(res, r - l + 1);
            }
        }
        return res;
    }
};
