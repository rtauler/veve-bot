from pynput import mouse
from pynput.mouse import Button, Controller
import time

mouse_pos = Controller()

# define mouse movement function
def on_move(x, y):
    # print('Pointer moved to {0}'.format((x, y)))
    time.sleep(2)
    return False


# function to get position of cart handle, grey area and click area
def get_position():
    # Collect events until released
    print('MOVE MOUSE to SELECTED PIXEL in 2s')
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
        selected_pixel = mouse_pos.position
        print(selected_pixel[0], selected_pixel[1])

    return selected_pixel
