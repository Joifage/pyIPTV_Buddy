import subprocess


def launch(_channel, _url, vlc):
    print("Sending channel:", _channel, "to vlc player...")
    try:
        subprocess.Popen(vlc + ' ' + str(_url))
    except Exception as e:
        print(e)