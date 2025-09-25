class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> count;
        int answer = 0;

        int left = 0;
        for (int i = 0; i < s.size(); ++i) {
            count[s[i]] += 1;
            while (count[s[i]] > 1) {
                count[s[left]] -= 1;
                left += 1;
            }
            answer = std::max(answer, i - left + 1);
        }

        return answer;
    }
};
