print("This macro is currently in the beta version so there might be some bugs 'Press Enter to continue'")
input("")

import requests
import json
import pyautogui
import keyboard
import time

# macro stuff
print('Packages loaded')
seed_filter = input('Enter seed filter : ')
hotkey = input("Enter the key to be set as hotkey : ")
difficulty = int(input('input the difficulty "0 - normal , 1 - hard , 2 - easy" : '))
delay = int(input("Enter the dealy between click in milliseconds (minimum 70 recomended 3000) : ")) / 1000
pc = int(input("""Please select your pc power this macro runs without reading any of your pc files. please select your pc power based on the things given below 
If your pc has i3 or amdryzen3 or processors before with 4gb ram or below Enter '6'
If your pc has i3 or amdryzen3 with 8gb ram enter '4'
If your pc has a i5 or amdryzen5 or anything better with 8gb + ram select '3'  """))
print ('open minecraft in fullscreen or focused. you can minimize this window')
print ('this macro will start in 5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Macro started')
# 
# 
# 


def seedbank(filter):
    global seed
    print('sending request to seedbank')
    request = requests.get(f"http://fsg.gel.webfactional.com?filter={filter}")
    print('seed recived from seedbank')
    seed = json.loads(request.text)
    print(f"Response : {request.text} \n Response code : {request.status_code}")
    seed = seed['struct']
    return seed

def macro_seedbank(seed):
        pyautogui.press('Esc')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(delay)
        pyautogui.press('enter')

        print('escape done')

        pyautogui.press('tab')
        time.sleep(delay) 
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')        
        time.sleep(delay) 
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1) 
        pyautogui.press('tab')

        print('part done')

        if difficulty == 0:
            print('no change in diff')
        elif difficulty == 1:
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('enter')
        elif difficulty == 2:
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('enter')

        print('difficulty set')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(seed)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')






while True:
    if keyboard.is_pressed(hotkey) == True:
        seed = seedbank(seed_filter)
        print('reset initiatiated')
        print('recived seed')
        print(seed)
        macro_seedbank(seed)

