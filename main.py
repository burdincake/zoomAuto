import pyautogui
import schedule
import time
import os
from selenium import webdriver
from selenium import *
import pathlib
from win32com.client import Dispatch

a11 = '''
####### ####### ####### #     #    ### #     # 
     #  #     # #     # ##   ##     #  ##    # 
    #   #     # #     # # # # #     #  # #   # 
   #    #     # #     # #  #  #     #  #  #  # 
  #     #     # #     # #     #     #  #   # # 
 #      #     # #     # #     #     #  #    ## 
####### ####### ####### #     #    ### #     #
MADE BY: KWON, JUNESEOK :)
'''
print(a11)

weekX = "A"
def setup():
    baba = open("schedule.txt", "w+")
    baba.close()
    print("Hello user!\n welcome to ZoomAuto :)")
    print("I will tell you what to do each step.\nThis only takes less than 5 minutes\nyou would only need to do this once")
    webUrl = "https://naver.com/"
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("Press Access Allow if popup pops up")
    a = str(pathlib.Path().absolute())
    driver = webdriver.Chrome(executable_path=a + "/chromedriver.exe")
    driver.get(webUrl)
    driver.quit()
    f = open("schedule.txt", "a")
    #name
    print("Enter your name: ", end="")
    name = input()
    f.write(name)
    #A
    print("Enter Zoom Code for block A (Type x for empty class) :",end="")
    A = input()
    f.write("\n"+A)
    #A*
    print("Enter Zoom Code for block A* (Type x for empty class): ", end="")
    As = input()
    f.write("\n"+As)
    #B
    print("Enter Zoom Code for block B (Type x for empty class): ", end="")
    B = input()
    f.write("\n"+B)
    #Bs
    print("Enter Zoom Code for block B*: ", end="")
    Bs = input()
    f.write("\n"+Bs)
    #C
    print("Enter Zoom Code for block C: ", end="")
    C = input()
    f.write("\n"+C)
    #C*
    print("Enter Zoom Code for block C*: ", end="")
    Cs = input()
    f.write("\n"+Cs)
    #D
    print("Enter Zoom Code for block D: ", end="")
    D = input()
    f.write("\n"+D)
    #D*
    print("Enter Zoom Code for block D*: ", end="")
    Ds = input()
    f.write("\n"+Ds)
    #E
    print("Enter Zoom Code for block E: ",end="")
    E = input()
    f.write("\n"+E)
    #E*
    print("Enter Zoom Code for block E*: ",end="")
    Es = input()
    f.write("\n"+Es)
    #F
    print("Enter Zoom Code for block F: ",end="")
    F = input()
    f.write("\n"+F)
    #F*
    print("Enter Zoom Code for block F*: ",end="")
    Fs = input()
    f.write("\n"+Fs)
    #Homeroom
    print("Enter Zoom Code for Homeroom: ", end="")
    Hr = input()
    f.write("\n"+Hr)
    f.close()
    print("setup complete! rerun program :)",end = "")
    while (1==1):
        avsdfdas = input()

def enterZoomMac(code):
    if(code != "x"):
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak("Program started! Do not touch your computer until finished!")
        print("LOG: Program started! Do not touch your computer until finished!")
        time.sleep(2)
        code = code.replace(" ","")
        webUrl = "https://zoom.us/j/"+code+"#success"
        a = str(pathlib.Path().absolute())
        driver = webdriver.Chrome(executable_path=a+"/chromedriver.exe")
        driver.get(webUrl)
        time.sleep(5)
        button = driver.find_element_by_class_name('_3Gj8x8oc')
        button.click()
        time.sleep(7)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('space')
        time.sleep(0.2)
        driver.close()
        time.sleep(5)
        pyautogui.typewrite('12345',interval=0.02)
        time.sleep(0.4)
        pyautogui.press('enter')
        driver.quit()
        speak.Speak("Program finished! you may touch your computer. Also, Do not turn me off unless this is your last class")
        print("Log: Program finished! you may touch your computer. Also, Do not turn me off unless this is your last class")
    else:
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak("It is self study period. enjoy")
        print("Log: It is self study period. enjoy :)")

def enterZoomMac1(code):
    print(code)
    print("run!")
def Main():
    if not os.path.isfile('schedule.txt'):
        baba = open("schedule.txt","w+")
        baba.close()
    a = open("schedule.txt", "r")
    name = a.readline();
    a.close()
    if(name==""):
        setup()
    print("Is this week A or B (A/B): ",end="")
    inputweekAB = input()
    if(inputweekAB == "A" or inputweekAB == "a"):
        weekX = "A"
    elif (inputweekAB == "B" or inputweekAB == "b"):
        weekX = "B"
    else:
        Main()
    print("Hello "+name,end="")
    print("If this is not your name, enter \"x\". If correct, enter \"start\": ",end="")
    input1 = input()
    if(input1 == "x" or input1 == "\"x\""):
        print("Reset Initiated!")
        setup()
    elif(input1 == "start" or input1 == "\"start\""):
        start()
