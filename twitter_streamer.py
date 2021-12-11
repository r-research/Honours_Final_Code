## Author: LucidProgramming
## Date: January 15, 2018 and January 17, 2018
## Source: https://www.youtube.com/watch?v=wlnx-7cm4Gg and https://www.youtube.com/watch?v=rhBZqEWsZU4

## Modified by Kathleen Shalini Rome
## Date: April 10, 2021

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials_seroja

class TwitterAuthenticator():
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials_seroja.consumer_key,twitter_credentials_seroja.consumer_secret)
        auth.set_access_token(twitter_credentials_seroja.access_token, twitter_credentials_seroja.access_token_secret)
        return auth


class TwitterStreamer(): #we want to save to tweets_filename
    # A class for streaming and processing live tweets. 
    def __init__(self):
       self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self,fetched_tweets_filename, hash_tag_list ):
        #This handles Twitter authen and connection to the Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener) #listenre is responsible how to deal with tweets and error
        
        # THis line filters twitter streams to capture data by the keywords
        stream.filter(track=hash_tag_list) 

# Allow us to print the tweets
class TwitterListener(StreamListener):
    # This is a basic listener class that just prints recieved tweets to teh stdout.
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self,data): #take in streamlistener data and can do whatever we want
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf: #'a' is append
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s " % str(e))
        return True

    def on_error(self,status):
        if status == 420:
            # Returning false on data method in case rate limit occurs. 
            return False
        print(status) #when we encounter an error it will print it out
        #Good to check we dont over do the 

if __name__ == "__main__":

    # A max of 10 keywords may be used
    hash_tag_list =  ["cyclone", "cyclone seroja","#Seroja", '#Odette', '#CycloneSeroja','severe weather','meteorology','bureau of meteorology', 'tropical cyclone']
    # 4. Storm and warning gave irrelevant data ["cyclone", "cyclone seroja","#Seroja", '#Odette', 'fujiwhara effect','severe weather','warning','storm','bureau of meteorology', 'tropical cyclone']
    
    # tweet cyclone 10 april ["cyclone", "cyclone seroja","Seroja", 'Odette', 'cyclone warning','cyclonewarning','cyclone season','bureau']
    fetched_tweets_filename = "tweets_cyclone_10_April_5.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)