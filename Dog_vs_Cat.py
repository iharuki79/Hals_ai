from apscheduler.schedulers.blocking import BlockingScheduler

twische = BlockingScheduler()

@twische.scheduled_job('interval',seconds=1)
def timed_job():
    print("\t∪o・ｪ・o∪<Bow!")

@twische.scheduled_job('interval',seconds=2)
def timed_job():
    print("\t\t\tMeow!> (=^･ω･^=)")


if __name__ == '__main__':
    twische.start()
