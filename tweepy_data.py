import tweepy

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEEuaQEAAAAAmJVCeL1N%2FiSo9G6YVLB%2FhPoHjjg%3DkfiN8gv5mGV6WEHsle74BxyyQkAdJt1O6ET4WuarlWk5JTKN57'
client = tweepy.Client(bearer_token=bearer_token)


response = client.search_recent_tweets(query="Tres Cantos",tweet_fields = ['created_at'], max_results=10)

for tweet in response.data:
    print(tweet.text)
    print(tweet.created_at.date()) #.created_at devuelve datetime

