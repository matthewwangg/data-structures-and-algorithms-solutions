class MyQueue {
public:
    MyQueue() {

    }

    void push(int x) {
        stack_1_.push_back(x);
    }

    int pop() {
        while (stack_1_.size() > 1) {
            stack_2_.push_back(stack_1_.back());
            stack_1_.pop_back();
        }

        int answer = stack_1_.back();
        stack_1_.pop_back();
        while(!stack_2_.empty()) {
            stack_1_.push_back(stack_2_.back());
            stack_2_.pop_back();
        }

        return answer;
    }

    int peek() {
        int answer;
        while (stack_1_.size() > 0) {
            answer = stack_1_.back();
            stack_2_.push_back(answer);
            stack_1_.pop_back();
        }

        while(!stack_2_.empty()) {
            stack_1_.push_back(stack_2_.back());
            stack_2_.pop_back();
        }

        return answer;
    }

    bool empty() {
        return stack_1_.empty();
    }

private:
    std::vector<int> stack_1_;
    std::vector<int> stack_2_;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
