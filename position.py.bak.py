from pynput import mouse
from pynput.mouse import Button, Controller
import time

mouse_pos = Controller()

# define mouse movement function
def on_move(x, y):
    # print('Pointer moved to {0}'.format((x, y)))
    time.sleep(5)
    return False


# function to get position of cart handle, grey area and click area
def get_position():
    # Collect events until released
    print('MOVE MOUSE WHERE CART ICON HANDLE IS in 5s')
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
        cart_handle = mouse_pos.position
        print(cart_handle[0], cart_handle[1])

    # Collect events until released
    print('MOVE MOUSE WHERE THE GREY AREA AROUND THE CART IS in 5s')
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
        grey_area = mouse_pos.position
        print(grey_area[0], grey_area[1])

    # Collect events until released
    print('MOVE MOUSE WHERE TO CLICK TO BUY in 5s')
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
        buy_click = mouse_pos.position
        print(buy_click[0], buy_click[1])

    return [cart_handle, grey_area, buy_click]
