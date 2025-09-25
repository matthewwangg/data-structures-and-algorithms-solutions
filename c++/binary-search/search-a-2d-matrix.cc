class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left_row = 0;
        int right_row = matrix.size() - 1;
        while (left_row <= right_row) {
            int middle_row = (left_row + right_row) / 2;
            if (target < matrix[middle_row][0]) {
                right_row = middle_row - 1;
            } else if (target > matrix[middle_row][matrix[middle_row].size() - 1]) {
                left_row = middle_row + 1;
            } else {
                int left = 0;
                int right = matrix[middle_row].size() - 1;
                while (left <= right) {
                    int middle = (left + right) / 2;
                    if (matrix[middle_row][middle] == target) {
                        return true;
                    } else if (matrix[middle_row][middle] < target) {
                        left = middle + 1;
                    } else {
                        right = middle - 1;
                    }
                }
                break;
            }
        }
        return false;
    }
};
