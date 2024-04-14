import praw
import csv
import time
import random

#reddit = praw.Reddit(
#    client_id="bfjUihVvdYPtItFAkZZBjQ",
#    client_secret="jkAGqRW0bov4zBX3LFhwgdI-2q2cTg",
#    password="DejMieDane2137",
#    user_agent="linux:maskmap:v1 (by u/No_Pitch4042)",
#    username="No_Pitch4042"
#)
reddit = praw.Reddit(
    client_id="FQ1mxfCo74PEEBFDH94DPw",
    client_secret="***",
    password="***",
    user_agent="linux:maskingmap:v1 (by u/No_Pitch4042)",
    username="No_Pitch4042"
)

urls = [
    "https://www.reddit.com/r/explainlikeimfive/comments/14vcmea/eli5_what_is_autistic_masking/", 
    "https://www.reddit.com/r/AutisticAdults/comments/18lehcn/people_whove_been_heavily_masking_what_has_been/",
    "https://www.reddit.com/r/autism/comments/11968n4/does_anyone_have_experience_with_high_iq_masking/",
    "https://www.reddit.com/r/AutismInWomen/comments/1bi0dcy/highmasking_ladies_how_did_you_knowrealize_that/",
    "https://www.reddit.com/r/AutisticAdults/comments/17ui2mx/for_those_with_good_social_skills_high_masking/",
    "https://www.reddit.com/r/AutismInWomen/comments/1b23nwd/question_for_those_who_have_masked_their_autistic/",
    "https://www.reddit.com/r/AutismInWomen/comments/15a934s/has_anyone_else_noticed_that_masking_just_got_way/",
    "https://www.reddit.com/r/AutismInWomen/comments/15wohoc/what_does_masking_lookfeel_like_for_you/",
    "https://www.reddit.com/r/aspergers/comments/5wlie3/theres_such_a_thing_as_autism_camouflaging_and_it/",
    "https://www.reddit.com/r/AutismInWomen/comments/15q7g1s/what_made_you_realize_you_were_maskingcamouflaging/",
    "https://www.reddit.com/r/aspergirls/comments/9d0pfc/how_do_you_know_when_youre_masking/",
    "https://www.reddit.com/r/sadposting/comments/14od9lj/average_autism_experience/",
    "https://www.reddit.com/r/autism/comments/14vg7sm/what_is_a_very_autistic_experience_you_could_tell/",
    "https://www.reddit.com/r/evilautism/comments/18cv1nk/the_autism_experience/",
    "https://www.reddit.com/r/autism/comments/13230ev/diagnosed_people_what_is_a_common_autistic/"
]


with open('/home/anopsy/Code/hackher/data/comments_reddit_unlimited.csv', 'a', newline='', encoding='utf-8') as file:
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
                time.sleep(random.randint(0, 3))


#https://www.reddit.com/r/AutisticAdults/comments/18lehcn/people_whove_been_heavily_masking_what_has_been/
#https://www.reddit.com/r/autism/comments/11968n4/does_anyone_have_experience_with_high_iq_masking/
#https://www.reddit.com/r/AutismInWomen/comments/1bi0dcy/highmasking_ladies_how_did_you_knowrealize_that/
#https://www.reddit.com/r/AutisticAdults/comments/17ui2mx/for_those_with_good_social_skills_high_masking/
#https://www.reddit.com/r/AutismInWomen/comments/1b23nwd/question_for_those_who_have_masked_their_autistic/
#https://www.reddit.com/r/AutismInWomen/comments/15a934s/has_anyone_else_noticed_that_masking_just_got_way/
#https://www.reddit.com/r/AutismInWomen/comments/15wohoc/what_does_masking_lookfeel_like_for_you/
#https://www.reddit.com/r/aspergers/comments/5wlie3/theres_such_a_thing_as_autism_camouflaging_and_it/
#https://www.reddit.com/r/AutismInWomen/comments/15q7g1s/what_made_you_realize_you_were_maskingcamouflaging/
#https://www.reddit.com/r/aspergirls/comments/9d0pfc/how_do_you_know_when_youre_masking/
#https://www.reddit.com/r/sadposting/comments/14od9lj/average_autism_experience/
#https://www.reddit.com/r/autism/comments/14vg7sm/what_is_a_very_autistic_experience_you_could_tell/
#https://www.reddit.com/r/evilautism/comments/18cv1nk/the_autism_experience/
#https://www.reddit.com/r/autism/comments/13230ev/diagnosed_people_what_is_a_common_autistic/

        #anxiety
#https://www.reddit.com/r/Anxiety/comments/163onfb/what_is_your_scariest_anxiety_symptoms/  
#https://www.reddit.com/r/AskReddit/comments/u4paqx/what_does_anxiety_feel_like_to_you/
#https://www.reddit.com/r/AskReddit/comments/96e0fg/how_does_it_feel_to_have_social_anxiety/
#https://www.reddit.com/r/AskReddit/comments/148jnrc/what_does_anxiety_physically_feel_like_to_you/
#https://www.reddit.com/r/Anxiety/comments/190eow3/what_were_your_first_signs_of_anxiety/
        
        #depression
#https://www.reddit.com/r/AskReddit/comments/2vmu0k/serious_what_are_some_of_your_experience_with/
#https://www.reddit.com/r/depression/comments/anh7tv/regular_checkin_post/