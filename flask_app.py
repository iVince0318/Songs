# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

from Songs import find_artist, find_title, find_key, load_songs

app = Flask(__name__)


def display_song(song):
    ret = '<p>'
    for field in song:
        ret += f'<b>{field}:</b> {song[field]}<br>'
    ret += '</p>'
    return ret


@app.route("/", methods=["GET", "POST"])
def find_songs():
    load_songs()
    if request.method == "GET":
        page = """
<div align="center">
<h1>Song Finder</h1>
</div>

<p>
Use this app to search Vincent's catalogue of songs.
</p>

<form method="post" action=".">
    <p>Artist: <input name="artist" /></p>
    <p>Title: <input name="title" /></p>
    <p>Key: <input name="key" /></p>
    <p><input type="submit" value="Search" /></p>
</form>
"""
    else:
        page = '<div align="center"><h1>Search Results</h1></div>'
        songs = []
        artist = request.form["artist"]
        if artist:
            songs = find_artist(artist)
        else:
            title = request.form["title"]
            if title:
                songs = find_title(title)
            key = request.form["key"]
            if key:
                songs = find_key(key)
        if songs:
            for song in songs:
                page += display_song(song)
        else:
            page = 'no songs found'   
    return page