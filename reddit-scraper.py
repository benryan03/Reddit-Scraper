#reddit-scraper
print("Reddit scraper")

import praw
import wget
import os
import datetime

#getting user inputs
subreddit_input = input("Enter subreddit: /r/")
x = input("Enter sort order (hot, new, top): ")
image_number = int(input("Enter the number of submissions to parse (limit 1000): "))

#initializing PRAW things
reddit = praw.Reddit('main_account', user_agent='main_account user agent') #this logs into a reddit account specified in praw.ini
subreddit = reddit.subreddit(subreddit_input)

if x == "hot":
    sort_order = subreddit.hot
elif x == "new":
    sort_order = subreddit.new
elif x == "top":
    sort_order = subreddit.top

for submission in sort_order (limit=image_number):
    
    #this changes datetime to display time with . instead of : because : cannot be used in filenames
    date_and_time = str(datetime.datetime.fromtimestamp(submission.created))
    date_time_list = list(date_and_time)
    date_time_list[13] = "."
    date_time_list[16] = "."
    date_and_time_string = "".join(date_time_list)

    #this gets the reddit submission's title and the file extension of the submission's link
    submission_title_string = str(submission.title)
    print(submission.title, submission.url)
    file_extension = submission.url[len(submission.url) -4:]

    if file_extension == ".jpg" or file_extension == ".png" or file_extension == ".bmp" or file_extension == "jpeg" or file_extension == ".gif" or file_extension == "gifv": #if url is a direct image link

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

        if os.path.exists("downloads/" + date_and_time_string + " - " + submission_title_string + file_extension) == False:

            if file_extension == ".jpg":
                file_name = wget.download(submission.url,)
                os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .jpg")
            elif file_extension == ".png":
                file_name = wget.download(submission.url,)
                os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .png")
            elif file_extension == ".bmp":
                file_name = wget.download(submission.url,)
                os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .bmp")
            elif file_extension == "jpeg":
                file_name = wget.download(submission.url,)
                os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .jpeg")
            elif file_extension == ".gif":
                file_name = wget.download(submission.url,)
                os.rename(file_name, "downloads/" + date_and_time_string + " - " + submission_title_string + " .gif")
            print("\n")

        else:
            print("File already downloaded.\n")

    else:
        print("Submission is not a direct image link.")
