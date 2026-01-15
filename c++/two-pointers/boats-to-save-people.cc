class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        
        int boats = 0;

        int left = 0;
        int right = people.size() - 1;

        while (left < right) {
            if (people[left] + people[right] <= limit) {
                left++;
            }

            boats++;
            right--;
        }

        boats += (left == right) ? 1 : 0;

        return boats;
    }
};
