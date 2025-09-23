class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> groups;
        for (int i = 0; i < strs.size(); ++i) {
            std::string key = strs[i];
            std::sort(key.begin(), key.end());

            groups[key].push_back(strs[i]);
        }

        std::vector<std::vector<std::string>> answer;
        for (auto [key, group] : groups) {
            answer.push_back(group);
        }

        return answer;
    }
};
