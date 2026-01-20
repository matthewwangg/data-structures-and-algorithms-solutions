class FreqStack {
public:
    FreqStack() {
        time_ = 0;
    }

    void push(int val) {
        count_[val]++;
        heap_.push(std::make_tuple(count_[val], time_, val));
        time_++;
    }

    int pop() {
        std::tuple<int, int, int> element = heap_.top();
        count_[std::get<2>(element)]--;
        heap_.pop();
        return std::get<2>(element);
    }

private:
    std::priority_queue<std::tuple<int, int, int>> heap_;
    std::unordered_map<int, int> count_;
    int time_;
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
