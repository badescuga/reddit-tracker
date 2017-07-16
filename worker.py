from multiprocessing import Pool
from pprint import pprint
import schedule
import praw
import json
import time

WORKER_COUNT = 3
SCHEDULE_TIME = 5  # seconds

REDDIT_CLIENT_ID = "y06iTiHoyVa8fA"
REDDIT_SECRET = "7mTVgS61qSPM6aH28m9czS32OzQ"
REDDIT_USER_AGENT = "Python aggregator (by /u/badescuga )"

SUBREDDITS_PATH = "subreddits.json"

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

    # init reddit api
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

    # loading subreddits from json file
    with open(SUBREDDITS_PATH) as data_file:    
        data = json.load(data_file)
        subreddits_array = data["subreddits"]
        pprint(subreddits_array)

    # keep alive
    while True:
        schedule.run_pending()
        time.sleep(1)

# calling from here for now, will move to main.py at some point
start()