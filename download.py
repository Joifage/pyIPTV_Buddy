import urllib.request
import re


def download_m3u(m3u_url):
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
