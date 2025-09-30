class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, int> indegree;
        std::unordered_map<int, std::vector<int>> dependents;

        for (auto req : prerequisites) {
            indegree[req[0]] += 1;
            dependents[req[1]].push_back(req[0]);
        }

        std::queue<int> q;
        for (int course = 0; course < numCourses; ++course) {
            if (indegree[course] == 0) {
                q.push(course);
            }
        }

        std::vector<int> schedule;
        while (q.size() > 0) {
            int course = q.front();
            q.pop();

            schedule.push_back(course);

            for (int dependent : dependents[course]) {
                indegree[dependent] -= 1;
                if (indegree[dependent] == 0) {
                    q.push(dependent);
                }
            }        
        }

        return schedule.size() == numCourses;
    }
};
