class MinStack {
public:
    MinStack() {
    }
    
    void push(int val) {
        if (!stack_.empty()) {
            stack_.push_back(std::vector<int>{val, std::min(getMin(), val)});
        } else {
            stack_.push_back(std::vector<int>{val, val});
        }
    }
    
    void pop() {
        stack_.pop_back();
    }
    
    int top() {
        return stack_.empty() ? -1 : stack_.back()[0];
    }
    
    int getMin() {
        return stack_.empty() ? -1 : stack_.back()[1];
    }
    
private:
    std::vector<std::vector<int>> stack_;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
