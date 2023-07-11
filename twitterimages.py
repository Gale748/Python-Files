import tweepy
import requests
import pickle

# Twitter API credentials
CONSUMER_KEY='<your_consumer_key>'
CONSUMER_SECRET='<your_consumer_secret>'
ACCESS_TOKEN='<your_access_token>'
ACCESS_TOKEN_SECRET='<your_access_token_secret>'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Initialize API client
api = tweepy.API(auth)

# Fetch the tweets from the given Twitter user
tweets = []
for status in tweepy.Cursor(
    api.user_timeline,
    screen_name="mvrcobutbetter",
    include_rts=False,
    exclude_replies=True,
    count=2000
).items():
    tweets.append(status)

with open('cached_tweets.pkl', 'wb') as f:
    pickle.dump(tweets, f)

with open('cached_tweets.pkl', 'rb') as f:
    tweets = pickle.load(f)

print(len(tweets))

# Iterate over the tweets and download any images that are present
for tweet in tweets:
    if hasattr(tweet, "extended_entities"):
        media = tweet.extended_entities.get("media", [])
    else:
        media = tweet.entities.get("media", [])
    if media:
        for i, m in enumerate(media):
            image_url = m["media_url_https"]
            try:
                response = requests.get(image_url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image for tweet {tweet.id}: {e}")
                continue
            with open(str(tweet.id) + "_" + str(i) + ".jpg", "wb") as f:
                f.write(response.content)
