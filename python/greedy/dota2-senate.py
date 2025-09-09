class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = defaultdict(int)
        banned = defaultdict(int)
        q = deque()

        for senator in senate:
            count[senator] += 1
            q.append(senator)
        
        while q:
            senator = q.popleft()

            if count["R"] == 0:
                return "Dire"
            
            if count["D"] == 0:
                return "Radiant"

            if banned[senator]:
                banned[senator] -= 1
                count[senator] -= 1
                continue
            
            if senator == "R":
                banned["D"] += 1
            else:
                banned["R"] += 1
            
            q.append(senator)
