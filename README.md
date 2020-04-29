# Open_CV-Template-matching
## A mini Open CV(Template-matching) program which is fun and eye-catchy 

#### While taking a break from my final year college project I had nothing to do as the whole word was in LOCKDOWN because of COVID-19.
#### Then I came across this lame challenge called "[1to50](http://zzzscore.com/1to50/en/ "1to50")" which my cousin sent me.
#### We just had to click 1 to 50 as fast as possible 
#### By hand I could get it in 45 ~ 53 seconds 

### Got bored  so thought of making a program to automate it

####  After 6 ~ 8 hours of digging 
##### AND
#### Trial and error of 2 hours 
#### I came up with this 

```python
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

```
![](https://github.com/ARjUN-ZORO/Open_CV-Template-matching/blob/master/Screenshot%20(68).png)


#### All I'm doing is matching these ![](https://github.com/ARjUN-ZORO/Open_CV-Template-matching/blob/master/nums/4.png) with what is on the screen 
#### Once I get a match I'm asking the program to click at the location which it was found

### There you go Awesome results 

![](https://github.com/ARjUN-ZORO/Open_CV-Template-matching/blob/master/Screenshot%20(66).png)

I apologize for my grammar.
