import streamlit as st
import whisper
import subprocess
import openai
import ffmpeg
import soundfile as sf
import numpy as np
#import av
#from pydub import AudioSegment
#import pyaudio
import wave
import sys
# Load environment variables
from dotenv import load_dotenv
import os

model = whisper.load_model("base")
audio = "audio.webm"
result = model.transcribe(audio)

with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])

st.write(result["text"])
