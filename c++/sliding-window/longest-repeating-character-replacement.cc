class Solution {
public:
    int characterReplacement(string s, int k) {
        std::unordered_map<char, int> count;
        int total_count = 0;
        char most_common_character = ' ';
        int answer = 0;

        int left = 0;
        for (int i = 0; i < s.size(); ++i) {
            count[s[i]] += 1;
            total_count += 1;
            if (!most_common_character || count[s[i]] >= count[most_common_character]) {
                most_common_character = s[i];
            }

            while (total_count - count[most_common_character] > k) {
                count[s[left]] -= 1;
                total_count -= 1;
                left += 1;

                if (s[left] == most_common_character) {
                    break;
                }
            }

            answer = std::max(answer, i - left + 1);
        }

        return answer;
    }
};
