#reddit_scraper_v1.0
print("Reddit scraper")

import praw
import wget
import os

reddit = praw.Reddit('main_account', user_agent='main_account user agent')

subreddit = reddit.subreddit('pics')
new_subreddit = subreddit.new()

for submission in subreddit.new(limit=3):  #hard limit is 1000

    print(submission.title, submission.url)
    file_name = wget.download(submission.url,)    
    os.rename(file_name, "downloads/" + submission.title + " .jpg") 
    print("\n")

print("DEBUG: end")