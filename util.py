import openai
import os
from dotenv import load_dotenv
from pytube import YouTube
import requests
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def download(youtubelink):
    try:
        # Create a YouTube object
        yt = YouTube(youtubelink)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        audio_stream.download(output_path='.', filename='audio.mp3')

        return 'audio.mp3'
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def transcribe(audio_file_path):
    # Open the audio file
    with open(audio_file_path, 'rb') as audio_file:
        # Transcribe the audio file
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript


def generate_summary(model, transcript):

    summary = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role":"user", "content":"You are an expert ai that helps create comprehensive summaries of youtube videos."},
            {"role":"user", "content":"Create a summary of the transcript of the video. Ensure you have a brief summary of the video, bullet points with the most important takeaways, and the purpose of the video."},
            {"role":"user", "content":"The summary consists of 3 parts: 1.- Ensure you have a brief summary of the video, 2.- bullet points with the most important takeaways, and 3.- the purpose of the video."},
            {"role":"system", "content":"Sure, I can help with that, please provide the transcript of the youtube video"},
            {"role":"user", "content":str(transcript)},
        ],
        temperature=0, #The temperature parameter controls the randomness of the generated output.
    )
    # Extract the summary text from the response
    summary = summary['choices'][0]['message']['content']
    return summary

def is_valid_youtube_link(youtube_link):
    try:
        response = requests.get(youtube_link)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False