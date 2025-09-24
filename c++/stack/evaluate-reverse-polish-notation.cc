class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::vector<int> stack;
        std::vector<std::string> operators = {"+", "-", "*", "/"};

        for (std::string token : tokens) {
            if (std::find(operators.begin(), operators.end(), token) == operators.end()) {
                stack.push_back(std::stoi(token));
            } else {
                int input1 = stack.back();
                stack.pop_back();
                int input2 = stack.back();
                stack.pop_back();

                int answer;
                if (token == "+") {
                    answer = input2 + input1;
                } else if (token == "-") {
                    answer = input2 - input1;
                } else if (token == "*") {
                    answer = input2 * input1;
                } else {
                    answer = input2 / input1;
                }
                stack.push_back(answer);
            }
        }
        return stack.back();
    }
};
