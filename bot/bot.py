import tweepy
import json
import pickle

def authenticateAndTweetImage():

    with open('secrets.json', 'r') as f:
        data = json.load(f)

        #Authenticate to Twitter
        auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
        auth.set_access_token(data["ACCESS_TOKEN"],data["ACCESS_TOKEN_SECRET"])

        # Create API object
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        f = open('num.pckl', 'rb')
        image_num = pickle.load(f)
        f.close()

        api.update_with_media("images/{}.png".format(image_num), status="#{}".format(image_num))
        print("Posted #{}".format(image_num))

        image_num += 1

        pickle.dump( image_num, open( "num.pckl", "wb" ) )