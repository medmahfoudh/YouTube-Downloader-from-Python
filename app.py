from pytube import YouTube
from tkinter import *


window = Tk()
window.config(padx=30 , pady=30)
window.title("YouTube Downloader")

link_label=Label(text='Link:',font=('Courrier',12,'bold'))
link_label.grid(column=0, row=0)
link_label.config(padx=20,pady=20)
input_link_label = Entry()
input_link_label.grid(column=0 , row=1)

def Download():
    link = input_link_label.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


button_Download=Button(text='click to download' , command=Download)
button_Download.grid(column=2 , row= 1 )

# link = input("Enter the YouTube video URL: ")
# Download(link)

window.mainloop()