class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> pq;

        for (int stone : stones) {
            pq.push(stone);
        }

        while (pq.size() > 1) {
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();

            if (x == y) {
                continue;
            } else {
                pq.push(x - y);
            }
        }

        if (pq.size() == 1) {
            return pq.top();
        } else {
            return 0;
        }
    }
};
