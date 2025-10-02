class Solution {
public:
    int getSum(int a, int b) {
        int mask = 0xFFFFFFFF;
        while (b != 0) {
            int old_a = a;
            a = (a ^ b) & mask;
            b = ((old_a & b) << 1) & mask;
        }

        if (a < 0x7FFFFFF) {
            return a;
        } else {
            return ~(a ^ mask);
        }
    }
};
