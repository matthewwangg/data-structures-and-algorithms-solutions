class UnionFind:
    def __init__(self, size):
        self.representative = {}
        self.size = {}

        for i in range(size):
            self.representative[i] = i
            self.size[i] = 1
    
    def find(self, x):
        if x == self.representative[x]:
            return x
        
        self.representative[x] = self.find(self.representative[x])

        return self.representative[x]
    
    def union(self, a, b):
        representative_a = self.find(a)
        representative_b = self.find(b)

        if representative_a == representative_b:
            return
        
        if self.size[representative_a] > self.size[representative_b]:
            self.size[representative_a] += self.size[representative_b]
            self.representative[representative_b] = representative_a 
        else:
            self.size[representative_b] += self.size[representative_a]
            self.representative[representative_a] = representative_b 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        group = {}
        names = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                names[email] = accounts[i][0]

                if email in group:
                    uf.union(i, group[email])
                else:
                    group[email] = i
        
        components = {}
        for email in group:
            representative = uf.find(group[email])
            if representative not in components:
                components[representative] = []
            components[representative].append(email)
        
        answer = []
        for key in components:
            if not components[key]:
                answer.append([])
                continue
            answer.append([names[components[key][0]]] + sorted(components[key]))
        
        return answer
