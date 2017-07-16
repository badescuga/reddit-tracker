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
REDDIT_USER_AGENT = "Python reddit aggregator (by /u/badescuga )"

SUBREDDITS_PATH = "subreddits.json"

# loading subreddits from json file
with open(SUBREDDITS_PATH) as data_file:
    data = json.load(data_file)
    subreddits_array = []
    for key in data["subreddits"]:
        string_split = key.split("/")
        subreddits_array.append(string_split[len(string_split) - 1])

# init reddit api; TODO: create reddit connection specific for every worker, PRAW not safe
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

print("starting worker, worker_count: ", WORKER_COUNT)

def fetchRedditData(subreddit_path):
    print("=> subreddit: ", subreddit_path)
    # subreddit = reddit.subreddit('AskReddit')
    # for submission in subreddit.stream.submissions():
    #     # do something with submission
    #     print submission.title
    subreddit=reddit.subreddit(subreddit_path)
    for submission in subreddit.new():
        print submission.title

    print("=> fetchRedditData returning")
    return subreddit_path

def periodicalFetch():
    print("=> Periodical Fetch")
    print(pool.map(fetchRedditData, subreddits_array))

# needs to be inited after periodicalFetch()
pool = Pool(WORKER_COUNT)

def start(): 

    # start scheduler job
    schedule.every(SCHEDULE_TIME).seconds.do(periodicalFetch)

    # keep alive
    while True:
        schedule.run_pending()
        time.sleep(1)

# calling from here for now, will move to main.py at some point
start()
