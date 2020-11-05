import pyautogui, time

msg = input("enter your massage: ")
n = input("how many times?: ")
time.sleep(5)
for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')