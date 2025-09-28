class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        capacity_ = k;
        for (int num : nums) {
            pq_.push(-num);
        }

        while (pq_.size() > k) {
            pq_.pop();
        }
    }
    
    int add(int val) {
        pq_.push(-val);
        if (pq_.size() > capacity_) {
            pq_.pop();
        }

        return -pq_.top();
    }

private:
    int capacity_;
    std::priority_queue<int> pq_;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
 