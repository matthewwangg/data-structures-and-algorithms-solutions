class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0;
        for (int i = 0; i < arr.size(); ++i) {
            if (i >= k) {
                if (std::abs(x - arr[i]) - std::abs(x - arr[left]) < 0 || arr[i] < x) {
                    left++;
                }
            }
        }

        return std::vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
