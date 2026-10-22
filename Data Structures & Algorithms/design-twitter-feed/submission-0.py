class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][idx]
                heap.append((-t, tid, u, idx))
        heapq.heapify(heap)

        while heap and len(res) < 10:
            neg_t, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                t, tid = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-t, tid, u, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)