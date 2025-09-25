class Solution {
public:
    string minWindow(string s, string t) {
        std::string answer = "";

        std::unordered_map<char, int> count;
        std::unordered_set<char> required_chars;
        for (char c : t) {
            count[c] += 1;
            required_chars.insert(c);
        }

        int left = 0;
        int required = required_chars.size();
        for (int i = 0; i < s.size(); ++i) {
            count[s[i]] -= 1;
            if (count[s[i]] == 0) {
                required -= 1;
                
                while (required == 0) {
                    count[s[left]] += 1;
                    if (count[s[left]] > 0) {
                        if (answer == "" || i - left + 1 < answer.size()) {
                            answer = s.substr(left, i - left + 1);
                        }
                        required += 1;
                    }
                    left += 1;
                }
            }
        }

        return answer;
    }
};
