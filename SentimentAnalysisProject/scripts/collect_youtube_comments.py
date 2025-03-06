from googleapiclient.discovery import build
import pandas as pd
import os
import re  # Import the regular expression module

# Retrieve API Key from environment variables
api_key = os.environ.get("YOUTUBE_API_KEY")
if not api_key:
    raise ValueError("YOUTUBE_API_KEY environment variable not set.")

youtube = build('youtube', 'v3', developerKey=api_key)


def extract_video_id(url):
    """Extracts the video ID from a YouTube URL.

    Args:
        url (str): The YouTube video URL.

    Returns:
        str: The video ID, or None if the URL is invalid.
    """
    try:
        # Regular expression to match various YouTube URL formats
        pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/(?:watch)?\?(?:.*&)?v=)|youtu\.be\/)([\w-]+)(?:[^\w-]|$)"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            return None
    except:
        return None


def get_video_comments(video_id, max_results=100):
    """Retrieves comments from a YouTube video."""
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            textFormat="plainText",
            maxResults=max_results  # Adjust as needed (max is usually 100)
        )
        response = request.execute()

        while response:  # Handle pagination of results
            for item in response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                comments.append(comment)

            if 'nextPageToken' in response:
                request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId=video_id,
                    textFormat="plainText",
                    pageToken=response['nextPageToken'],
                    maxResults=max_results
                )
                response = request.execute()
            else:
                break  # No more pages
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list if there is an error.

    return comments


# Get YouTube video URL from user input
video_url = input("https://youtu.be/eAJ30sL-ZsM?si=cRuVEcIssBoXiRkw")

# Extract video ID from the URL
video_id = extract_video_id(video_url)

if video_id:
    comments = get_video_comments(video_id)

    if comments:
        df = pd.DataFrame({'Comment': comments})
        print(df.head())
        df.to_csv('data/youtube_comments.csv', index=False)
        print("Comments saved to data/youtube_comments.csv")
    else:
        print("No comments retrieved or an error occurred.")
else:
    print("Invalid YouTube video URL.")