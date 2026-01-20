class Solution {
public:
    string simplifyPath(string path) {
        std::vector<std::string> folders = std::views::split(path, '/') | std::ranges::to<std::vector<std::string>>();
        std::vector<std::string> simplified_path;

        for (int i = 0; i < folders.size(); ++i) {
            if (folders[i] == "" || folders[i] == ".") {
                continue;
            }

            if (folders[i] == "..") {
                if (simplified_path.empty()) {
                    continue;
                }
                simplified_path.pop_back();
            } else {
                simplified_path.push_back(folders[i]);
            }
        }

        std::string final_path;
        for (int i = 0; i < simplified_path.size(); ++i) {
            final_path += "/" + simplified_path[i];
        }

        return (final_path.size() > 0) ? final_path : "/";
    }
};
