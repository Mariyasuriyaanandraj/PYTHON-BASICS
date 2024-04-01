# %%
pip install pytube

# %% [markdown]
# Normal Quality

# %%
from pytube import YouTube

def download_youtube_video(url, filename):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(url)

        # Select the highest resolution stream
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        # Download the video
        stream.download(filename=filename)
        print("Download successful!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage:
url = "https://www.youtube.com/watch?v=9Q_BHL6GFIk"
filename = "video.mp4"
download_youtube_video(url, filename)



# %% [markdown]
# High Resolution
# 

# %%
from pytube import YouTube

def download_youtube_video(url, filename):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(url)

        # Filter streams by resolution and select 720p
        stream = yt.streams.filter(res="720p").first()

        # Download the video
        stream.download(filename=filename)
        print("Download successful!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage:
url = "https://www.youtube.com/watch?v=9Q_BHL6GFIk"
filename = "video.mp4"
download_youtube_video(url, filename)



# %%



