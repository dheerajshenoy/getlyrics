from depends import *  


A = ""
def usage_menu():
    print("usage:\ngetlyrics [OPTIONS]...\n-h, --help --> This Help Menu\nFor SPOTIFY LYRICS --> Just run the program without any arguments\nFor other songs --> Run the program with song name as the argument within DOUBLE QUOTES\nEXAMPLE: getlyrics \"tool lateralus\"\n")
def opSong(artist,song_name):
    artist = artist.strip('\n')
    song_name = song_name.strip('\n')
    song_name = song_name.replace("'",'')
    print("\nFINDING LYRICS FOR " + artist.capitalize() + " " + song_name.capitalize())
    if("Remaster" in song_name or "Alternate Mix" in song_name or "Rough Mix" in song_name):
        p = imp.pos('-',song_name)
        song_name = song_name[:p-1]
        system("clear")

    if(song_name == ''):
        NAME = artist.replace(' ','-')
        NAME.replace(' ','-')
        NAME = str(NAME) + '-lyrics'
    else:
        NAME = artist.replace(' ','-') + '-' + song_name.replace(' ','-') 
        NAME = str(NAME) + '-lyrics'
    respond = requests.get("https://www.genius.com/" + NAME)
    try:
        if(respond.status_code == 200):
            soup = BeautifulSoup(respond.text,"lxml")
            s = soup.find('div',class_="lyrics")
            global A
            A = s.text.strip('\n')
            print('\n' + A)
        elif(respond.status_code == 404):
            print("Check that song name again")
        else:
            print("Something went wrong")
    except:
        print("UH OH")

def get_lyrics():
    argv = sys.argv[1:]
    short_opts = '-S -m: -h'
    long_opts = '--spotify --mysong: --help'
    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
        
        for opt, arg in opts:
            if opt in ('-S', '--spotify'):
                artist = os.popen('playerctl -p spotify metadata artist').read()
                song_name = os.popen('playerctl -p spotify metadata title').read()
                opSong(artist,song_name)
            elif opt in ('-m', '--mysong'):
                opSong(arg,'')

            elif opt in ('-h', '--help'):
                usage_menu()

    except getopt.GetoptError as err:
        usage_menu()
        sys.exit(2)

if __name__ == "__main__":
    get_lyrics()
