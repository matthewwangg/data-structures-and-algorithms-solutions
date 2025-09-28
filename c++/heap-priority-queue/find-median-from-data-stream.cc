class MedianFinder {
public:
    MedianFinder() {
        count_ = 0;
    }
    
    void addNum(int num) {
        if (higher_.size() == lower_.size()) {
            higher_.push(-num);
            int low = -higher_.top();
            higher_.pop();
            lower_.push(low);
        } else {
            lower_.push(num);
            int high = lower_.top();
            lower_.pop();
            higher_.push(-high);
        }
        count_ += 1;
    }
    
    double findMedian() {
        if (count_ % 2 == 0) {
            return static_cast<double>(lower_.top() - higher_.top()) / 2.0;
        } else {
            return static_cast<double>(lower_.top());
        }
    }

private:
    std::priority_queue<int> higher_;
    std::priority_queue<int> lower_;

    int count_;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
 