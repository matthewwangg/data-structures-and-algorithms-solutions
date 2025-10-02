class Solution {
public:
    bool isMatch(string s, string p) {
        std::unordered_map<int, std::unordered_map<int, bool>> cache;
        return match(0, 0, s, p, cache);
    }

private:
    bool match(int i, int j, std::string& s, std::string& p, std::unordered_map<int, std::unordered_map<int, bool>>& cache) {
        if (i == s.size() && j == p.size()) {
            return true;
        }

        if (j == p.size()) {
            return false;
        }

        if (j < p.size() - 1 && p[j + 1] == '*') {
            if (i < s.size() && (p[j] == s[i] || p[j] == '.')) {
                cache[i][j] = match(i + 1, j, s, p, cache) || match(i, j + 2, s, p, cache);
            } else {
                cache[i][j] = match(i, j + 2, s, p, cache);
            }
        } else {
            if (i < s.size() && (p[j] == s[i] || p[j] == '.')) {
                cache[i][j] = match(i + 1, j + 1, s, p, cache);
            } else {
                cache[i][j] = false;
            }
        }

        return cache[i][j];
    } 
};
