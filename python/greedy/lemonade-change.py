class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            if bill == 10:
                change[5] -= 1
            if bill == 20:
                if change[10]:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            
            if change[5] < 0:
                return False

            change[bill] += 1
        
        return True
