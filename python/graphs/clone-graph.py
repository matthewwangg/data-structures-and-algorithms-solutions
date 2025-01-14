"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}
        q = deque()
        q.append(node)
        while q:
            current = q.popleft()
            if current in nodes:
                continue
            nodes[current] = Node(current.val, [])
            for neighbor in current.neighbors:
                q.append(neighbor)

        for n in nodes:
            for neighbor in n.neighbors:
                nodes[n].neighbors.append(nodes[neighbor])

        return nodes[node]