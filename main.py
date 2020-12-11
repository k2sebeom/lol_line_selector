# from PIL import ImageGrab
# import cv2
# import numpy as np
import keyboard
# import mouse
# import ctypes
import time


# def find_chatbox():
#     screen = np.array(ImageGrab.grab())
#     k_w = user32.GetSystemMetrics(0) / screen.shape[1]
#     k_h = user32.GetSystemMetrics(1) / screen.shape[0]
#     gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
#     result = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF)
#     _, _, min_loc, _ = cv2.minMaxLoc(result)
#     x, y = min_loc
#     h, w = template.shape
#
#     x += w // 2
#     y += h // 2
#
#     mouse.move(x * k_w, y * k_h)
#     mouse.click()


def write_on_chat(line):
    keyboard.write(line)
    keyboard.press_and_release('enter')


if __name__ == '__main__':
    # user32 = ctypes.WinDLL('user32', use_last_error=True)

    # template = cv2.imread("template.png", 0)

    print('''
    채팅창을 클릭하고 원하는 라인에 맞는 단축키를 꾸욱 누르세요.
    
    f1: ㅅㅍ
    f2: ㅈㄱ
    f3: ㅇㄷ
    f4: ㅁㄷ
    f5: ㅌ
    
    종료를 위해서는 esc 를 누르세요.''')
    while True:
        if keyboard.is_pressed('f1'):
            write_on_chat('ㅅㅍ')
        elif keyboard.is_pressed('f2'):
            write_on_chat('ㅈㄱ')
        elif keyboard.is_pressed('f3'):
            write_on_chat('ㅇㄷ')
        elif keyboard.is_pressed('f4'):
            write_on_chat('ㅁㄷ')
        elif keyboard.is_pressed('f5'):
            write_on_chat('ㅌ')
        elif keyboard.is_pressed('esc'):
            break
        else:
            time.sleep(0.1)
