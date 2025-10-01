class Solution {
public:
    bool checkValidString(string s) {
        int left = 0;
        int right = 0;
        int star = 0;
        int opened = 0;
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (c == '(') {
                left++;
                opened++;
            } else if (c == ')') {
                right++;
                opened--;
            } else {
                star++;
                opened--;
            }

            if (left + star < right) {
                return false;
            }

            opened = std::max(opened, 0);
        }

        return opened == 0;
    }
};
