class Solution {
public:
    vector<vector<string>> partition(string s) {
        std::vector<std::vector<std::string>> partitions;
        std::vector<std::string> partition;
        construct(0, s, partition, partitions);

        return partitions;
    }

private:
    void construct(int index, std::string& s, std::vector<std::string>& partition, std::vector<std::vector<std::string>>& partitions) {
        if (index == s.size()) {
            partitions.push_back(partition);
            return;
        }

        for (int i = index; i < s.size(); ++i) {
            if (std::equal(s.begin() + index, s.begin() + i + 1, s.rbegin() + (s.size() - (i+ 1)))) {
                partition.push_back(s.substr(index, i - index + 1));
                construct(i+1, s, partition, partitions);
                partition.pop_back();
            }
        }
    }
};
