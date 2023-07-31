import streamlit as st
import whisper

model = whisper.load_model("base")
audio = "audio.mp3"
result = model.transcribe(audio)

with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])

st.write(result["text"])
