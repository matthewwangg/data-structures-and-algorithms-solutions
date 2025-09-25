class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *std::max_element(piles.begin(), piles.end());

        int answer = std::numeric_limits<int>::max();
        while (left <= right) {
            int middle = (right + left) / 2;
            
            long hours = 0;
            for (int pile : piles) {
                hours += pile / middle;
                if (pile % middle != 0) {
                    hours += 1;
                }
            }

            if (h >= hours) {
                answer = std::min(answer, middle);
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        return answer;
    }
};
