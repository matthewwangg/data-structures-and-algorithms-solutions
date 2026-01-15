class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {
        prefix_ = std::vector<std::vector<int>>(matrix.size() + 1, std::vector<int>(matrix[0].size() + 1, 0));
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size(); ++j) {
                prefix_[i+1][j+1] = matrix[i][j] + prefix_[i+1][j] + prefix_[i][j+1] - prefix_[i][j];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix_[row2+1][col2+1] - prefix_[row2+1][col1] - prefix_[row1][col2+1] + prefix_[row1][col1];
    }

private:
    std::vector<std::vector<int>> prefix_;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
