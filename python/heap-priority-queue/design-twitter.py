import heapq


class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId, []) + [(tweetId, self.count)]
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets.get(userId, [])[:]
        for i in self.following.get(userId, set()):
            feed += self.tweets.get(i, [])

        heap = []
        for i in feed:
            heapq.heappush(heap, (i[1], i[0]))

        finalanswer = []
        for i in range(10):
            if heap:
                finalanswer.append(heapq.heappop(heap)[1])

        return finalanswer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId] = self.following.get(followerId, set())
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId, set()):
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)