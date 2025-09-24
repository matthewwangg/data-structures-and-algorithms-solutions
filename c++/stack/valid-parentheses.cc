class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> parentheses = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        std::vector<char> left_parentheses{'(', '[', '{'};
        std::vector<char> stack;

        for (char c : s) {
            if (std::find(left_parentheses.begin(), left_parentheses.end(), c) != left_parentheses.end()) {
                stack.push_back(c);
            } else {
                if (stack.size() == 0 || parentheses[stack.back()] != c) {
                    return false;
                }
                stack.pop_back();
            }
        }

        return stack.size() == 0;
    }
};
