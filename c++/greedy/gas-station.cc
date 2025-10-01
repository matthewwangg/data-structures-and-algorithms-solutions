class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        std::vector<int> net(gas.size(), std::numeric_limits<int>::max());
        int current_net = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); ++i) {
            current_net += gas[i] - cost[i];
            net[i] = current_net;
            if (current_net < net[start]) {
                start = i;
            }
        }
        
        if (current_net < 0) {
            return -1;
        }

        return (start == gas.size() - 1 ? 0 : start + 1);
    }
};
