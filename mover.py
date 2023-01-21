import pyautogui
import datetime
import time
import random


def main():
    print(pyautogui.size())


pyautogui.FAILSAFE


localtime = time.localtime()
formatted_localtime = time.strftime("%Y %m %d %H %M %S", localtime)

for alkalom in range(360):
    pyautogui.press("shift")
    x = random.randint(200, 500)
    y = random.randint(200, 500)
    pyautogui.moveTo(x, y)

    localtime = time.localtime()
    formatted_localtime = time.strftime("%Y %m %d %H %M %S", localtime)

    print(f"Moved at {str(formatted_localtime)} to {x=} {y=}.")
    print("Movement made at {}".format(datetime.datetime.now().time()))

    time.sleep(10)

print(f"Exited at {str(formatted_localtime)}")


if __name__ == '__main__':
    main()
