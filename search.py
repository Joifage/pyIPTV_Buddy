import os
import re

_path = os.path.dirname(os.path.abspath(__file__))
_output = []


def search_result(_search):
    for file in os.listdir(_path):
        if file.endswith(".m3u"):
            with open(file, encoding="utf8") as m3u_file:
                for line in m3u_file:
                    line = re.findall(r'\"(.*?)\"', line)
                    if _search.lower() in str(line).lower():
                        try:
                            _group = [line[1], line[3], next(m3u_file).replace('\n', ''), ]
                        except:
                            _group = [line[1], line[2], next(m3u_file).replace('\n', ''), ]
                        if not ('-=' or '=-') in line[1]:
                            _output.append(_group)
