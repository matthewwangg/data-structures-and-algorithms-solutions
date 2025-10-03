class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        std::vector<int> answer = digits;
        std::reverse(answer.begin(), answer.end());
        for (int i = 0; i < answer.size(); ++i) {
            if (answer[i] < 9) {
                answer[i]++;
                break;
            } else {
                answer[i] = 0;
            }
        }
        
        if (answer[answer.size() - 1] == 0) {
            answer.push_back(1);
        }
        std::reverse(answer.begin(), answer.end());

        return answer;
    }
};
