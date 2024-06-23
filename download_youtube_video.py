import pytube

# Define the YouTube video URL
video_url = "https://www.youtube.com/watch?v=DFJoYL7lS54"

# Create a YouTube object
youtube = pytube.YouTube(video_url)

# Get the highest resolution video stream
stream = youtube.streams.get_highest_resolution()

# Download the video
stream.download(output_path="path_to_save_video")

print("Video downloaded successfully!")
