class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        merge_sort(nums, 0, nums.size() - 1);

        return nums;
    }

private:
    void merge_sort(std::vector<int>& nums, int left, int right) {
        if (right <= left) {
            return;
        }
        
        int middle = left + int((right - left) / 2);

        merge_sort(nums, left, middle);
        merge_sort(nums, middle + 1, right);

        merge(nums, left, middle+1, right);
    }

    void merge(std::vector<int>& nums, int first, int second, int end) {
        std::vector<int> buffer = {};
        int start = first;
        int mid = second - 1;
        while (first <= mid || second <= end) {
            if (first > mid) {
                buffer.push_back(nums[second]);
                second++;
            } else if (second > end) {
                buffer.push_back(nums[first]);
                first++;
            } else if (nums[first] < nums[second]) {
                buffer.push_back(nums[first]);
                first++;
            } else {
                buffer.push_back(nums[second]);
                second++;
            }
        }

        for (int i = start; i <= end; ++i) {
            nums[i] = buffer[i - start];
        }
    }
};
