from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
from GenerateText import GenerateText
import PrepareChain

def puttweet():
    twitter = OAuth1Session(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
    chain=PrepareChain.PrepareChain()
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)
    generator=GenerateText(1)
    tw=generator.generate()
    params = {"status": "[hals_ai]"+tw}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
