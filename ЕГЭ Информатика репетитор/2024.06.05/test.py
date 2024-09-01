from time import time
from pytube import YouTube, Playlist

playlist_link = "https://www.youtube.com/playlist?list=PLY-7sZHGtDzJ54dJIwV5UEzaDVvegbmnx"

video_links = Playlist(playlist_link).video_urls

video_titles = []
start = time()
for link in video_links:
    title = YouTube(link).title
    print(title)
    video_titles.append(title)

print("|||||||||||||||||")
text = "\n".join(video_titles)
print(text)

print(f'Time taken: {time() - start}')