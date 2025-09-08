class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        value = [float('-inf') for _ in range(len(stoneValue)+1)]
        value[len(stoneValue)] = 0
        for i in range(len(stoneValue)-1, -1, -1):
            score = 0
            for j in range(1, 4):
                if i + j > len(stoneValue):
                    break
                
                score += stoneValue[i+j-1]
                value[i] = max(value[i], score - value[i+j])
        
        if value[0] > 0:
            return "Alice"
        elif value[0] < 0:
            return "Bob"
        else:
            return "Tie"
