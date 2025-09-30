class UnionFind {
public:
    UnionFind(int nodes) {
        size_ = std::vector<int>(nodes, 1);
        for (int i = 1; i < nodes + 1; ++i) {
            representative_.push_back(i);
        }
    }

    int find(int x) {
        if (representative_[x - 1] == x) {
            return x;
        }

        representative_[x - 1] = find(representative_[x - 1]);

        return representative_[x - 1];
    }

    bool do_union(int a, int b) {
        int representative_a = find(a);
        int representative_b = find(b);

        if (representative_a == representative_b) {
            return false;
        } else {
            if (size_[representative_a - 1] > size_[representative_b - 1]) {
                size_[representative_a - 1] += size_[representative_b - 1];
                representative_[representative_b - 1] = representative_a;
            } else {
                size_[representative_b - 1] += size_[representative_a - 1];
                representative_[representative_a - 1] = representative_b;
            }
            return true;
        }
    }

private:
    std::vector<int> size_;
    std::vector<int> representative_;
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UnionFind uf = UnionFind(edges.size());

        std::vector<int> answer = {};
        for (int i = 0; i < edges.size(); i++) {
            if (!uf.do_union(edges[i][0], edges[i][1])) {
                answer = edges[i];
            }
        }

        return answer;
    }
};
