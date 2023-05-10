from pytube import YouTube
import tkinter as tk
import sys

def download_vid(root, link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    if yt is not None:
        try:
            print(yt.title)
            yt.download()
        except:
            print("An error has occurred")
            sys.exit(1)
        success_label = tk.Label(root, text="Download successful")
        success_label.place(relx=0.5, rely=0.7, anchor="center")
    else:
        faliure_label = tk.Label(root, text="Download faliure")
        faliure_label.place(relx=0.5, rely=0.7, anchor="center")
        
            

def vid(root):
    vid_frame = tk.Frame(root, width=1200, height=600)
    vid_frame.place(x=0, y=0)
    info = tk.Label(vid_frame, text="You're downloading a single video")
    info.place(relx=0.5, rely=0.1, anchor="center")
    link_label = tk.Label(vid_frame, text="Input video link")
    link_entry = tk.Entry(vid_frame, width=75)
    download = tk.Button(vid_frame, text="DOWNLOAD", width=50, height=5, command=lambda: download_vid(vid_frame, link_entry.get()))
    link_label.place(relx=0.1, rely=0.2)
    link_entry.place(relx=0.1, rely=0.25)
    download.place(relx=0.3, rely=0.4)

def playlist(root):
    playlist_frame = tk.Frame(root, width=1200, height=600)
    playlist_frame.place(x=0, y=0)
    info = tk.Label(playlist_frame, text="You're downloading a playist")
    info.place(relx=0.5, rely=0.1, anchor="center")
    link_label = tk.Label(playlist_frame, text="Input playlist link")
    link_entry = tk.Entry(playlist_frame, width=75)
    download = tk.Button(playlist_frame, text="DOWNLOAD", width=50, height=5)
    link_label.place(relx=0.1, rely=0.2)
    link_entry.place(relx=0.1, rely=0.25)
    download.place(relx=0.3, rely=0.4)

def main():
    root = tk.Tk()
    root.title("YT video downloader")
    root.geometry("1200x600")
    frame = tk.Frame(root, width=1200, height=600)
    frame.place(x=0, y=0)
    question = tk.Label(frame, text="What do you want to download?")
    button_vid = tk.Button(frame, text="Single video", width=50, height=5, command=lambda: vid(root))
    button_playlist = tk.Button(frame, text="Playlist", width=50, height=5, command=lambda: playlist(root))
    question.place(relx=0.5, rely=0.1, anchor="center")
    button_vid.place(relx=0.5, rely=0.3, anchor="center")
    button_playlist.place(relx=0.5, rely=0.5, anchor="center")
    root.mainloop() 
    
main()