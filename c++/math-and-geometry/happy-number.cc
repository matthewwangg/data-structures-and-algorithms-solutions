class Solution {
public:
    bool isHappy(int n) {
        int num = n;
        std::unordered_set<int> visited;
        while (num != 1) {
            if (visited.contains(num)) {
                return false;
            }

            visited.insert(num);

            int new_num = 0;
            while (num > 0) {
                new_num += std::pow(num % 10, 2);
                num /= 10;
            }
            num = new_num;
        }
        return true;
    }
};
