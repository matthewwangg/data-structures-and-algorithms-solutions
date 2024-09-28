"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        answer = Node(0)
        current = answer
        temp = head

        while temp:
            current.next = Node(temp.val)
            current = current.next
            nodes[temp] = current
            temp = temp.next

        temp = head
        current = answer.next
        while temp:
            if temp.random:
                current.random = nodes[temp.random]
            current = current.next
            temp = temp.next

        return answer.next