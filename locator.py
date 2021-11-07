import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
print(currentMouseX, currentMouseY)
