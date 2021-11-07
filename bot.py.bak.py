import pyautogui
import time
from mss.darwin import MSS as mss
import mss.tools

from PIL import Image

# # 0.20
# while True:
#   start = time.time()
#   print(pyautogui.pixel(64, 174))
#   end = time.time()
#   print(end - start)

# 0.19
# while True:
#     start = time.time()
#     img = pyautogui.screenshot()
#     # img = pyautogui.screenshot('my_screenshot.png', region=(64, 174, 1, 1))
#     print(img.getpixel((0, 0)))
#     end = time.time()
#     print(end - start)

# # 0.14
# while True:
#     start = time.time()
#     with mss() as sct:
#         img = sct.shot()
#     print(img)
#     end = time.time()
#     print(end - start)

# 0.007
# while True:
#     start = time.time()
#     with mss.mss() as sct:
#         # Get information of monitor 2
#         monitor_number = 1
#         mon = sct.monitors[monitor_number]

#         # The screen part to capture
#         monitor = {
#             "top": mon["top"] + 174,  # 100px from the top
#             "left": mon["left"] + 64,  # 100px from the left
#             "width": 1,
#             "height": 1,
#             "mon": monitor_number,
#         }
#         output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)
#         sct_img = sct.grab(monitor)
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         # print(output)
#         im = Image.open('sct-mon1_174x64_1x1.png')
#         pix = im.load()
#         print(pix[0, 0])
#     end = time.time()
#     print(end - start)

# # 0.005
# monitor_number = 1

# while True:
#     start = time.time()
#     with mss.mss() as sct:
#         mon = sct.monitors[monitor_number]

#         # The screen part to capture
#         monitor = {
#             "top": mon["top"] + 174,  # 100px from the top
#             "left": mon["left"] + 64,  # 100px from the left
#             "width": 1,
#             "height": 1,
#             "mon": monitor_number,
#         }
#         output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)
#         sct_img = sct.grab(monitor)
#         img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
#         pix = img.load()
#         print(pix[0, 0])

#     end = time.time()
#     print(end - start)

# 0.004
with mss.mss() as sct:

    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 174,  # 100px from the top
        "left": mon["left"] + 64,  # 100px from the left
        "width": 1,
        "height": 1,
        "mon": monitor_number,
    }

    while True:
        start = time.time()
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        pix = img.load()
        print(pix[0, 0])
        end = time.time()
        print(end - start)
