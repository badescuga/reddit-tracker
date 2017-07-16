from multiprocessing import Pool
import schedule
import time

WORKER_COUNT = 3
SCHEDULE_TIME = 5  # seconds

print("starting worker, worker_count: ", WORKER_COUNT)

def fetchRedditData(subreddit):
    print("subreddit: ", subreddit)
    return subreddit


def periodicalFetch():
    print("=> Periodical Fetch")
    print(pool.map(fetchRedditData, [1, 2, 3 , 4, 5]))

# needs to be inited after periodicalFetch()
pool = Pool(WORKER_COUNT)

def start(): 

    # start scheduler job
    schedule.every(SCHEDULE_TIME).seconds.do(periodicalFetch)

    # keep alive
    while True:
        schedule.run_pending()
        time.sleep(1)

# calling from here for now, will move to main.py at some poin
start()