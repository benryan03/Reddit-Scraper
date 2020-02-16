#reddit_scraper_v1.4
print("Reddit scraper")

import praw
import wget
import os
import datetime

global date_and_time_string

def change_time_format(time): #this function changes datetime to display time with . instead of : because : cannot be used in filenames
    global date_and_time_string
    date_and_time = str(datetime.datetime.fromtimestamp(submission.created))
    date_time_list = list(date_and_time)
    date_time_list[13] = "."
    date_time_list[16] = "."
    date_and_time_string = "".join(date_time_list)
    print(date_and_time_string)

reddit = praw.Reddit('main_account', user_agent='main_account user agent') #this logs into a reddit account specified in praw.ini

subreddit_input = input("Enter subreddit: /r/")
image_number = int(input("Enter the number of submissions to parse (limit 1000): "))

subreddit = reddit.subreddit(subreddit_input)

for submission in subreddit.new(limit=image_number):

    change_time_format(submission.created)
    submission_title_string = str(submission.title)
    print(submission.title, submission.url)
    file_extension = submission.url[len(submission.url) -4:]
    print("file_extension: " + file_extension)

    if file_extension == ".jpg" or file_extension == "png" or file_extension == ".bmp" or file_extension == "jpeg": #if url is a direct image link

        #if submission title includes character not usable in filename:
        if ("?" in str(submission_title_string) 
        or "/"  in str(submission_title_string)
        or "\\" in str(submission_title_string)
        or ":" in str(submission_title_string)
        or "*" in str(submission_title_string)
        or "\"" in str(submission_title_string)
        or "<" in str(submission_title_string)
        or ">" in str(submission_title_string)
        or "|" in str(submission_title_string)):

            #change illegal character
            submission_title_string = submission_title_string.replace("?", "&#63")
            submission_title_string = submission_title_string.replace("/", "&#47")
            submission_title_string = submission_title_string.replace("\\", "&#92")
            submission_title_string = submission_title_string.replace(":", "&#58")
            submission_title_string = submission_title_string.replace("\"", "&#92")
            submission_title_string = submission_title_string.replace("<", "&#60")
            submission_title_string = submission_title_string.replace(">", "&#62")
            submission_title_string = submission_title_string.replace("|", "&#124")
            submission_title_string = submission_title_string.replace("*", "&#42")


        if os.path.exists("downloads/" + date_and_time_string + " - " + submission_title_string + " .jpg") == False:
            file_name = wget.download(submission.url,)
            os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .jpg") 
            print("\n")

        else:
            print("File already downloaded.\n")
    else:
        print("Submission is not a direct image link.")
