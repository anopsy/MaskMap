
import praw
import csv
import time
import random


reddit = praw.Reddit(
    client_id="FQ1mxfCo74PEEBFDH94DPw",
    client_secret="QTTXx5llyMdHLyEqvyDtUlMmV-8KFw",
    password="DejMieDane2137",
    user_agent="linux:maskingmap:v1 (by u/No_Pitch4042)",
    username="No_Pitch4042"
)

urls = [
     "https://www.reddit.com/r/AskReddit/comments/2gq4z5/reddit_what_was_the_most_awkward_uncomfortable/",
     "https://www.reddit.com/r/DecidingToBeBetter/comments/plvd5m/whats_the_most_enjoyable_most_fun_thing_you_did/"

 
]
   


with open('/home/anopsy/Code/hackher/data/control.csv', 'a', newline='', encoding='utf-8') as file:
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

#"https://www.reddit.com/r/AskOldPeople/comments/16of69u/what_are_the_most_important_life_lessons_you_have/",
#   "https://www.reddit.com/r/Adulting/comments/15g5vyu/what_was_the_most_humbling_experience_of_your/",
#    "https://www.reddit.com/r/IndianTeenagers/comments/18fsvx8/females_what_is_the_most_gayest_experience_you/",
#   "https://www.reddit.com/r/socialskills/comments/yp00mc/people_who_got_their_first_experience_of_love_or/"
#    "https://www.reddit.com/r/AskReddit/comments/clh950/whats_the_creepiest_experience_in_your_life/",
#     "https://www.reddit.com/r/AskReddit/comments/6gsx2i/paranormal_or_not_what_is_the_scariest_creepiest/",
#     "https://www.reddit.com/r/AskReddit/comments/1bn1r9a/what_was_your_most_traumatic_life_experience/"