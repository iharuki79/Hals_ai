from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
import GetTweet

CK,CKS,AT,ATS=os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"]

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=30)
def timed_job():
    GetTweet.gettweet(CK,CKS,AT,ATS)
    TextTweet.puttweet()

if __name__ == "__main__":
    twische.start()
