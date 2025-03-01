from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from Ollama import summaryOllama
from ChatGPT import summaryGPT

def get_video_title(video_id): # Gets the video title, incase the function name wasn't obvious enough, dunno how it works the black magic is done behind the yt_dlp library curtains
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'noplaylist': True, 
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', 'Title not found')

def main():
    print("Make sure you put in the video ID, NOT the whole URL.")
    video_id = input("Video ID: ") # TO DO: Make it so that it does let you put in the whole URL and move the print command to after when the user puts an incorrect input.

    video_title = get_video_title(video_id) # Calls the function
    print(f"Video Title: {video_title}")

    Transcription = YouTubeTranscriptApi.get_transcript(video_id)
    prompt = f"Summarize the following content in 10 bullet points with timestamps: 1. Video Title: {video_title}; 2. Transcript: {Transcription}"
    
    while True:
        aiUserChoice = input("Type '1' if you want to summarize locally (via Ollama) or type '2' via ChatGPT: ")
        
        if aiUserChoice == "1": # Summarizes using whatever local AI you have.
            print("Everything works! Moving onto the summarry...")
            summaryOllama(Transcription, video_title, prompt)
            break

        elif aiUserChoice == "2": # Opens a chatgpt tab and pastes the transcript alongside a prompt. TO DO: implement chatgpt API
            print("Everything works! Moving onto the summarry...")
            summaryGPT(Transcription, video_title, prompt)
            break

        else:
            print("Enter a valid number (1 or 2)")
            continue

if __name__ == "__main__":
    main()