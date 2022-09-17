# This is a sample Python script.
# import pymouse
# from concurrent.futures import thread
# from os import name
import pickle
import sys
import webbrowser
# import wx
from threading import Timer
# import tkinter
# import timer
import threading
import pyautogui
#import fbase
import numpy as np
# from pynput import mouse
# from PIL import ImageGrab
# from PIL import Image
# from pynput.mouse import Controller
# from pynput.mouse import  Button
# from selenium import selenium
# import pytesseract
# import pytesseract
# import cv2
# import scrapy

from firebase import firebase

import time
import tkinter as tk
# from selenium.webdriver.chrome.service import Service
# import selenium
# from webdriver_manager.chrome import ChromeDriverManager
# import re
from firebase.firebase import FirebaseApplication
from pywin.mfc import thread
from selenium.webdriver.chrome.options import Options

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import traceback
import firebase

global error_link
global temp_link
global driver
global button
global close


def configurht():
    print("congiiiiigggg")
    file = open("arr", "rb")
    kf = np.load(file, allow_pickle=True)
    m = list(kf)
    print(m)
    file.close()
    i = 1
    k = 1
    while (k < m[0] + 1):
        time.sleep(m[i])
        pyautogui.click(x=m[i + 1][0], y=m[i + 1][1])
        i = i + 2
        k = k + 1


def connect(lis):
    global acces
    global error_link
    global giveme_somtime
    acces = 1
    print("before splitting ")

    try:
        print(lis + "  available")
        splited_text = lis.split()
    except:

        print("text not found")
        traceback.print_exc()
        # t = Timer(60, sel)
        # t.start()
    try:

        for i in splited_text:
            if ("https://meet.google.com/" in i):
                if temp_link == i:
                    print("invalid link")
                    giveme_somtime = 1
                    t = Timer(60, sel)
                    t.start()
                    break
                else:
                    if (giveme_somtime == 1):
                        giveme_somtime = 0
                        time.sleep(10)

                    print(temp_link + ' temp link')

                    print(i + ' orginal link')
                    print("connected")
                    error_link = i
                    webbrowser.open_new_tab(i)
                    t = Timer(60 * 2, sel)
                    t.start()

                    # time.sleep(8)
                    # mouse = Controller()
                    # print(mouse.position)
                    print(pyautogui.position())
                    time.sleep(4)
                    configurht()
                    # mouse.position = (902, 503)
                    # pyautogui.click(1313, 150)

                    # mouse.press(Button.left)

                    # mouse.release(Button.left)
                    # time.sleep(3)
                    # print(mouse.position)
                    # mouse.position = (1056, 460)
                    # pyautogui.click(1056, 460)

                    # mouse.press(Button.left)
                    # mouse.release(Button.left)
                    break


    except:
        print()
        print("in second loop connect failure")
        # traceback.print_exc()
        t = Timer(15, sel)
        t.start()


def textextarct(text):
    a = text
    print(text)
    print(a.split('\n'))
    text_split = a.split('\n')
    # print(a.split('\n')[54].split())
    # print(a.startwith('http'))
    k = 0
    init = 0
    userlink = [10]

    for i in text_split:
        k = k + 1
        if ("https://meet.google.com/" in i):
            # userlink[k] = i
            print(i)
            userlink = i

    # print(userlink)
    connect(userlink)


def sel():
    global acces
    global driver
    global temp_link
    temp_link = error_link
    try:
        search = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div')
        # print(search.find_element_by_class_name(classnames='ZKn2B'))
        # print(search.find_element_by_class_name(classnames='ZKn2B').text)

    except:
        time.sleep(3)
        sel()

        # driver.find_element_by_css_selector('div')
    try:
        search.click()
    except:
        print('ss')

    if acces == 1:
        acces = 0
        time.sleep(2)
        search1 = driver.find_element_by_xpath('//*[@id="main"]/div[3]')
        classnames = search1.find_element_by_tag_name('div')
        # print(classnames.text)
        print(classnames.get_attribute('class'))
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        textextarct(classnames.text)
        # thread.start_new_thread(textextarct, (classnames.text,))
        # thread.exit()
        time.sleep(1000)

        print('cccc')


