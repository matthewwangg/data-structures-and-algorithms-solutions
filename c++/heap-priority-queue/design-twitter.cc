class Twitter {
public:
    Twitter() {
        time_ = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweets_[userId].push(std::make_pair(time_, tweetId));
        time_ += 1;
    }
    
    vector<int> getNewsFeed(int userId) {
        followees_[userId].insert(userId);
        std::priority_queue<std::pair<int, int>> pq;
        for (int followee : followees_[userId]) {
            std::vector<std::pair<int, int>> replace;
            while (tweets_[followee].size() > 0 && replace.size() < 10) {
                replace.push_back(tweets_[followee].top());
                pq.push(tweets_[followee].top());
                tweets_[followee].pop();
            }

            for (std::pair<int, int> tweet : replace) {
                tweets_[followee].push(tweet);
            }
        }

        std::vector<int> feed;
        int size = pq.size();
        for (int i = 0; i < std::min(10, size); ++i) {
            feed.push_back(pq.top().second);
            pq.pop();
        }

        return feed;
    }
    
    void follow(int followerId, int followeeId) {
        followees_[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followees_[followerId].contains(followeeId)) {
            followees_[followerId].erase(followeeId);
        }
    }

private:
    int time_;

    std::unordered_map<int, std::unordered_set<int>> followees_;
    std::unordered_map<int, std::priority_queue<std::pair<int, int>>> tweets_;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
 