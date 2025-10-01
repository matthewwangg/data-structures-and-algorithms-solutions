class Solution {
public:
    vector<int> partitionLabels(string s) {
        std::unordered_map<char, int> last_index;
        for (int i = 0; i < s.size(); ++i) {
            last_index[s[i]] = i;
        }
        
        std::vector<int> partitions = {};
        int start = 0;
        int end = 0;
        for (int i = 0; i < s.size(); ++i) {
            end = std::max(end, last_index[s[i]]);
            if (i == end) {
                partitions.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return partitions;
    }
};
