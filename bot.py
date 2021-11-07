import pyautogui
from pynput.mouse import Button, Controller
import time
from mss.darwin import MSS as mss
import mss.tools

from PIL import Image

from position import get_position

mouse = Controller()

# get positions (x,y)
selected_pixel = get_position()

# 0.004
with mss.mss() as sct:
    # define monitor to use
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    selected_pixel_area = {
        "top": mon["top"] + selected_pixel[1],
        "left": mon["left"] + selected_pixel[0],
        "width": 1,
        "height": 1,
        "mon": monitor_number,
    }


def get_pixel_color():
    sct_img = sct.grab(selected_pixel_area)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    sct_img_pixel_color = img.load()
    selected_pixel_color = sct_img_pixel_color[0, 0]
    # print(selected_pixel_color)
    return selected_pixel_color


current_pixel_color = get_pixel_color()
# infinite loop till action (click) is called

# prepare mouse for clicking
print('putting mouse in clicking position in 3s')
# time.sleep(3)
pyautogui.moveTo(selected_pixel[0], selected_pixel[1])

while True:
    start = time.time()
    selected_pixel_color = get_pixel_color()
    if not selected_pixel_color == current_pixel_color:
        # pyautogui.click(selected_pixel[0], selected_pixel[1])
        mouse.click(Button.left)
        print('clicked! on', selected_pixel[0], selected_pixel[1])
        end = time.time()
        print(end - start)
        break
    else:
        end = time.time()
        print('false', selected_pixel_color, end - start)
