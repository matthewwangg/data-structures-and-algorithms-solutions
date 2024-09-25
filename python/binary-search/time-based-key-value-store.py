class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        temp = []
        current = ""
        while len(self.store.get(key, [])) > 0 and self.store[key][-1][0] > timestamp:
            temp.append(self.store[key].pop())

        if len(self.store.get(key, [])) > 0:
            current = self.store[key][-1][1]

        for i in temp[::-1]:
            self.store[key].append(i)
        return current

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)