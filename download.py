import urllib.request
import re
import os
import datetime

_path = os.path.dirname(os.path.abspath(__file__))
_file = _path + '\iptv.m3u'


def download_m3u(m3u_url):
    if os.path.isfile(_file) is True:
        try:
            _mtime = os.path.getmtime(_file)
            _file_mtime = (datetime.datetime.fromtimestamp(_mtime).strftime('%d/%m/%Y'))
            _today = datetime.datetime.today().strftime('%d/%m/%Y')
            if _file_mtime == _today:
                print("m3u file found and upto date.. skipping download.")
                pass
            else:
                _weburl = urllib.request.urlopen(m3u_url)
                _file_status = str(_weburl.getcode())
                _match = re.match('(^2)',
                                  _file_status) is not None
                if _match is True:
                    print("Status", _file_status, "- m3u file found on remote server")
                else:
                    print("Status", _file_status, "- An error may have occurred locating the remote file")
                print("Retrieving file from web server")
                urllib.request.urlretrieve(m3u_url, "iptv.m3u")
        except:
            pass
    else:
        _weburl = urllib.request.urlopen(m3u_url)
        _file_status = str(_weburl.getcode())
        _match = re.match('(^2)',
                          _file_status) is not None
        if _match is True:
            print("Status", _file_status, "- m3u file found on remote server")
        else:
            print("Status", _file_status, "- An error may have occurred locating the remote file")
        print("Retrieving file from web server")
        urllib.request.urlretrieve(m3u_url, "iptv.m3u")
