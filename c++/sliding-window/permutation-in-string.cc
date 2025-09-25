class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> count;
        for (char c : s1) {
            count[c] += 1;
        }

        int left = 0;
        for (int i = 0; i < s2.size(); ++i) {
            count[s2[i]] -= 1;

            if (count[s2[i]] == 0) {
                int zero = true;
                for (auto [ch, counter] : count) {
                    if (counter != 0) {
                        zero = false;
                        break;
                    }
                }

                if (zero) {
                    return true;
                }
            } else {
                while (count[s2[i]] < 0) {
                    count[s2[left]] += 1;
                    left += 1;
                }
            }
        }
        return false;
    }
};
