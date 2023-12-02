import schedule
import time

import threading

def addScheduleEveryday(time, action):
    return schedule.every().day.at(time).do(action)


def runScheduler(interval):
    def startSchedule():
        print("Start your scheduling, press CTR+C to quit")
        while True:
            schedule.run_pending()
            time.sleep(interval)
    thread = threading.Thread(target=startSchedule)
    thread.start()


def stopScheduler(job):
    schedule.cancel_job(job)
