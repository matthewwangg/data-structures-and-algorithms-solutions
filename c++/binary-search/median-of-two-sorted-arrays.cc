class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();

        int left = 0;
        int right = m;

        while (left <= right) {
            int middle_1 = (left + right) / 2;
            int middle_2 = (m + n + 1) / 2 - middle_1;

            int max_left_1 = (middle_1 == 0) ? std::numeric_limits<int>::min() : nums1[middle_1 - 1];
            int min_right_1 = (middle_1 == m) ? std::numeric_limits<int>::max() : nums1[middle_1];
            int max_left_2 = (middle_2 == 0) ? std::numeric_limits<int>::min() : nums2[middle_2 - 1];
            int min_right_2 = (middle_2 == n) ? std::numeric_limits<int>::max() : nums2[middle_2];

            if (max_left_1 <= min_right_2 && max_left_2 <= min_right_1) {
                if ((m + n) % 2 == 0) {
                    return (std::max(max_left_1, max_left_2) + std::min(min_right_1, min_right_2)) / 2.0;
                } else {
                    return max(max_left_1, max_left_2);
                }
            }

            if (max_left_1 > max_left_2) {
                right = middle_1 - 1;
            } else {
                left = middle_1 + 1;
            }
        }
        return 0.0;
    }
};
