class StockSpanner {
public:
    StockSpanner() {

    }

    int next(int price) {
        span_.push_back(price);

        int counter = 0;
        for (int i = span_.size() - 1; i >= 0; --i) {
            if (span_[i] <= price) {
                counter++;
            } else {
                break;
            }
        }

        return counter;
    }

private:
    std::vector<int> span_;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
