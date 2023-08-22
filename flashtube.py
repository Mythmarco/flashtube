import streamlit as st
import util
import os
import time

st.set_page_config(page_title="FlashTube", page_icon="static/play.png", layout='wide')
import base64
# Function to read binary data and convert to base64
def get_image_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Convert your images to base64
sr2new = get_image_base64('static/content.png')
# Include the base64 images in your HTML
st.markdown(
    f"""
    <div class="container">
        <h2 class="text-center mt-4">
            <img src="data:image/png;base64,{sr2new}" width="75" height="75" class="d-inline-block align-top" alt="">
            FlashTube <span style="font-style: italic; font-size: 17px;">for the "busy"</span>
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("Introducing FlashTube, a revolutionary application designed to provide concise and insightful summaries of YouTube videos.")

transcripts = os.path.join(os.getcwd(), 'transcripts')


youtubelink = st.text_input('Enter the youtube link here:')

if youtubelink:
    if util.is_valid_youtube_link(youtubelink):
        st.balloons()
        st.success('Congrats. Youtube Link is correct and valid')
    else:
        st.error('This is not a valid youtube link', icon="🚨")
    
    if st.button('Summarize'):
        with st.spinner('Downloading...'):
            time.sleep(5)
            audio = util.download(youtubelink)
        with st.spinner('Transcribing...'):
            transcript = util.transcribe(audio)
        with st.spinner('Generating Summary...'):
            summary = util.generate_summary('gpt-3.5-turbo-16k', transcript)
        st.markdown("**Summary**", unsafe_allow_html=True)
        st.markdown(summary, unsafe_allow_html=True)

st.markdown("""
<footer class="footer mt-auto py-3">
    <div class="container text-center">
        <p class="text-muted">
            Final Project for CS50's Introduction to Computer Science | Harvard University |<p></p>
            Copyright © 2023 | Marco Saenz| All Rights Reserved |  MSMMXXIII |
            <a href="https://www.linkedin.com/in/marco-saenz-pmp/" target="_blank">LinkedIn</a> |
            <a href="https://github.com/Mythmarco" target="_blank">GitHub</a> |
        </p>
    </div>
</footer>
""", unsafe_allow_html=True)