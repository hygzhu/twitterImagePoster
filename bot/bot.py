import tweepy
import json

def authenticateAndTweetImage():

    with open('secrets.json', 'r') as f:
        data = json.load(f)

        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
        auth.set_access_token(data["ACCESS_TOKEN"],data["ACCESS_TOKEN_SECRET"])

        # Create API object
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        api.update_with_media("images/test.png", status="Test")
