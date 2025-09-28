class Solution {
public:
    vector<string> letterCombinations(string digits) {
        std::unordered_map<char, std::vector<char>> mapping = {{'2', {'a', 'b', 'c'}}, {'3', {'d', 'e', 'f'}}, {'4', {'g', 'h', 'i'}}, {'5', {'j', 'k', 'l'}}, {'6', {'m', 'n', 'o'}}, {'7', {'p', 'q', 'r', 's'}}, {'8', {'t', 'u', 'v'}}, {'9', {'w', 'x', 'y', 'z'}}};
        std::string combination;
        std::vector<std::string> combinations;
        construct(0, digits, mapping, combination, combinations);

        return combinations;
    }

private:
    void construct(int i, std::string& digits, std::unordered_map<char, std::vector<char>>& mapping, std::string& combination, std::vector<std::string>& combinations) {
        if (i == digits.size() && combination.size() > 0) {
            combinations.push_back(combination);
            return;
        }

        for (char c : mapping[digits[i]]) {
            combination.push_back(c);
            construct(i+1, digits, mapping, combination, combinations);
            combination.pop_back();
        }
    }
};
