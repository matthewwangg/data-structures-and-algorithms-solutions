class UnionFind:
    def __init__(self, size):
        self.representative = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.representative[x] == x:
            return x
        
        self.representative[x] = self.find(self.representative[x])
        
        return self.representative[x]
    
    def union(self, a, b):
        representative_a = self.find(a)
        representative_b = self.find(b)

        if representative_a == representative_b:
            return
        
        if self.size[representative_a] >= self.size[representative_b]:
            self.representative[representative_b] = representative_a
            self.size[representative_a] += self.size[representative_b]
        else:
            self.representative[representative_a] = representative_b
            self.size[representative_b] += self.size[representative_a]
    
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        m, n = min(nums), max(nums)
        if len(nums) == 1:
            return True
        if m <= 1:
            return False

        uf = UnionFind(2*n+1)

        def find_prime_factors(n):
            sieve = [0 for _ in range(n+1)]

            for p in range(2, n+1):
                if sieve[p] == 0:
                    for multiple in range(p, n+1, p):
                        sieve[multiple] = p
            
            return sieve
        
        sieve = find_prime_factors(n)
        for num in nums:
            val = num
            while val > 1:
                prime_factor = sieve[val]
                root = prime_factor + n
                if uf.find(root) != uf.find(num):
                    uf.union(root, num)
                while val % prime_factor == 0:
                    val //= prime_factor
                
        component = uf.find(nums[0])
        for i in range(len(nums)):
            if uf.find(nums[i]) != component:
                return False
        
        return True
