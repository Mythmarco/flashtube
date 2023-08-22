# <img src="static/content.png" width="100" height="100" style="vertical-align: middle;"> FlashTube <i><span style="font-size: 0.8em;">for the "busy"</span></i>

## Video Demo: https://www.youtube.com/watch?v=mkeV2Bt4pxI&ab_channel=MS

## Overview
In today's fast-paced world, staying updated with your favorite YouTube content can be a challenge. Introducing FlashTube, a revolutionary application designed to provide concise and insightful summaries of YouTube videos. Whether you're looking to catch up on the latest trends, follow educational content, or simply explore new entertainment, FlashTube offers a quick overview at your fingertips. 

## Installation

This app requires Python 3.10 or later. You will also need to install the necessary Python libraries, which are listed in the requirements.txt file. You can install these dependencies with pip:


Copy code
```pip install -r requirements.txt```
Usage
To run the app, navigate to the application's directory and execute the following command:

Copy code
```streamlit run flashtube.py```

The application will then be accessible in your web browser at http://localhost:8501.

## Usage:
Enter the youtube link in the box.
Click on the "Get Summary" button.

## Features:
It uses openai whisper api to transcribe the audio of the video.
It uses GPT-4 to generate the summary of the video.

## Description:
The app indludes two main files, the flashtbe.py whcih contains the streamlit app, and the util.py file that contains my functions.

The main app is a brief front end with the title of the app and a text input, where the user can enter the youtube link. The app has a function that is called when text is input into the text box. This function will check if the input is a valid youtube link. If it is, the app will display a message and some ballons animation showing that the link is valid, otherwise if the link is invalid, the app will show an alarm saying the youtube link is not valid. THis is done using a request to the youtube link and if it returns a 200 status code, then the link is valid.

Once the user clicks on the "Get Summary" button, the app will execute three different functions from the util.py file.

1.- The first funtion is the download function, I found a library called pytube, that helps with downloading data from youtube links in my case Im downloading the audio of the video to the root folder.

2.- The second function is the transcribe function, which takes an audio file as argument and transcribes the audio using OpenAI api and the whisper model. The function will return the transcription of the audio.

3.- The third function is the generate_summary function, which uses also OpenAI api and the 3.5 turbo model via chat completions to request gpt-3.5 to generate a summary of the video, bulletpoints with key info and a pruppose of the video. It returns this summary in a string. which is then parsed with markdown to display it in the app.

These three functions are called in the main app, and the app will show the summary of the viewo at the end. THe intent was to create a workflow for this solution and learn how to quickly deploy something like this that could help someone like me that doesnt have time to watch a 30 min video, but would like to know what the video is about.

## Author

- [Marco Saenz]((https://github.com/Mythmarco))

## License

This project is [MIT licensed](./LICENSE).

<a href="https://www.flaticon.com/free-icons/ai" title="ai icons">Ai icons created by Freepik - Flaticon</a>
