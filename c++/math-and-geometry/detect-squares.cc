class DetectSquares {
public:
    DetectSquares() {
        
    }
    
    void add(vector<int> point) {
        points_[point[0]][point[1]] += 1;
    }
    
    int count(vector<int> point) {
        int answer = 0;
        
        for (auto [x, map] : points_) {
            for (auto [y, count] : map) {
                if ((points_.contains(x) && points_[x].contains(point[1])) && (points_.contains(point[0]) && points_[point[0]].contains(y)) && (x != point[0] && y != point[1]) && (std::abs(x - point[0]) == std::abs(y - point[1]))) {
                    answer += points_[x][y] * points_[x][point[1]] * points_[point[0]][y];
                } 
            }
        }

        return answer;
    }

private:
    std::unordered_map<int, std::unordered_map<int, int>> points_;
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
 