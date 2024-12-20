from typing import List, Dict, Set, Tuple
from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.timestamp = 0
    
    def post_tweet(self, user_id: int, tweet_id: int):
        self.tweets[user_id].append((self.timestamp, tweet_id))
        self.timestamp += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        followees = self.followees[user_id] | {user_id}
        all_tweets = []
        
        for followee in followees:
            all_tweets.extend(self.tweets[followee])
        
        all_tweets.sort(key=lambda x: -x[0])
        
        return [tweet_id for _, tweet_id in all_tweets[:10]]
    
    def follow(self, follower_id: int, followee_id: int):
        self.followees[follower_id].add(followee_id)
    
    def unfollow(self, follower_id: int, followee_id: int):
        if followee_id in self.followees[follower_id]:
            self.followees[follower_id].remove(followee_id)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