# driver = webdriver.Chrome('chromedriver.exe', )
# driver.get('https://web.whatsapp.com')  # Already authenticated
#  time.sleep(30)

# driver = webdriver.Chrome("C://Users//JUNAID B S//Downloads//chromedriver_win32.exe")

# time.sleep(10)


def show():
    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")


#  Controller.click(mouse[0],mouse[1])
# Press the green button in the gutter to run the script.


def starter(a):
    global acces
    acces = 1
    global button
    global driver
    global temp_link
    global error_link

    closebut.place(x=100, y=100)
    # open_whatsapp('PyCharm')
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    # service = Service('C:\\Users\\JUNAID B S\\Downloads\\chromedriver_win32\\chromedriver.exe')
    # service.start()
    # driver = webdriver.Remote(service.service_url)
    # driver.get('https://web.whatsapp.com/')
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    temp_link = "https://meet.google.com/vuy-mkiw-epk?hs=151"
    error_link = temp_link

    sel()


def closebtton(f):
    global driver
    print()
    global closebut
    messages = tk.Label(window,text='try  after a while')
    messages1 = tk.Label(window,text='closing....')

    try:
        messages1.place(x=100, y=80)
        driver.close()
        messages.place_forget()
        messages1.place_forget()
        closebut.place_forget()

        button.place(x=100, y=100)
    except:
        messages1.place_forget()

        print("do it after somtime")
        messages.place(x=100, y=80)


def closer(s):
    x = threading.Thread(target=closebtton, args=('',))
    x.start()


def opensel(k):
    button.place_forget()
    closebut.place(x=100, y=100)
    x = threading.Thread(target=starter, args=('',))
    x.start()


def configur_click(a):
    global click_acces
    global timeval
    global timerlab
    global window1
    global win1but
    window2 = tk.Tk()
    window3 = tk.Tk()
    window2.title('googlemeat_cheater')
    window2.geometry("200x100+10+20")
    window3.title('googlemeat_cheater')
    window3.geometry("200x100+10+20")
    # window3.withdraw()
    smpl = tk.StringVar(window2, "loading")
    # smpl.set("poda")
    smpl1 = tk.StringVar(window3, "loading")
    smpl1.set("succesfully")
    succesful = tk.Label(window3, textvariable=smpl1)
    timerla = tk.Label(window2, textvariable=smpl)
    timerla.place(x=20, y=40)
    succesful.place(x=20, y=40)
    # window.deiconify()
    try:
        file = open("arr", "rb")
        kf = np.load(file, allow_pickle=True)
        m = list(kf)
        file.close()

    except:
        file = open("arr", "wb")
        # np.save(file, arry)
        file.close()
        m = [0]
        print()
    if (m[0] < 6):

        countdown = 6
        for count in reversed(range(1, countdown + 1)):
            time.sleep(1)
            print(count)
            smpl.set("capturing.. in" + str(count))
            window2.update()

        print('action!')

        tmppos = pyautogui.position()
        list.append(m, timeval)
        list.append(m, tmppos)

        m[0] = m[0] + 1

        arry = np.array(m, list)

        # np.append(arry,"dddd")

        file = open("arr", "wb")
        np.save(file, arry)
        file.close()
        file = open("arr", "rb")
        smp = np.load(file, allow_pickle=True)
        print(smp)

        # print(np.load(file,allow_pickle=True))
        # print(arry[2])
        # m = [10]

        # list.append(m,[2,0])
        # list.index(m,1)
        print(m)
        smpl1.set(str(m[0]) + "th click succesfully captured")
        # m[1]=[2,3]
        # print(m)
        # print(m[1][0])
        # m[3]=[4,5]
        with open("file.txt", 'w') as output:

            output.write(str(m))
        with open("file.txt", 'r') as output:

            k = output.read()
            # f=list(int(k))
        print(k[0])

        window3.deiconify()
        window3.update()
        time.sleep(3)

        # threading.main_thread().run()
        # threadin('')
        click_acces = 0
        sys.exit()
    else:
        smpl1.set("Exeed the limit 6 click available")
        window3.update()
        window3.deiconify()

        time.sleep(1)
        click_acces = 0


