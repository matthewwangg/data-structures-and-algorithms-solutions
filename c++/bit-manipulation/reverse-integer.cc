class Solution {
public:
    int reverse(int x) {
        int sign = x < 0 ? -1 : 1;
        int answer = 0;
        if (x < -2147483647) {
            return 0;
        }
        int digits = std::abs(x);
        int limit = (std::pow(2, 31) - 1) / 10;
        while (digits > 0) {
            if (answer > limit) {
                return 0;
            }
            answer *= 10;
            answer += digits % 10;
            digits /= 10;
        }
        return sign * answer;
    }
};
