from telnetlib import PRAGMA_HEARTBEAT
import requests
import platform
import os, ctypes, sys
import time

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
FILENAME = 'nasa_pic.png'


def get_filename():
    
    if platform.system()=="Linux":
        import pwd
        username = pwd.getpwuid(os.getuid()).pw_name
        directory = "/home/" + username + "/Downloads/"
    elif platform.system()=="Darwin":
        import pwd
        username = pwd.getpwuid(os.getuid()).pw_name
        directory = "/Users/" + username + "/Downloads/"
    elif platform.system()=="Windows":
        username = os.getenv('username')
        directory = 'C:\\Users\\' + username + '\\Desktop'
    
    return os.path.join(directory, FILENAME)

def check_internet_connection():
    while True:
        try:
            requests.get(url).status_code
            return True
        except :
            print("Check Your Internet Connection")
            time.sleep(3)
    
def download_pic_of_day():
   
#    if  check_internet_connection() is True :
        r = requests.get(url)

        if r.status_code != 200:
            print('error')
            return
    
        picture_url = r.json()['url']
        if "jpg" not in picture_url:
            print("No image for today, must be a video")
        else:
            pic = requests.get(picture_url , allow_redirects=True)
            filename = get_filename()
        
            open(filename, 'wb').write(pic.content)
        
            print(f"saved picture of the day to {filename}!")
       
if __name__ == '__main__':
    if check_internet_connection() is True:
        download_pic_of_day()
        filename = get_filename()

    # set background
        if platform.system()=="Linux":
            os.system(cmd)
            cmd = "gsettings set org.gnome.desktop.background picture-uri file:" + filename
        elif platform.system()=="Darwin":
            os.system(cmd)    
            cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename +"\"'"
        # use absolute path to the image, and not a path that begins with a user path (~/Downloads/image.jpg)!

        elif platform.system()=="Windows":
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+ filename+' /f')
            os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
            sys.exit()
            
