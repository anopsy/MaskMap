import praw
import csv
import time
import random


reddit = praw.Reddit(
    client_id="FQ1mxfCo74PEEBFDH94DPw",
    client_secret="***",
    password="DejMieDane2137",
    user_agent="linux:maskingmap:v1 (by u/No_Pitch4042)",
    username="No_Pitch4042"
)

urls = [
    "https://www.reddit.com/r/Anxiety/comments/163onfb/what_is_your_scariest_anxiety_symptoms/",
    "https://www.reddit.com/r/AskReddit/comments/u4paqx/what_does_anxiety_feel_like_to_you/",
    "https://www.reddit.com/r/AskReddit/comments/96e0fg/how_does_it_feel_to_have_social_anxiety/",
    "https://www.reddit.com/r/AskReddit/comments/148jnrc/what_does_anxiety_physically_feel_like_to_you/",
    "https://www.reddit.com/r/Anxiety/comments/190eow3/what_were_your_first_signs_of_anxiety/"
]


with open('/home/anopsy/Code/hackher/data/anxiety.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Comment"])

    for url in urls:
        submission = reddit.submission(url=url)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
                # Write each comment to a new row in the CSV
                writer.writerow([comment.body])
                time.sleep(random.randint(0, 3))



        #anxiety
#https://www.reddit.com/r/Anxiety/comments/163onfb/what_is_your_scariest_anxiety_symptoms/  
#https://www.reddit.com/r/AskReddit/comments/u4paqx/what_does_anxiety_feel_like_to_you/
#https://www.reddit.com/r/AskReddit/comments/96e0fg/how_does_it_feel_to_have_social_anxiety/
#https://www.reddit.com/r/AskReddit/comments/148jnrc/what_does_anxiety_physically_feel_like_to_you/
#https://www.reddit.com/r/Anxiety/comments/190eow3/what_were_your_first_signs_of_anxiety/
        
        #depression
#https://www.reddit.com/r/AskReddit/comments/2vmu0k/serious_what_are_some_of_your_experience_with/
#https://www.reddit.com/r/depression/comments/anh7tv/regular_checkin_post/
