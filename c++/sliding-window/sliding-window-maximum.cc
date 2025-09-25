class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        std::priority_queue<std::pair<int, int>> pq;
        std::vector<int> answer;

        int left = 0;
        for (int i = 0; i < nums.size(); ++i) {
            pq.push(std::make_pair(nums[i], i));

            if (i < k - 1) {
                continue;
            }

            int maximum = std::numeric_limits<int>::min();
            while (maximum == std::numeric_limits<int>::min()) {
                std::pair<int, int> candidate = pq.top();
                if (candidate.second < left) {
                    pq.pop();
                } else {
                    maximum = candidate.first;
                }
            }
            left += 1;

            answer.push_back(maximum);
        }

        return answer;
    }
};