def start():
    print("\n\n\n\n\n\n\n\n\nI will turn on your zoom Automatically. I will keep time for you :)\n ALSO, DO NOT CLOSE THIS WINDOW! (YOU MAY SHRINK IT)")
    array = []
    with open('schedule.txt') as f:
        for f1 in f:
            array.append(f1[0:len(f1)-1])
    name = str(array[0])
    a = str(array[1])
    sa = str(array[2])
    b = str(array[3])
    sb = str(array[4])
    c = str(array[5])
    sc = str(array[6])
    d = str(array[7])
    sd = str(array[8])
    e = str(array[9])
    se = str(array[10])
    f = str(array[11])
    sf = str(array[12])
    hr = str(array[13])
    if(weekX == "A" or weekX == "a"):
        schedule.every().monday.at("08:27").do(enterZoomMac, hr)
        schedule.every().monday.at("08:52").do(enterZoomMac, b)
        schedule.every().monday.at("09:47").do(enterZoomMac, c)
        schedule.every().monday.at("10:42").do(enterZoomMac, a)
        schedule.every().monday.at("11:37").do(enterZoomMac, e)
        schedule.every().monday.at("13:22").do(enterZoomMac, f)
        schedule.every().monday.at("14:17").do(enterZoomMac, d)
        schedule.every().monday.at("15:12").do(enterZoomMac, hr)
    if(weekX == "B" or weekX == "b"):
        schedule.every().monday.at("8:27").do(enterZoomMac, hr)
        schedule.every().monday.at("8:52").do(enterZoomMac, sb)
        schedule.every().monday.at("9:47").do(enterZoomMac, sc)
        schedule.every().monday.at("10:42").do(enterZoomMac, sa)
        schedule.every().monday.at("11:37").do(enterZoomMac, se)
        schedule.every().monday.at("13:22").do(enterZoomMac, sf)
        schedule.every().monday.at("14:17").do(enterZoomMac, sd)
        schedule.every().monday.at("15:12").do(enterZoomMac, hr)
    #tuesday
    schedule.every().tuesday.at("08:27").do(enterZoomMac, hr)
    schedule.every().tuesday.at("08:52").do(enterZoomMac, se) #52!!!!!!!
    schedule.every().tuesday.at("09:47").do(enterZoomMac, sf)
    schedule.every().tuesday.at("10:42").do(enterZoomMac, sd)
    schedule.every().tuesday.at("11:37").do(enterZoomMac, sa)
    schedule.every().tuesday.at("13:22").do(enterZoomMac, sb)
    schedule.every().tuesday.at("14:17").do(enterZoomMac, sc)

    #wednesday
    schedule.every().wednesday.at("08:27").do(enterZoomMac, hr)
    schedule.every().wednesday.at("08:52").do(enterZoomMac, b)
    schedule.every().wednesday.at("09:47").do(enterZoomMac, c)
    schedule.every().wednesday.at("10:42").do(enterZoomMac, a)
    schedule.every().wednesday.at("11:37").do(enterZoomMac, e)
    schedule.every().wednesday.at("13:22").do(enterZoomMac, f)
    schedule.every().wednesday.at("14:17").do(enterZoomMac, d)
    schedule.every().wednesday.at("15:12").do(enterZoomMac, hr)




    #thursday
    schedule.every().thursday.at("08:27").do(enterZoomMac, hr)
    schedule.every().thursday.at("08:52").do(enterZoomMac, se)
    schedule.every().thursday.at("09:47").do(enterZoomMac, sf)
    schedule.every().thursday.at("10:42").do(enterZoomMac, sd)
    schedule.every().thursday.at("11:37").do(enterZoomMac, sa)
    schedule.every().thursday.at("13:22").do(enterZoomMac, sb)
    schedule.every().thursday.at("14:17").do(enterZoomMac, sc)
    #friday
    schedule.every().friday.at("08:27").do(enterZoomMac, hr)
    schedule.every().friday.at("08:52").do(enterZoomMac, b)
    schedule.every().friday.at("09:47").do(enterZoomMac, c)
    schedule.every().friday.at("10:42").do(enterZoomMac, a)
    schedule.every().friday.at("11:37").do(enterZoomMac, e)
    schedule.every().friday.at("13:22").do(enterZoomMac, f)
    schedule.every().friday.at("14:17").do(enterZoomMac, d)


if __name__ == "__main__" :
    Main()


while True:
    schedule.run_pending()
    time.sleep(1)
