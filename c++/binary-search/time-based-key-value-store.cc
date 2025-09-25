class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        store_[key].push_back(std::make_pair(value, timestamp));
    }
    
    string get(string key, int timestamp) {
        int left = 0;
        int right = store_[key].size() - 1;

        int answer = -1;
        while (left <= right) {
            int middle = (right + left) / 2;
            if (store_[key][middle].second > timestamp) {
                right = middle - 1;
            } else {
                answer = std::max(answer, middle);
                left = middle + 1;
            }
        }

        if (answer == -1) {
            return "";
        } else {
            return store_[key][answer].first;
        }
    }

private:
    std::unordered_map<std::string, std::vector<std::pair<std::string, int>>> store_;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
 