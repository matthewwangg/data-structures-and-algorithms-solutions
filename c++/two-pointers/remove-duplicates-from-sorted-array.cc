class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        if (check_palindrome(s, left, right)) {
            return true;
        }

        int new_left = left + 1;
        int new_right = right - 1;

        return check_palindrome(s, new_left, right) || check_palindrome(s, left, new_right);
    }

private:
    bool check_palindrome(std::string& s, int& left, int& right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
};
