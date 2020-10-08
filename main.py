"""
This file executes the Bot's functions, including accessing Reddit using
PRAW, parsing through subreddit post titles, and sending the user message.
"""
import praw
import time

USER = "username" # redacted
SUBJECT = "Someone is selling a villager you're interested in!"
KEY_PHRASES = ["[FT] Del", "[FT] Tangy"]

def access_reddit():
    """
    Accesses Reddit's API and logs into bot account.
    """
    reddit = praw.Reddit(user_agent="AC-Villager-Bot from username", #redacted
                         client_id="-----------", # redacted
                         client_secret="-------------", # redacted
                         username="AC-Villager-Bot",
                         password="-------------" # redacted
                         )
    return reddit


def find_posts(reddit):
    """
    Parses through subreddit submissions and finds posts that include keyphrase(s). Sends
    post links to designated user with constants USER and SUBJECT.
    """
    subreddit = reddit.subreddit("ACVillager") # can be changed to any subreddit
    try:
        while True:
            for submission in subreddit.stream.submissions():
                for key in KEY_PHRASES:
                    if key.lower() in submission.title.lower() and submission.created_utc > start_time:
                        reddit.redditor("missingclubpenguin").message(SUBJECT, submission.url) # sends user the message
                        break
    except Exception as ex:
        print(ex)
        time.sleep(60)


if __name__ == '__main__':
    start_time = time.time()
    reddit = access_reddit()
    find_posts(reddit)