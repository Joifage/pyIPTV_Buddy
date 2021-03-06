import os
import re

_path = os.path.dirname(os.path.abspath(__file__))
_output = []


def search_result(_search):
    for file in os.listdir(_path):
        if file.endswith(".m3u"):
            with open(file, encoding="utf8") as m3u_file:
                for line in m3u_file:
                    line1 = re.findall(r'tvg-name=\"(.*?)\"', line)
                    line2 = re.findall(r'group-title=\"(.*?)\"', line)
                    if _search.lower() in str(line1).lower():
                        try:
                            _group = [line1[0], line2[0], next(m3u_file).replace('\n', ''), ]
                        except Exception as e:
                            print(e)
                        if not ('-=' or '=-') in line[0]:
                            _output.append(_group)


def category_search(_cat_ask):
    for file in os.listdir(_path):
        if file.endswith(".m3u"):
            with open(file, encoding="utf8") as m3u_file:
                for line in m3u_file:
                    line1 = re.findall(r'tvg-name=\"(.*?)\"', line)
                    line2 = re.findall(r'group-title=\"(.*?)\"', line)
                    if _cat_ask.lower() in str(line2).lower():
                        try:
                            _group = [line1[0], line2[0], next(m3u_file).replace('\n', ''), ]
                        except Exception as e:
                            print(e)
                        if not ('-=' or '=-') in line[1]:
                            _output.append(_group)
