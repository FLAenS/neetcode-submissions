class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> para =  {
            {'}', '{'},
            {')', '('},
            {']', '['}
        };

        for (char c: s) {
            if (para.count(c)) {
                if (!stack.empty() && stack.top() == para[c]) {
                    stack.pop();
                } else {return false;}
            } else {
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
