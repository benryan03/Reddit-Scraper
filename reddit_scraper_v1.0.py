#reddit_scraper_v1.1
print("Reddit scraper")

import praw
import wget
import os

reddit = praw.Reddit('main_account', user_agent='main_account user agent') #this logs into a reddit account specified in praw.ini

subreddit_input = input("Enter subreddit: ")
image_number = int(input("Enter the number of submissions to parse (limit 1000): "))

subreddit = reddit.subreddit(subreddit_input)

for submission in subreddit.new(limit=image_number):

    print(submission.title, submission.url)
    file_extension = submission.url[len(submission.url) -4:]
    print("file_extension: " + file_extension)
    if file_extension == ".jpg" or file_extension == "png" or file_extension == ".bmp" or file_extension == "jpeg": #if url is a direct image link
        file_name = wget.download(submission.url,)    
        os.rename(file_name, "downloads/" + submission.title + " .jpg") 
        print("\n")
    else:
        print("Submission is not a direct image link.")

print("DEBUG: end")
