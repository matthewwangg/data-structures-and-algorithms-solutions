class Solution {
public:
    string decodeString(string s) {
        std::vector<std::string> stack;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ']') {
                std::string result;
                while (stack.back() != "[") {
                    result = stack.back() + result;
                    stack.pop_back();
                }

                stack.pop_back();
                std::string multiplied_result;
                std::string factor;
                while (!stack.empty() && std::isdigit(stack.back().front())) {
                    factor = stack.back() + factor;
                    stack.pop_back();
                }

                for (int i = 0; i < std::stoi(factor); ++i) {
                    multiplied_result += result;
                }

                stack.push_back(multiplied_result);
            } else {
                std::string character(1, s[i]);
                stack.push_back(character);
            }
        }

        std::string answer;
        for (int i = 0; i < stack.size(); ++i) {
            answer += stack[i];
        }

        return answer;
    }
};
