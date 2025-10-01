class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        std::vector<int> merged_triplet = {0, 0, 0};
        for (std::vector<int> triplet : triplets) {
            if (triplet[0] > target[0] || triplet[1] > target[1] || triplet[2] > target[2]) {
                continue;
            }

            merged_triplet[0] = std::max(merged_triplet[0], triplet[0]);
            merged_triplet[1] = std::max(merged_triplet[1], triplet[1]);
            merged_triplet[2] = std::max(merged_triplet[2], triplet[2]);
        }
        return merged_triplet == target;
    }
};
