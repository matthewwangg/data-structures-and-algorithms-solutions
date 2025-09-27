struct TrieNode {
    std::unordered_map<char, TrieNode*> dictionary;
    int count;
    bool terminal;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    void add(std::string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->dictionary.contains(c) || !node->dictionary[c]) {
                node->dictionary[c] = new TrieNode();
            }
            node->count += 1;
            node = node->dictionary[c];
        }
        node->terminal = true;
    }

    bool search(std::string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->dictionary.contains(c) || !node->dictionary[c]) {
                return false;
            }
            node = node->dictionary[c];
        }
        return node->terminal;
    }

    bool prefix(std::string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->dictionary.contains(c) || !node->dictionary[c]) {
                return false;
            }
            node = node->dictionary[c];
        }
        return node->count > 0;
    }

    TrieNode* root;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* trie = new Trie();
        for (std::string word : words) {
            trie->add(word);
        }

        std::vector<std::vector<bool>> visited(board.size(), std::vector<bool>(board[0].size(), false));
        std::vector<std::pair<int, int>> options = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};
        std::string string = "";
        std::vector<std::string> answer;
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                dfs(i, j, string, visited, options, board, answer, trie->root);
            }
        }

        return answer;
    }

private:
    void dfs(int i, int j, std::string& string, std::vector<std::vector<bool>>& visited, std::vector<std::pair<int, int>>& options, std::vector<std::vector<char>>& board, std::vector<std::string>& answer, TrieNode* trie_node) {
        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || visited[i][j]) {
            return;
        }

        if (!trie_node->dictionary.contains(board[i][j]) || !trie_node->dictionary[board[i][j]]) {
            return;
        }

        string.push_back(board[i][j]);
        if (trie_node->dictionary[board[i][j]]->terminal) {
            answer.push_back(string);
            trie_node->dictionary[board[i][j]]->terminal = false;
        }

        visited[i][j] = true;
        
        for (auto [n_i, n_j] : options) {
            dfs(i+n_i, j+n_j, string, visited, options, board, answer, trie_node->dictionary[board[i][j]]);
        }
        visited[i][j] = false;
        string.pop_back();
    }
};
