struct Node {
    int key;
    int val;

    Node* prev;
    Node* next;

    Node(int key, int val)
        : key(key),
          val(val),
          prev(nullptr),
          next(nullptr)
    {}
};

class LRUCache {
public:
    LRUCache(int capacity) {
        capacity_ = capacity;
        head_ = new Node(-1, -1);
        tail_ = new Node(-1, -1);

        head_->next = tail_;
        tail_->prev = head_;
    }
    
    int get(int key) {
        if (!dictionary_.contains(key)) {
            return -1;
        }

        remove(dictionary_[key]);
        add(dictionary_[key]);

        return dictionary_[key]->val;
    }
    
    void put(int key, int value) {
        if (dictionary_.contains(key)) {
            remove(dictionary_[key]);
            Node* to_add = new Node(key, value);
            dictionary_[key] = to_add;
            add(to_add);
        } else {
            if (capacity_ == dictionary_.size()) {
                Node* to_delete = tail_->prev;
                dictionary_.erase(to_delete->key);
                remove(to_delete);
            }

            Node* to_add = new Node(key, value);
            dictionary_[key] = to_add;
            add(to_add);
        }
    }

private:
    void add(Node* node) {
        node->next = head_->next;
        head_->next->prev = node;
        head_->next = node;
        node->prev = head_;
    }

    void remove(Node* node) {
        node->next->prev = node->prev;
        node->prev->next = node->next;
    }

    int capacity_;

    std::unordered_map<int, Node*> dictionary_;

    Node* head_;
    Node* tail_;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 