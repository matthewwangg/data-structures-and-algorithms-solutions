class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_count;
        std::unordered_map<char, int> t_count;
        std::unordered_set<char> chars;

        for (char c : s) {
            s_count[c] += 1;
            chars.insert(c);
        }

        for (char c : t) {
            t_count[c] += 1;
            chars.insert(c);
        }

        for (char c : chars) {
            if (s_count[c] != t_count[c]) {
                return false;
            }
        }
        return true;
    }
};
