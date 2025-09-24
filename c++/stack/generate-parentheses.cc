class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::string> result;
        dfs(0, 0, "", n, result);
        return result;
    }

private:
    void dfs(int open, int close, std::string s, int n, std::vector<std::string>& result) {
        if (open == close && open + close == n * 2) {
            result.push_back(s);
            return;
        }

        if (open + close == n * 2) {
            return;
        }

        if (open > close) {
            dfs(open, close + 1, s + ")", n, result);
        }

        dfs(open + 1, close, s + "(", n, result);
    }
};
