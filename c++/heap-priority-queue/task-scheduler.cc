class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        std::priority_queue<std::pair<int, char>> pq;
        std::unordered_map<char, int> count;
        for (char c : tasks) {
            count[c] += 1;
            pq.push(std::make_pair(count[c], c));
        }

        int answer = 0;
        std::unordered_map<char, int> last;
        std::unordered_map<int, bool> taken;
        while (pq.size() != 0) {
            std::pair<int, char> current = pq.top();
            pq.pop();

            if (!last.contains(current.second)) {
                last[current.second] = -n;
            }

            int next = last[current.second] + n + 1;
            while (taken[next] && taken[next] == true) {
                next++;
            }
            taken[next] = true;
            last[current.second] = next;
            answer = std::max(answer, next);
        }

        return answer;
    }
};
