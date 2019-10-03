# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
import GetTweet

# APIの秘密鍵
CK,CKS,AT,ATS=os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"]

twische = BlockingScheduler()

# 30分に一度ツイート
@twische.scheduled_job('interval',minutes=30)
def timed_job():
    TextTweet.puttweet()

# 半日に一度ツイートを取得、チェーンを作ってdbに保存
@twische.scheduled_job('interval',hours=12)
def timed_job():
    #ツイートを取得
    GetTweet.gettweet(Ck,CKS,AT,ATS)

    #data.txtに保存
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()

    #チェーンを作成、dbに保存
    chain = PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

if __name__ == "__main__":
    twische.start()
