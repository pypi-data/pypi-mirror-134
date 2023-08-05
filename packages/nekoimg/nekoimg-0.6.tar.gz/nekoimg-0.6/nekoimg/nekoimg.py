class nekoimg(self):
    import requests
    import webbrowser
    import pyautogui
    import time
    r = requests.get('https://nekos.life/api/v2/img/neko')
    res = r.json()
    print('Here is your neko img! you have 9 seconds to see it! and dont move until the tab close!')
    time.sleep(3)
    webbrowser.open(res['url'])
    time.sleep(9)
    pyautogui.hotkey('ctrl', 'w')