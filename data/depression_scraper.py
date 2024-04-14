import praw
import csv
import time
import random


reddit = praw.Reddit(
    client_id="FQ1mxfCo74PEEBFDH94DPw",
    client_secret="***",
    password="***",
    user_agent="linux:maskingmap:v1 (by u/No_Pitch4042)",
    username="No_Pitch4042"
)

urls = [
    "https://www.reddit.com/r/AskReddit/comments/7r779f/how_does_it_feel_to_have_depression/",
    "https://www.reddit.com/r/AskReddit/comments/2vmu0k/serious_what_are_some_of_your_experience_with/",
    "https://www.reddit.com/r/bipolar/comments/18n24xf/how_does_depression_feel_like_to_you/"
    
]


with open('/home/anopsy/Code/hackher/data/depression.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row if the file is empty:
    if file.tell() == 0:
        writer.writerow(["Comment"])

    #iterate over all URLs in the list
    for url in urls:
        submission = reddit.submission(url=url)
        # Replace MoreComments objects with all available comments
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
                # Write each comment to a new row in the CSV
                writer.writerow([comment.body])

  
  
#https://www.reddit.com/r/depression/comments/anh7tv/regular_checkin_post/
