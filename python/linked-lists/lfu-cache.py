class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minf = 0
        self.keytofreq = {}
        self.keytoval = {}
        self.freqtokey = defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keytoval:
            return -1

        if key in self.freqtokey[self.keytofreq[key]]:
            del self.freqtokey[self.keytofreq[key]][key]

        self.keytofreq[key] += 1
        self.freqtokey[self.keytofreq[key]][key] = 1

        if not self.freqtokey[self.minf]:
            self.minf += 1

        return self.keytoval[key]

    def put(self, key: int, value: int) -> None:
        if key in self.keytoval:
            self.keytoval[key] = value

            if key in self.keytofreq and key in self.freqtokey[self.keytofreq[key]]:
                del self.freqtokey[self.keytofreq[key]][key]

            self.keytofreq[key] = self.keytofreq.get(key, 0) + 1
            self.freqtokey[self.keytofreq[key]][key] = 1

            if not self.freqtokey[self.minf]:
                self.minf += 1
        else:
            if self.cap == 0:
                self.cap += 1
                deletekey, val = self.freqtokey[self.minf].popitem(last=False)
                del self.keytoval[deletekey]
                del self.keytofreq[deletekey]

            self.keytoval[key] = value
            self.keytofreq[key] = 1
            self.freqtokey[1][key] = 1
            self.cap -= 1
            self.minf = 1

        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)