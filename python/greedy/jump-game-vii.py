class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        spots = deque()
        spots.append(0)

        for i in range(1, len(s)):
            if spots and spots[0] + maxJump < i:
                spots.popleft()
            
            if s[i] == "0" and spots and spots[0] + minJump <= i:
                spots.append(i)
        
        if len(spots) == 0:
            return False

        return spots[-1] == len(s)-1
