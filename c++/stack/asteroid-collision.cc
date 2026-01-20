class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        std::vector<int> stack;
        
        for (int i = 0; i < asteroids.size(); ++i) {
            if (stack.empty() || stack.back() < 0 || asteroids[i] > 0) {
                stack.push_back(asteroids[i]);
                continue;
            }
            
            bool destroyed = false;
            while (!destroyed && !stack.empty() && stack.back() > 0) {
                if (stack.back() > - asteroids[i]) {
                    destroyed = true;
                    break;
                } else if (stack.back() == - asteroids[i]) {
                    destroyed = true;
                }
                stack.pop_back();
            }

            if (!destroyed) {
                stack.push_back(asteroids[i]);
            } 
        }

        return stack;
    }
};
