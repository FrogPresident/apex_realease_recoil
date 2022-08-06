import win32api
import pyautogui


def main():
    a = 0
    while True:
        if win32api.GetKeyState(20):
            if win32api.GetKeyState(0x02) & 0x8000:
                if win32api.GetKeyState(0x01) & 0x8000:
                    pyautogui.moveRel(0, 20, 0.01)
                    while True:
                        pyautogui.moveRel(30, 30, 0.01)
                        pyautogui.moveRel(-30, -30, 0.01)
                        if win32api.GetKeyState(0x01) & 0x8000 == 0:
                            break


if __name__ == '__main__':
    main()
