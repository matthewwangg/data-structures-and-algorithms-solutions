class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }

        unsigned long long num;
        if (n < 0) {
            x = 1.0 / x;
            num = -static_cast<unsigned long long>(n);
        } else {
            num = n;
        }

        double answer = 1;
        while (num != 0) {
            if (num % 2 == 1) {
                answer *= x;
                num -= 1;
            }
            x *= x;
            num /= 2;
        }
        return answer;
    }
};
