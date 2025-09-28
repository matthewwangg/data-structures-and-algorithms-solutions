class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());

        std::unordered_map<int, int> last_index;
        for (int i = 0; i < candidates.size(); ++i) {
            last_index[candidates[i]] = i;
        }

        std::vector<std::vector<int>> combinations;
        construct(0, target, {}, combinations, candidates, last_index);

        return combinations;
    }

private:
    void construct(int index, int target, std::vector<int> candidate, std::vector<std::vector<int>>& combinations, std::vector<int>& candidates, std::unordered_map<int, int>& last_index) {
        if (index == candidates.size()) {
            if (target == 0) {
                combinations.push_back(candidate);
            }
            return;
        }

        if (target - candidates[index] >= 0) {
            candidate.push_back(candidates[index]);
            construct(index, target - candidates[index], candidate, combinations, candidates, last_index);
            candidate.pop_back();
        }
        
        construct(last_index[candidates[index]] + 1, target, candidate, combinations, candidates, last_index);
    }
};
