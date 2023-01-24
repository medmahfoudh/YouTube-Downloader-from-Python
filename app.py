from pytube import YouTube
from tkinter import *


window = Tk()
window.config(padx=30 , pady=30)
window.title("YouTube Downloader")

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)