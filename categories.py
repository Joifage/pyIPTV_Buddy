import os
import re
import search
import selection
import vlc

_path = os.path.dirname(os.path.abspath(__file__))
s = search
_vlc = vlc.vlc_path
_output = []


def categories():
    for file in os.listdir(_path):
        if file.endswith(".m3u"):
            with open(file, encoding="utf8") as m3u_file:
                for line in m3u_file:
                    if '#EXTINF' in line:
                        line = re.findall(r'\"(.*?)\"', line)
                        if line[3] != '':
                            if line[3] not in _output:
                                _output.append(line[3])

    _output_new = list(filter(None, _output))
    _output_length = len(_output_new)
    _ask = -99
    while _ask <= 0 or _ask >= _output_length:
        s._output = []
        _output_length = len(_output_new)
        os.system('cls')
        try:
            print("Now Playing:", _channel, '\n')
        except:
            pass
        print(format('#', '<4'), format('| Category', '<30'))
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        i = 0
        for items in range(_output_length):
            i += 1
            print(format(str(i) + '.', '<4'), format('| ' + _output_new[items], '<30'))

        print("\n\t0. Go Back")
        try:
            _ask = int(input("\nSelect a category: "))
        except ValueError:
            pass
        if _ask > 0 and _ask <= _output_length:
            _ask -= 1
            _cat_ask = str(_output_new[_ask])
            search.category_search(_cat_ask)
            _output_length = len(s._output)
            _selection = -99
            while _selection <= 0 or _selection >= _output_length:
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
                try:
                    _selection = selection.ask(_output_length)
                except ValueError:
                    input("Invalid selection... press enter to go back")
                if 0 < _selection <= _output_length:
                    _selection -= 1
                    _channel = str(s._output[_selection][0])
                    _url = str(s._output[_selection][2])
                    vlc.launch(_channel, _url, _vlc)
                elif _selection == 0:
                    return
                else:
                    input("Invalid selection... press enter to go back")
        elif _ask == 0:
           return
        else:
            input("Invalid selection... press enter to go back")
