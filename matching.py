import cv2, pyautogui, time
import  numpy as np
from PIL import ImageGrab

num = 1
def grab():
    full = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,0,540,730))), cv2.COLOR_RGB2BGR)
    return full

def gettemp(n):
    name = 'nums\\'+n+".png"
    temp = cv2.imread(name,0)
    return temp

def match():
    full = grab()
    gray = cv2.cvtColor(full,cv2.COLOR_BGR2GRAY)
    for i in range(1,51):
        if i == 26:
            full = grab()
            gray = cv2.cvtColor(full,cv2.COLOR_BGR2GRAY)
        temp = gettemp(str(i))
        w, h = temp.shape[::-1]
        res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
        threshold = 0.954 # works(0.954) Change at your onw risk  
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(full, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 3)
            print(pt,i)

        pyautogui.click(pt[0],pt[1])
        cv2.imshow('outimg',full)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

match()
