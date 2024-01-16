import win32api, win32con
import time
import keyboard

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# Reemplaza las coordenadas (x, y) con las que desees

cycles = 7
while cycles < 10 or keyboard.is_pressed('p'):
    time.sleep(2)
    click(30, 40)
    time.sleep(2)
    click(55, 40)
    if keyboard.is_pressed('p'):
        print('Se presionó [p]arar!')
        break
    print(cycles)
    cycles += 1
if cycles == 10:
    print(f"El ciclo terminó por el numero limite: ", {cycles})

'''
t = 0
while True:
    time.sleep(1)
    print(t)
    t += 1
    if keyboard.is_pressed('p'):
        print('Se presionó [p]arar!')
        break
'''