class MyStack {
public:
    MyStack() {

    }

    void push(int x) {
        queue_1_.push(x);
    }

    int pop() {
        while (queue_1_.size() > 1) {
            queue_2_.push(queue_1_.front());
            queue_1_.pop();
        }

        int answer = queue_1_.front();
        queue_1_.pop();
        while (queue_2_.size() > 0) {
            queue_1_.push(queue_2_.front());
            queue_2_.pop();
        }

        return answer;
    }

    int top() {
        int answer;
        while (!queue_1_.empty()) {
            answer = queue_1_.front();
            queue_2_.push(answer);
            queue_1_.pop();
        }

        while (queue_2_.size() > 0) {
            queue_1_.push(queue_2_.front());
            queue_2_.pop();
        }

        return answer;
    }

    bool empty() {
        return queue_1_.empty();
    }

private:
    std::queue<int> queue_1_;
    std::queue<int> queue_2_;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
