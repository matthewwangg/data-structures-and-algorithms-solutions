class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_map<std::string, std::vector<std::string>> ladder;

        wordList.push_back(beginWord);
        for (std::string word : wordList) {
            for (int i = 0; i < word.size(); ++i) {
                std::string wildcard = word;
                wildcard[i] = '.';
                ladder[wildcard].push_back(word);
            }
        }
        
        std::unordered_set<std::string> visited;
        std::queue<std::pair<std::string, int>> q;
        q.push(std::make_pair(beginWord, 1));
        while (q.size() > 0) {
            std::pair<std::string, int> current = q.front();
            q.pop();

            if (visited.contains(current.first)) {
                continue;
            }

            visited.insert(current.first);

            if (current.first == endWord) {
                return current.second;
            }

            for (int i = 0; i < current.first.size(); ++i) {
                std::string wildcard = current.first;
                wildcard[i] = '.';
                for (std::string neighbor : ladder[wildcard]) {
                    q.push(std::make_pair(neighbor, current.second + 1));
                }
            }
        }

        return 0;
    }
};
