#####################################################################################################
# Program Name : Bitcoin_OSINT_SM_Tweet.py							    #									
# Description  : To gather tweets for given bitcoin wallet address	                            #
# Author       : Anjali Pillai(git ID: Anjalipillaii)						    #			
# Created Date : 25 May 2021									    #
# Last Updated : 30 May 2021									    #
# Execution    : python3 Bitcoin_OSINT_SM_Tweet.py 						    #
#####################################################################################################


import requests
from requests_oauthlib import OAuth1

# To get user input
bitcoin_id = input("Enter Address (sample: 1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s): ")


# Funtion to call twitter API and get tweets for the given Bitcoin address
def get_tweets(bitcoin_id):

    # API URL
    twitter_api_url = "https://api.twitter.com/1.1/search/tweets.json"

    # API authentication
    auth = OAuth1(
        "4Ca3CfSWr6HOljwB8jldxuiGe", 
        "04NlQqYiVzH3cFqfcWtdw6iMsBaqpEEFxMhuu9DNeR6gv4YMoe", 
    )

    # Array that will contain all tweet links to return
    tweet_links = []

    r = requests.get(
        twitter_api_url,
        auth=auth,
        params={"q": bitcoin_id, "count": "100"},
    )

    if r.status_code == 200:
        data = r.json()
        tweets = data["statuses"]
        for tweet in tweets:
            tweet_links.append(
                "https://twitter.com/"
                + str(tweet["user"]["screen_name"])
                + "/status/"
                + str(tweet["id"])
            )

    return tweet_links

# Function to save the tweets to a textfile
def save_tweets(bitcoin_id):
    content = get_tweets(bitcoin_id)

    with open(str(bitcoin_id) +"_tweet.txt", "w") as file:
        file.writelines("\n".join(content))


save_tweets(bitcoin_id)