def reset(a):
    print("kkk")
    if (click_acces != 1):
        arry = np.array([0], list)

        # np.append(arry,"dddd")

        file = open("arr", "wb")
        np.save(file, arry)
        file.close()
        L2.place(x=109, y=80)
        # time.sleep(1)
        # L2.place_forget()


def threadin(a):
    print('started')
    # sys.exit()
    global smpl
    global click_acces

    print(click_acces)
    if (click_acces != 1):
        click_acces = 1

        print("in if")
        print(click_acces)

        win1but.place(x=94, y=140)
        global timeval
        #
        j = 0
        try:
            tem1 = int(inputbox.get())
            print(tem1)
        except:
            smpl.set("Enter loading TIME")
            j = 1
            timerlab.place(x=110, y=60)
            click_acces = 0

        if (inputbox.get() != "" and tem1 < 5 and tem1 != 0):
            print(inputbox.get())
            timerlab.place_forget()
            # win1but.place_forget()
            timeval = tem1

            x = threading.Thread(target=configur_click, args=('',))
            x.start()
            # win1but.place(x=94, y=140)





        else:
            if (j != 1):
                smpl.set("number must be less than 6 seconds")
                timerlab.place(x=50, y=60)
                print("empty")
                click_acces = 0

                j = 0


def configure(a):
    #print("ddddddd")
    window.withdraw()
    window1.deiconify()
    # button = tk.Button(window, text="     START     ", fg='green', )


def ready():
    global button, closebut, window, window1, win1but, smpl, timerlab, inputbox,L2,L1
    window = tk.Tk()
    window.title('googlemeat_cheater')
    window1 = tk.Tk()
    window1.title('googlemeat_cheater')
    window1.geometry("300x200+10+20")
    window1.withdraw()
    win1but = tk.Button(window1, text="     CAPTURE CLICK     ", fg='green', )
    # win1but1 = tk.Button(window1, text="      ADD  ", fg='green', )
    win1but.place(x=94, y=140)
    # win1but1.place(x=94, y=140)
    L1 = tk.Label(window1, text="TIME DELAY")
    numberc = tk.StringVar(window1, "loading")

    numberc.set("ADD YOUR CLICK")
    nclick = tk.Label(window1, textvariable=numberc)
    nclick.place(x=109, y=20)
    inputbox1 = tk.Entry(window1, bd=5)
    # inputbox1.place(x=100, y=50)
    L2 = tk.Label(window1, text="Reset succesfully")
    # L2.place(x=109, y=80)
    click_change = tk.Button(window1, text="     reset     ", fg='green', height=1, width=5)
    click_change.bind('<Button-1>', reset)
    click_change.place(x=130, y=170)

    L1.place(x=30, y=100)
    inputbox = tk.Entry(window1, bd=5)
    inputbox.place(x=100, y=100)
    win1but.bind('<Button-1>', threadin)
    # win1but1.bind('<Button-1>', configur_click)
    button = tk.Button(window, text="     START     ", fg='green', )
    confiq = tk.Button(window, text="    configure     ", fg='green', )
    closebut = tk.Button(window, text="     STOP     ", fg='red', )
    closebut.bind('<Button-1>', closer)
    smpl = tk.StringVar(window1, "loading")
    smpl.set("poda")
    timerlab = tk.Label(window1, textvariable=smpl)
    timerlab.place(x=100, y=40)
    timerlab.place_forget()
    button.bind('<Button-1>', opensel)
    button.place(x=100, y=70)
    confiq.place(x=94, y=140)
    confiq.bind('<Button-1>', configure)
    # webbrowser.open_new_tab("www.google.com")

    window.geometry("300x200+10+20")
    window.mainloop()
    window1.mainloop()


