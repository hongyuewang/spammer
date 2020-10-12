import pyautogui, time
time.sleep(5)

f = open("spam.txt", 'r', errors="ignore")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')


