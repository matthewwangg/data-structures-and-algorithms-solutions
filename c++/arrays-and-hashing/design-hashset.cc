class MyHashSet {
public:
    MyHashSet() {
        hash_set_ = std::vector<bool>(1000001, false);
    }

    void add(int key) {
        hash_set_[key] = true;
    }

    void remove(int key) {
        hash_set_[key] = false;
    }

    bool contains(int key) {
        return hash_set_[key];
    }

private:
    std::vector<bool> hash_set_;
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
