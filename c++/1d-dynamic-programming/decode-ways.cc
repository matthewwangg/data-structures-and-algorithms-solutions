class Solution {
public:
    int numDecodings(string s) {
        std::unordered_map<int, int> cache;
        return decode(0, s, cache);
    }

private:
    int decode(int i, std::string& s, std::unordered_map<int, int>& cache) {
        if (i == s.size()) {
            return 1;
        }

        if (s[i] == '0') {
            return 0;
        }

        if (cache.contains(i)) {
            return cache[i];
        }

        cache[i] = 0;
        if (i < s.size() - 1 && (s[i] == '1' || (s[i] == '2' && s[i+1] - '0' < 7))) {
            cache[i] += decode(i + 2, s, cache);
        }
        cache[i] += decode(i + 1, s, cache);

        return cache[i];
    }
};
