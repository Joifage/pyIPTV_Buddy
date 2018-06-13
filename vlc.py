import subprocess
import time
import os


#for r in HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER:
#    global vlc_path
#    try:
#        r = OpenKey(r, 'Software\\VideoLAN\\VLC')
#        vlc_path = QueryValueEx(None, 'InstallDir')
#        print(vlc_path)#
#        CloseKey(r)
#        break
#    except error:
#        pass
global vlc_path

for vlc_dir in ':\Program Files\VideoLAN\VLC\VLC.exe', ':\Program Files (x86)\VideoLAN\VLC\VLC.exe':
    for drive in 'a', 'b', 'c', 'd', 'e', 'f', 'g':
        found = os.path.isfile(drive + vlc_dir)
        if found is True:
            vlc_path = drive + vlc_dir
            print("VLC Player found:", vlc_path)
            break

if vlc_path is None:
    print("VLC Player not found")
    input("Press enter to exit")
    exit()


def launch(_channel, _url, _vlc):
    print("Sending channel:", _channel, "to vlc player...")
    try:
        subprocess.Popen(str(_vlc) + ' ' + str(_url))
        time.sleep(3)
        #os.system('python pyIPTV_buddy.py')
        #return
    except Exception as e:
        print(e)
        input("Press Enter to continue")
