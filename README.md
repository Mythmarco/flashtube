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

## Features
It uses openai whisper api to transcribe the audio of the video.
It uses GPT-4 to generate the summary of the video.

## Author

- [Marco Saenz]((https://github.com/Mythmarco))

## License

This project is [MIT licensed](./LICENSE).

<a href="https://www.flaticon.com/free-icons/ai" title="ai icons">Ai icons created by Freepik - Flaticon</a>
