class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        std::unordered_map<int, int> cache;
        return break_word(0, s, wordDict, cache);
    }

private:
    bool break_word(int i, std::string& s, std::vector<std::string>& dictionary,  std::unordered_map<int, int>& cache) {
        if (i == s.size()) {
            return true;
        }

        if (cache.contains(i)) {
            return cache[i];
        }

        cache[i] = false;
        for (std::string word : dictionary) {
            if (word == s.substr(i, word.size())) {
                cache[i] = cache[i] || break_word(i + word.size(), s, dictionary, cache);
            }
        }
        return cache[i];
    }
};
