from depends import *  

def usage_menu():
    print("usage:\ngetlyrics [OPTIONS]...\n-h, --help --> This Help Menu\n-S, --spotify --> Returns the lyrics of the current spotify song if spotify is PLAYING\n-m, --mysong --> Returns the lyrics of the song specified after this argument within \"\"\n-o, --output --> Outputs the lyrics to the specified file ") 

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
        print('\n' + artist + ' ' +  song_name) 
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
    short_opts = '-S -m: -h -o:'
    long_opts = '--spotify --mysong: --help --output:'
    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
        
        for opt, arg in opts:
            if opt in ('-S', '--spotify'):
                if(os.popen('playerctl -p spotify status') == "Playing"):
                    artist = os.popen('playerctl -p spotify metadata artist').read()
                    song_name = os.popen('playerctl -p spotify metadata title').read()
                else:
                    sys.exit(1)
                opSong(artist,song_name)

            elif opt in ('-m', '--mysong'):
                opSong(arg,'')

            elif opt in ('-h', '--help'):
                usage_menu()

            elif opt in ('-o', '--output'):
                f = arg
                if(f == ''):
                    print("FILE NAME NOT SPECIFIED!!")
                else:
                    F = f + '.txt'
                    with open(F,'a+') as w:
                        global A
                        w.write(A)
                        print("Successfully written to file")
    except getopt.GetoptError as err:
        usage_menu()
        sys.exit(2)

if __name__ == "__main__":
    get_lyrics()
