class MyHashMap {
public:
    MyHashMap() {
        hash_map_ = std::vector<int>(1000001, -1);
    }

    void put(int key, int value) {
        hash_map_[key] = value;
    }

    int get(int key) {
        return hash_map_[key];
    }

    void remove(int key) {
        hash_map_[key] = -1;
    }

private:
    std::vector<int> hash_map_;
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
