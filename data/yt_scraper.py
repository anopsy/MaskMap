from youtube_transcript_api import YouTubeTranscriptApi
import csv


video_ids = ["HiU1WRPJa-4", "0THO5gteINk", "uyQZcioe8BA", "Rjk2EtQVhHc"]
# Replace 'VIDEO_ID' with the ID of the video you want to scrape
# video_id = 'PNjfWYabkEc'


for id in video_ids:
    # Open a CSV file for writing
    with open('/home/anopsy/Code/hackher/data/transcript.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Start", "Duration", "Text"])  # Write the header
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(id)


        #Write each line of the transcript
        for entry in transcript:
            writer.writerow([entry['start'], entry['duration'], entry['text']])