def key_validation(a):
    #validwindow.withdraw()
    #ready()
    global ischeckking
    if (ischeckking == 1):
        try:
            ischeckking=0

            validdm.set(" Checking...")

            flag = 0
            out = firebase.get(name='valid', url='https://ey-auto-2017a.firebaseio.com/')
            validkeys = list(out.values())
            #print(validkeys)
            for keys in validkeys:

                if (keys == int(validinputbox.get())):
                    k = 0
                    print("succesfully activated")
                    #print(str(keys)[0])
                    join = ''

                    for i in str(keys):
                        #print(i)
                        k = k + 1
                        join = join + i
                        if (k == 4):
                            break
                    tjoin = int(join)
                    #print(tjoin)
                    firebase.delete(name=join, url='https://ey-auto-2017a.firebaseio.com/valid')
                    flag = 1
                    file = open('temp', 'w')
                    file.write('1#2#4@193')
                    file.close()
                    validdm.set(" Activated Succesfully")
                    time.sleep(2)
                    validwindow.withdraw()
                    ready()

                    break
                    # ready()
                else:
                    print(" failed")
                    ischeckking = 1

            if (flag == 0):
                validdm.set("Wrong Key ")
                ischeckking = 1




        except:
            validdm.set("Connection Error")


def stthread(a):
    try:
        if (validinputbox.get() != '' and len(validinputbox.get()) == 6):
            x = threading.Thread(target=key_validation, args=('',))
            x.start()

        else:
            #print("enter somethig")
            validdm.set("Key Must Be 6 Digits ")

    except:
        #print("wrong value")
        validdm.set("Wrong Licens Key")


if __name__ == '__main__':
    # mous = Controller()
    # print(mous.position)
    # mous.position = (902, 503)

    # mous.press(Button.left)

    # mous.release(Button.left)
    # starter('')
    # tkinter.Button
    global inputbox, L2, button, inputbox, window, button, closebut, window, window1, win1but, smpl, timerlab
    global ischeckking
    ischeckking=1
    temp_keyw=''
    config = {
        "apiKey": "AIzaSyBa_41YmWBXOvxDdx_ckYAX3gCr5740xnI",
        "authDomain": "ey-auto-2017a.firebaseapp.com",
        "databaseURL": "https://ey-auto-2017a.firebaseio.com",
        "projectId": "ey-auto-2017a",
        "storageBucket": "ey-auto-2017a.appspot.com",
        "messagingSenderId": "189212200310",
        "appId": "1:189212200310:web:3f76ae2885f9ef9d53be57",
        "measurementId": "G-P8HBS7MQW8"
    }
    try:
        file = open('temp', 'r')
        temp_keyw=file.read()
        #print(temp_keyw)
        file.close()
    except:
        print("for key contact kadakollam@gmail.com")


    # firebase = pyrebase.initialize_app(config)
    # firebase = firebase(config).database()
    firebase = FirebaseApplication('https://ey-auto-2017a.firebaseio.com/', None)
    data = {'Name': 'John Doe',
            'RollNo': 3,
            'Percentage': 70.02
            }
    # print(firebase.path)
    # print(firebase.database_url)
    # firebase.push(data)
    # fireout=firebase.get()
    # print(fireout)
    # firebase.put(data=data,name='valid',url='https://ey-auto-2017a.firebaseio.com/')
    # key_validation('')

    # result = firebase.post('ey-auto-2017a/', data)
    # print(result)
    # orginal code
    click_acces = 0
    timeval = 0
    acces = 1
    giveme_somtime = 0
    #ready()
    # t.show()
if(temp_keyw=='1#2#4@193'):
    ready()

else:
    validwindow = tk.Tk()
    validwindow.title('googlemeat_cheater')
    validwindow.geometry("300x200+10+20")
    validbutton = tk.Button(validwindow, text="     VALIDATE     ", fg='green', )
    validbutton.bind('<Button-1>', stthread)
    validbutton.place(x=136, y=100)
    validinputbox = tk.Entry(validwindow, bd=5)
    validinputbox.place(x=100, y=60)
    validL1 = tk.Label(validwindow, text="License Key")
    validL1.place(x=30, y=60)
    validdm = tk.StringVar(validwindow, "loading")
    validdm.set("")

    valid_signal = tk.Label(validwindow, textvariabl=validdm)
    valid_signal.place(x=110, y=150)

    validwindow.mainloop(0)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
