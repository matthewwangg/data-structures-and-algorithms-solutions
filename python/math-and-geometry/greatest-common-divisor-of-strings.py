class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        gcd = ""

        candidate = ""
        for i in range(len(str2)):
            candidate += str2[i]

            if m % len(candidate) != 0 or n % len(candidate) != 0:
                continue
            
            if str1 == ((m // len(candidate)) * candidate) and str2 == ((n // len(candidate)) * candidate):
                gcd = candidate
        
        return gcd
