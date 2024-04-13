import praw
import csv

reddit = praw.Reddit(
    client_id="bfjUihVvdYPtItFAkZZBjQ",
    client_secret="jkAGqRW0bov4zBX3LFhwgdI-2q2cTg",
    user_agent="linux:maskmap:v1 (by u/No_Pitch4042)"
)

url = "https://www.reddit.com/r/explainlikeimfive/comments/14vcmea/eli5_what_is_autistic_masking/"
submission = reddit.submission(url=url)

with open('/home/anopsy/Code/hackher/data/comments.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Comment"])

    for top_level_comment in submission.comments:
        writer.writerow([top_level_comment.body])
        print(top_level_comment.body)

