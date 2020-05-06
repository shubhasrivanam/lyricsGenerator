import json
from musixmatch import Musixmatch

i = 1
while i==1:
    print("Welcome to the lyric generator!")
    song = input("Enter the name of the song you are looking for ")
    artist = input("Enter the name of the artist ")
    print()
    musixmatch = Musixmatch("41ea8cb5f8bb3296825e68afa4fca92a")
    lyrics = musixmatch.matcher_lyrics_get(song, artist)
    print (lyrics['message']['body']['lyrics']['lyrics_body'])
    print("To exit enter 0")
    i = int(input())
    
