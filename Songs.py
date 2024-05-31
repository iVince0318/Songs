"""
this program manages a song database
to run it, first type `cd python`
then type `python Songs.py`
"""
import csv

songs = None
    # {
    #     'title': 'Tennessee Whiskey',
    #     'artist': 'Chris Stapleton',
    #     'key': 'A',
    #     'chords': 'A-Bm',
    #     'lyrics': '',
    # },
    # {
    #     'title': 'Your Man',
    #     'artist': 'Josh Turner',
    #     'key': 'F#',
    #     'chords': 'B-F#-D',  # refrain chords ascending
    #     'lyrics': '',
    # },
    # {
    #     'title': "I'm Gonna Be 500 Miles",
    #     'artist': 'The Proclaimers',
    #     'key': 'E',
    #     'chords': 'E-A-B',
    #     'lyrics': '',
    # },
    # {
    #     'title': "I'm Yours",
    #     'artist': 'Jason Mraz',
    #     'key': 'B',
    #     'chords': 'B-F#-G#m-E',
    #     'lyrics': '',
    # },
    # {
    #     'title': "My Girl",
    #     'artist': 'Tropa Vibes Reggae',
    #     'key': 'C',
    #     'chords': 'C-F-G', # Change key whole step
    #     'lyrics': '',
    # },
    # {
    #     'title': "Fast Car",
    #     'artist': 'Tracy Chapman',
    #     'key': 'C',
    #     'chords': 'C-G-Em-D',
    #     'lyrics': '',
    # },
# ]


def print_song(song):
    if isinstance(song, str):
        print(song)
        return
    print('****')
    print('Title: ' + song['title'])
    print('Artist: ' + song['artist'])
    print('Key: ' + song['key'])
    print('Chords: ' + song['chords'])
    print('Lyrics: ' + song['lyrics'])
    print('****')


def find_artist(artist):
    matches = []
    for song in songs:
        if artist in song['artist']:
            matches.append(song)
    return matches


def find_key(key):
    matches = []
    for song in songs:
        if song['key'] == key:
            matches.append(song)
    return matches


def find_chords(chords):
    matches = []
    for song in songs:
        if chords in song['chords']:
            matches.append(song)
    return matches
    return f'{chords} not found'


def find_title(title):
    matches = []
    for song in songs:
        if song['title'] == title:
            matches.append(song)
    return matches
    return f'{chords} not found'


def find_value(field, value):
    matches = []
    for song in songs:
        if value in song[field]:
            matches.append(song)
    return matches
    return f'{value} not found'
    

def handle_choice(prompt, field):
    search_text = input(prompt)
    matches = find_value(field, search_text)
    if len(matches) == 0:
        print('result: no song for ' + search_text)
    else:
        for song in matches:
            print_song(song) 


def load_songs():
    global songs
    songs = []
    with open("mysite/Songs.csv", 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                # print(f'{i=}, {value=}')
                record[headers[i]] = value
            songs.append(record)
    return songs


def main():
    songs = load_songs()
    print(songs)
    while True:
        print('1: Find an artist')
        print('2: Find a song in a key')
        print('3: Find a song with chords')
        print('4: Find chords for a song title')
        print('x: Exit')
        choice = input('Make a choice from the menu above: ')
        if choice == 'x':
            print('thanks for using my song program')
            break
        elif choice == '1':
            handle_choice("Type the artist's name: ", 'artist')        
        elif choice == '2':
            handle_choice("Type the key: ", 'key')        
        elif choice == '3':
            handle_choice("Type the chords: ", 'chords')
        elif choice == '4':
            handle_choice("Type the song title: ", 'title')    


if __name__ == '__main__':
    main()