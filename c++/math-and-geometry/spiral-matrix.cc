class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        std::vector<int> answer;
        int i = 0;
        int j = 0;
        int direction = 0;
        int distance = 0;
        while (answer.size() != matrix.size() * matrix[0].size()) {
            answer.push_back(matrix[i][j]);
            switch (direction) {
                case 0:
                    j += 1;
                    if (j == matrix[0].size() - distance) {
                        j -= 1;
                        i += 1;
                        direction = 1;
                    }
                    break;
                case 1:
                    i += 1;
                    if (i == matrix.size() - distance) {
                        i -= 1;
                        j -= 1;
                        direction = 2;
                    }
                    break;
                case 2:
                    j -= 1;
                    if (j < 0 + distance) {
                        j += 1;
                        i -= 1;
                        direction = 3;
                    }
                    break;
                case 3:
                    i -= 1;
                    if (i < 0 + distance + 1) {
                        i += 1;
                        j += 1;
                        direction = 0;
                        distance += 1;
                    }
                    break;
            }
        }
        return answer;
    }
};
