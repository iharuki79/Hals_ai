from apscheduler.schedulers.blocking import BlockingScheduler
import TextTweet
import GetTweet

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=60)
def timed_job():
    GetTweet.gettweet()
    TextTweet.puttweet()

if __name__ == "__main__":
    twische.start()
