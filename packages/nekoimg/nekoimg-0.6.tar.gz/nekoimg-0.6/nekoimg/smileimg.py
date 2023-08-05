class smileimg(self):
    import requests
    import webbrowser
    import pyautogui
    import time
    r = requests.get('https://nekos.life/api/v2/img/smile')
    res = r.json()
    print('Here is your smile gif! you have 9 seconds to see it! and dont move until the tab close!')
    time.sleep(3)
    webbrowser.open(res['url'])
    time.sleep(9)
    pyautogui.hotkey('ctrl', 'w')