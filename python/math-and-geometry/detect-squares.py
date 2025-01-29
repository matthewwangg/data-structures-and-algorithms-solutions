class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: 0)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        answer = 0
        for p in self.points.keys():
            if (p[0], point[1]) in self.points and (point[0], p[1]) in self.points and p != (p[0], point[1]) and p != (
            point[0], p[1]) and abs(p[0] - point[0]) == abs(p[1] - point[1]):
                answer += self.points[p] * self.points[(p[0], point[1])] * self.points[(point[0], p[1])]

        return answer

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)