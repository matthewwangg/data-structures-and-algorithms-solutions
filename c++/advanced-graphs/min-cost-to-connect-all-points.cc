class UnionFind {
public:
    UnionFind(int size) {
        size_ = std::vector<int>(size, 1);

        for (int i = 0; i < size; ++i) {
            representative_.push_back(i);
        }
    }

    int find(int x) {
        if (representative_[x] == x) {
            return x;
        }

        representative_[x] = find(representative_[x]);
        return representative_[x];
    }

    bool do_union(int a, int b) {
        int representative_a = find(a);
        int representative_b = find(b);

        if (representative_a == representative_b) {
            return false;
        } else {
            if (size_[representative_a] > size_[representative_b]) {
                size_[representative_a] += size_[representative_b];
                representative_[representative_b] = representative_a;
            } else {
                size_[representative_b] += size_[representative_a];
                representative_[representative_a] = representative_b;
            }
        }
        return true;
    }

private:
    std::vector<int> representative_;
    std::vector<int> size_;
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        UnionFind uf = UnionFind(points.size());

        std::priority_queue<std::vector<int>> pq;
        for (int i = 0; i < points.size(); ++i) {
            for (int j = i + 1; j < points.size(); ++j) {
                pq.push(std::vector<int>{-(std::abs(points[i][0] - points[j][0]) + std::abs(points[i][1] - points[j][1])), i, j});
            }
        }

        int answer = 0;
        while (pq.size() > 0) {
            std::vector<int> current = pq.top();
            pq.pop();

            if (!uf.do_union(current[1], current[2])) {
                continue;
            }

            answer += -current[0];
        }

        return answer;
    }
};
