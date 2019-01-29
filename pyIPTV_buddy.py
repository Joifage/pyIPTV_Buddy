import search
import selection
import vlc
import categories
import download
import webbrowser
import os

m3u_url = ''
_vlc = vlc.vlc_path
_path = os.path.dirname(os.path.abspath(__file__))
_channel = None


def download_m3u():
    try:
        download.download_m3u(m3u_url)
    except Exception as e:
        print("Issue retrieving remote file, ERROR:", e)
        for file in os.listdir(_path):
            if file.endswith(".m3u"):
                pass
            else:
                print("m3u file not found/downloaded... exiting")
                exit(1)


def start(_channel):
    while True:
        s = search
        c = categories
        s._output = []
        os.system('cls')
        try:
            print("Now Playing:", _channel, '\n')
        except:
            pass
        print("""                         ________  _______    __     ____            __    __     
            ____  __  __/  _/ __ \/_  __/ |  / /    / __ )__  ______/ /___/ /_  __
           / __ \/ / / // // /_/ / / /  | | / /    / __  / / / / __  / __  / / / /
          / /_/ / /_/ // // ____/ / /   | |/ /    / /_/ / /_/ / /_/ / /_/ / /_/ / 
         / .___/\__, /___/_/     /_/    |___/    /_____/\__,_/\__,_/\__,_/\__, /  
        /_/    /____/                                                    /____/ 
    
                                    c = Categories
                                    t = Open TV Guide
                                    
                                     0. Exit
        """)
        _search = input("Enter search string or selection above: ").lower()
        if _search == "0":
            exit(0)
        elif _search == "c":
            c.categories()
            start(_channel)
        elif _search == "t":
            webbrowser.open('http://www.tvguide.co.uk/')
            start(_channel)
        elif _search == "":
            print("Input cannot be blank")
            input("Press enter to go back")
            start(_channel)
        else:
            search.search_result(_search)
            _output_length = len(s._output)
            if _output_length > 0:
                os.system('cls')
                try:
                    print("Now Playing:", _channel, '\n')
                except:
                    pass
                print(format('#', '<4'), format('| Name', '<75'), format('| Category', '<30'))
                print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
                      '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                i = 0
                for items in range(_output_length):
                    i += 1
                    print(format(str(i) + '.', '<4'), format('| ' + s._output[items][0], '<75'),
                          format('| ' + s._output[items][1], '<30'))
                _selection = selection.ask(_output_length)
                if _selection == 0:
                    start(_channel)
                else:
                    _selection -= 1
                    _channel = str(s._output[_selection][0])
                    _url = str(s._output[_selection][2])
                    vlc.launch(_channel, _url, _vlc)
            else:
                print("No results returned")
                input("Press enter to go back")
                start()

download_m3u()
start(_channel)
