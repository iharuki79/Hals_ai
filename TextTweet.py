# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
from GenerateText import GenerateText
import PrepareChain

def puttweet():

    # APIに接続
    twitter = OAuth1Session(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

    # data.txtを開く
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()

    # チェーンを作成
    chain=PrepareChain.PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    # ツイートする文章を生成
    generator=GenerateText()
    tw=generator.generate()

    #ツイート
    params = {"status": "[hals_ai]"+tw}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
