from collections import defaultdict
import heapq 

class Twitter:
    def __init__(self):
        self.curr_id = 0
        self.user_tweets = defaultdict(list) # {userId: (curr_id, tweetId)}     
        self.user_follow = defaultdict(set) # {user_id: {list of followees}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.curr_id += 1
        self.user_tweets[userId].append((self.curr_id, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        all_tweets = []
        for id in self.user_follow[userId] | {userId}:
            all_tweets.extend(self.user_tweets[id][-10:])
        
        heap = []
        for curr_id, tweet_id in all_tweets:
            if len(heap) < 10:
                heapq.heappush(heap, (curr_id, tweet_id))
            elif curr_id > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (curr_id,tweet_id))
        heap.sort(reverse = True)

        return [item[1] for item in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)