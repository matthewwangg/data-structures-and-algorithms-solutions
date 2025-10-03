class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        std::reverse(num1.begin(), num1.end());
        std::reverse(num2.begin(), num2.end());

        std::string answer(num1.size() + num2.size(), '0');
        for (int i = 0; i < num1.size(); ++i) {
            int digit1 = num1[i] - '0';
            for (int j = 0; j < num2.size(); ++j) {
                int digit2 = num2[j] - '0';

                int zeros = i + j;
                int carry = answer[zeros] - '0';

                int result = digit1 * digit2 + carry;
                answer[zeros] = (result % 10) + '0';
                answer[zeros + 1] += (result / 10);
            }
        }

        if (answer.back() == '0') {
            answer.pop_back();
        }
        std::reverse(answer.begin(), answer.end());

        return answer;
    }
};
