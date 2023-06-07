from email import message
from logging import exception
from math import e, inf, radians
from platform import release
from sys import float_repr_style
from urllib import request
import pyttsx3
import datetime
from pywhatkit import main
from selenium.webdriver.remote import command
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import os
import subprocess
import ctypes
from wikipedia.wikipedia import search
import winshell
import sys
import pygeoip
import requests
# import GetObject
# import Popen
import instaloader
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import smtplib
import requests
import bs4
from pywhatkit import sendwhatmsg
from tkinter import *
from instabot import Bot
import random



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Assistant: Good Morning")

    elif hour >= 12 and hour < 18:
        print("Assistant: Good Afternoon")

    else:
        print("Assistant: Good Evening")


def Auto_Login(webs, user, Password, email_xpath, password_xpath, login_xpath):

    try:
        option = Options()
        option.add_argument("start-maximized")
        driver = webdriver.Chrome(executable_path="D:\Study Material\programming\python\Javies\chromedriver.exe")

        driver.get(webs)

        time.sleep(5)

        driver.find_element_by_xpath(email_xpath).send_keys(user)
        time.sleep(2)
        driver.find_element_by_xpath(password_xpath).send_keys(Password)
        time.sleep(2)
        driver.find_element_by_xpath(login_xpath).click()

    except Exception as e:
        print(e)


