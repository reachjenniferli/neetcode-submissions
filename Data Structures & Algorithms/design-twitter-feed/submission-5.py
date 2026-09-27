class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(list)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append([tweetId, self.time])
        if userId not in self.followMap[userId]:
            self.followMap[userId].append(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        results = []

        for following in self.followMap[userId]:
            for tweetId, t in self.tweetMap[following]:
                heapq.heappush(maxheap, (-t, tweetId))

        while maxheap and len(results) < 10:
            results.append(heapq.heappop(maxheap)[1])

        return results
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
