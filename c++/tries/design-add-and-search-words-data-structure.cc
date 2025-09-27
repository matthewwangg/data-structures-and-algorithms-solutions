struct TrieNode {
    std::unordered_map<char, TrieNode*> dictionary;
    int count;
    bool terminal;
};

class Trie {
public:
    Trie() {
        root_ = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root_;
        for (char c : word) {
            if (!node->dictionary.contains(c)) {
                node->dictionary[c] = new TrieNode();
            }
            node->count += 1;
            node = node->dictionary[c];
        }
        node->terminal = true;
    }
    
    bool search(string word) {
        TrieNode* node = root_;
        for (char c : word) {
            if (!node->dictionary.contains(c)) {
                return false;
            }
            node = node->dictionary[c];
        }
        
        return node->terminal;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root_;
        for (char c : prefix) {
            if (!node->dictionary.contains(c)) {
                return false;
            }
            node = node->dictionary[c];
        }
        
        return node->count > 0 || node->terminal;
    }

private:
    TrieNode* root_;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
 