def takeCommand():

    print("Assistant: Listening Sir...")

    try:
        print("user:")
        query = input().lower()
        # print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Can you repeat ?, Sir!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def Msg_Twitter():

    print("Assistant: What should I tweet ?,sir!")

    tweet = takeCommand().lower()

    Auto_Login("https://twitter.com/login", 'youremail@gmail.com', 'password', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input',
               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')

    option = Options()
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(executable_path="D:\Study Material\programming\python\Javies\chromedriver.exe")

    tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    message_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    post_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div/div/span/span'

    time.sleep(4)

    driver.find_element_by_xpath(tweet_xpath).click()
    time.sleep(0.5)
    driver.find_elements_by_xpath(message_xpath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(post_xpath).click()


def run():
    print("Assistant: Do you want to start this program ?")
    while True:
        query = takeCommand()

        if "start" in query:
            print("starting")
            fun()

        elif "exit" in query:
            print("Assistant: Are you really want to close the program")
            order = takeCommand().lower()
            if 'yes' in order:
                print("okay")
                sys.exit()
            elif 'no' in order or 'not' in order:
                print("okay")
                pass


def mimic():
    while True:
        order = takeCommand().lower()
        if 'exit' in order:
            print("Assistant: Okay")
            break
        print(order)


def CLOse(b):

    closSe = {

        ' edge': 'TASKKILL /F /IM msedge.exe',
        ' chrome': 'TASKKILL /F /IM chrome.exe',
        ' notes': 'TASKKILL /F /IM notepad.exe',

    }
    os.system(closSe.get(b))


def OPPRO(query):

    address = {
        "open chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "open whatsapp": "C:\\Users\\suraj shegukar\\AppData\Local\\WhatsApp\\Whatsapp.exe",
        "open notepad": "C:\\windows\\system32\\notepad.exe",
        "open vs code": "C:\\Users\\suraj shegukar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    }
    os.startfile(address.get(query))


def Wtime():

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Assistant: Sir!, the current time is{strTime}")


def Search_wiki():

    print('Assistant: What should i search....')
    command = takeCommand().lower()
    command = command.replace('search', '')
    results = wikipedia.summary(command, sentences=1)
    print(command)
    print("According to wikipedia")
    print(results)


def OPweb(b):

    webb = {
        ' wikipedia': 'https://en.wikipedia.org/wiki/Main_Page',
        ' instagram': 'https://www.instagram.com/',
        ' facebook': 'https://www.facebook.com/',
        ' map': 'https://www.google.com/maps',
        ' google': 'https://www.google.com/',
        ' stackoverflow': 'https://www.stackoverflow.com/'
    }

    webbrowser.open(webb.get(b))


def Show_Note():

    print("Assistant: Showing your notes")
    os.startfile('data.txt')
    file = open('data.txt', 'r')
    print(file.read())
    print(file.read())


def Write_Note():

    print("Assistant: What should I write ?, sir!")
    note = takeCommand().lower()
    file = open('data.txt', 'a')
    print("Assistant: Sir,should i include date and time ?")
    snfm = takeCommand().lower()

    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        file.write("\n")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
        print("Assistant: Done")

    elif 'no' in snfm or 'not' in snfm:
        file.write(note)
        print("Assistant: Done")

    else:
        print("Assistant: can you repeat,sir!")


def CkInsta_Profile():

    try:
        print("Assistant: sir!,please enter the user name")
        name = input("Enter username here:")
        webbrowser.open(f"www.instagrm.com/{name}")
        print("Assistant: Sir here is the profile of the user")
        print("Assistant: Sir would you like to download profile picture of this account")
        condition = takeCommand().lower()

        if "yes" in condition:
            mod = instaloader.Instaloader()
            print("reaname the image sir")
            nam = takeCommand().lower()
            mod.download_profile(name, profile_pic_only=True)
            print('i am done sir, profile picture is saved in our main folder')

        elif 'no' in condition:
            print("okay sir!")

    except Exception as e:
        print(e)


def OPMusic():

    music_dir = 'D:\\song'
    songs = os.listdir(music_dir)
    print("Opening music file")
    print(songs, end="")
    os.startfile(os.path.join(music_dir, songs[random.randint(0, 100)]))


def OSExit():
    print("are you really want to close the program")
    order = takeCommand().lower()
    if 'yes' in order:
        print("okay")
        sys.exit()
    elif 'no' in order or 'not' in order:
        print("okay")
        pass


def Location():

    try:

        r = requests.get('https://get.geojs.io/')
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()['ip']
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        print(geo_data)
        print(geo_data['latitude'])
        print(geo_data['longitude'])
        print(geo_data['city'])
        print(geo_data['region'])
        print(geo_data['country'])
        print(geo_data['timezone'])
        print(geo_data['latitude'])
        print(geo_data['longitude'])
        print(geo_data['city'])
        print(geo_data['region'])
        print(geo_data['country'])
        print("and timezone is")
        print(geo_data['timezone'])

    except Exception as e:
        print(e)
        print(e)
        print("sorry sir!,due to some technical issue i can't find our location")


def SShot():

    img = pyautogui.screenshot()
    print('enter the name of file')
    name = takeCommand()
    # name = input("enter the name of file")
    img.save(name + ".png")
    print("I am done sir!, the screenshot is saved in your main folder")


def OpenFaceBook():

    print("opening Facebook")
    webbrowser.open("facebook.com")


def CPFaceBook():
    print("sir!,please enter the user name")
    name = input("Enter username here:")
    webbrowser.open(f"https://www.facebook.com/public/{name}")
    print("sir here is the profiles of the username that i found")


def fun():
    wishMe()
    print("Assistant: I am tokyo your personal desktop assistant.How can I help you ?")
    while True:

        query = takeCommand().lower()

        if 'tokyo' in query:

            print("yes sir!,tell me how can i help you ?")

# ---------------------------------------------------------------------------wikipedia----------------------------------------------------------------------------------
        elif 'what can you do' in query:

            print('''Assistant: what can i do as follows:
            1.Automated browser
            2.play videos on youtube
            3.can tell you your location
            4.facebook and instagram profile
            5.screenshot
            6.wikipedia
            7.open and write a notes
            8.send and open emails
            9.joke
            10.time and much more things''')

        elif 'wikipedia' in query:

            if 'search on wikipedia' in query:
                Search_wiki()

        elif 'open web' in query:

            try:
                b = query.replace('open web', '')
                print('opening' + b + " sir!")
                OPweb(b)

            except exception as e:
                print(e)

# ---------------------------------------------------------------------------facebook--------------------------------------------------------------------------------------
        elif 'facebook' in query:

            if 'open facebook' in query:
                OpenFaceBook()

            elif 'facebook profile' in query:
                CPFaceBook()
# ---------------------------------------------------------------------------music--------------------------------------------------------------------------------------
        elif 'open music' in query:
            OPMusic()

# ---------------------------------------------------------------------------my computer--------------------------------------------------------------------------------------
        elif 'open' in query:

            try:

                OPPRO(query)

            except exception as e:
                print(e)

        elif 'close' in query:
            b = query.replace('close', '')
            print('Closing' + b + " sir!")
            CLOse(b)

# ------------------------------------------------------------------------------time-------------------------------------------------------------------------------------------
        elif 'time' in query:
            Wtime()
# -----------------------------------------------------------------------------Questions------------------------------------------------------------------------------------

        elif 'your name' in query:
            print("My name is tokyo")

        elif 'about yourself' in query:
            # print("my name is "+ Name +"I am desktop assistant created by suraj and his friends as PBL Activity and I like to talk to people" )
            print("my name is tokyo .I am desktop assistant created by suraj and his friends as PBL Activity and I like to talk to people")

        elif 'hi' in query or 'hello' in query:
            print("hello sir, tell me how can help you")

        elif 'about your creator' in query:
            print("I was created by Suraj. he is studying at Zeal Institue as computer enginerring.Now he is in second year of enginerring and he is very good person with a nice personality")

        elif 'you like' in query:

            if 'which fruit you like' in query:
                print("I really like mangoes")

            elif "which place you like" in query:
                print(
                    "my favurite place is Pune. It's such a beautiful place with a nice people")

            else:
                print("I like to talk to diffrent peoples from diffrent places")

        elif 'who is' in query:
            person = query.replace("who is", "")
            info = wikipedia.summary(person, 1)
            print(info)
            print(info)

        elif 'joke' in query:
            print(pyjokes.get_joke())

        elif 'repeat me' in query:
            print("okay")
            mimic()

        elif 'play' in query:
            song = query.replace('play', '')
            print("playing" + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            text = query.replace('search', '')
            print("searching")
            pywhatkit.search(text)
# ----------------------------------------------------------------------------------powar------------------------------------------------------------------------------------------------------

        # elif "lock window" in query:
        #     print("locking window")
        #     ctypes.windll.user32.lockworkstation()

        # elif "shutdown window" in query:
        #     print("shutdowning window")
        #     subprocess.call('shutdown / p /f')

        # elif "restart window" in query:
        #     print("restarting window")
        #     subprocess.call(["shutdown", "r"])
        #
        # elif "sleep window" in query:
        #     print("slepping window")
        #     subprocess.call('shutdown / h')

# -----------------------------------------------------------------------------notes----------------------------------------------------------------------------------------

        elif 'note' in query:
            if 'show my notes' in query:
                Show_Note()

            elif 'write a note' or 'take a note' in query:
                Write_Note()

            else:
                print("Assistant: Can you repeat,sir!")
# -----------------------------------------------------------------------------exit/stop-------------------------------------------------------------------------------

        elif 'stop' in query:
            print("Assistant: Ok")
            run()

        elif 'exit' in query:
            OSExit()

# ------------------------------------------------------------------------------instagram----------------------------------------------------------------------------------------

        elif 'instagram' in query:

            if 'instagram profile' in query:
                CkInsta_Profile()

            elif 'open instagram' in query:
                print("Assistant: Opening instagram")
                webbrowser.open("https://www.instagram.com/")

            elif 'login to instagram' in query:
                print("Assistant: Do you want login by your account ?")
                cmmd = takeCommand().lower()
                if 'yes' in cmmd:
                    print("Assistant: Login by your account, sir!")
                    Auto_Login("https://www.instagram.com/accounts/login/",'youremail@gmail.com','password',
                               '//*[@id="loginForm"]/div/div[1]/div/label/input', '//*[@id="loginForm"]/div/div[2]/div/label/input', '//*[@id="loginForm"]/div/div[3]')

                else:
                    webbrowser.open("https://www.instagram.com/")


# ---------------------------------------------------------------------------------location----------------------------------------------------------------------------------------
        elif 'my location' in query:
            print("Assistant: Wait sir!,let me check")
            Location()

# ------------------------------------------------------------------------------------screenshot------------------------------------------------------------------------------------------------

        elif 'screenshot' in query:
            print('Assistant: Taking screenshot')
            SShot()
# -------------------------------------------------------------------------------------Gmail--------------------------------------------------------------------------------------------------------

        elif 'gmail' in query:

            if 'open gmail' in query:
                print("Assistant: Opening gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'send gmail' in query:

                try:
                    print("Assistant: Who you wanna send email")
                    person = input("enter the gmail of person")
                    to = person
                    print("Assistant: What should I say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    print("Assistant:Email has been sent!")

                except Exception as e:
                    print(e)
                    print("Assistant: Sorry, I am not able to send this email")

# -----------------------------------------------------------------------------------Twitter---------------------------------------------------------------------------------------

        elif 'twitter' in query:

            if 'open twitter' in query:
                print("Assistant: opening twitter")
                webbrowser.open('https://twitter.com/?lang=en')

            elif 'message on twitter' in query:
                Msg_Twitter()


# -----------------------------------------------------------------------------whatsapp-----------------------------------------------------------------------------------------

        elif 'whatsapp' in query:

            if 'open whatsapp' in query:
                print("Assistant: opening whatsapp")
                webbrowser.open("https://web.whatsapp.com/")

# -----------------------------------------------------------------------------youtube----------------------------------------------------------------------------------

        elif 'youtube' in query:

            if 'open youtube' in query:
                print("Assistant: opening Youtube")
                webbrowser.open("youtube.com")


if __name__ == "__main__":

    # Chatbot()
    wishMe()
    run()
