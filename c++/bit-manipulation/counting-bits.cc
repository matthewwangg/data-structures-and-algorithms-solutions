class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> count(n + 1, 0);
        int previous = 1;
        int next = 2;
        for (int i = 1; i < n + 1; ++i) {
            if (i == next) {
                count[i] = 1;
                previous = next;
                next *= 2;
            } else {
                count[i] = count[i - previous] + 1;
            }
        }
        return count;
    }
};
