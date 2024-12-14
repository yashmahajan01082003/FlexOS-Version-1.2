import glob
import math
import os
import subprocess
import threading
import time
import webbrowser

import os
from time import sleep
import cv2
import pygame
import render as render
from langdetect import detect
from matplotlib import pyplot as plt
import numpy as np

import comtypes
import cvzone
import pythoncom
import pyttsx3 as pyttsx3
import wmi
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from PIL import ImageGrab
from django.conf import settings
from django.http import HttpResponse, request
from django.shortcuts import render
from pathlib import Path

from .HandTrackingModule import handDetector
from .models import IconsForDesktop, BottomSideIcons, HandGest, Person
import psutil
import cv2
import pyautogui
import mediapipe as mp
import ctypes

import cv2
import pywhatkit
from bs4 import BeautifulSoup
from django.shortcuts import render
import datetime
import smtplib
import subprocess
import os
import json
from django.http import HttpResponse
import random
import time
import webbrowser
from random import choice
import PyPDF2
import psutil
import pyautogui
import pyjokes
import requests
import pyttsx3
import speech_recognition as sr
import wikipedia
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.utils import AudioUtilities
from requests import get
import pywhatkit as kit
import sys
from translate import Translator
from django.http import JsonResponse
from ctypes import cast , POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities , IAudioSessionControl


def index(request):
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context={
        'Icon' : Icons,
        'folders' : folders,
        'BIcons' : BIcons,
        'perc' : percent,
        'status' : status,
        'deskp': desktop_path,
    }
    return render(request,'home/templates/index.html',context)

def openDesktopD(request,fName):
    # Get the path to the desktop
    desktop_path = Path.home() / 'Desktop'

    # Construct the path to the fName directory on the desktop
    fName_path = desktop_path / fName

    # List directories within the fName directory
    directories = [directory for directory in os.listdir(fName_path) if os.path.isdir(fName_path / directory)]

    # Print the list of directories
    for directory in directories:
        print(directory)

    folders = directories

    context={
        'folders':folders,
        'root' : 'Desktop',
        'parent1' : fName,
    }
    return render(request,'home/templates/desktopfolderinternal.html',context)

def BSIcons(request,fName):
    Bicons = BottomSideIcons.objects.all()
    if fName == Bicons[0].name:
        webbrowser.open('www.google.com')

    if fName == Bicons[1].name:
        calculator_process = subprocess.Popen('calc.exe')

    if fName == Bicons[2].name:
        subprocess.Popen('explorer')

    if fName == Bicons[3].name:
        camera_app_url = 'microsoft.windows.camera:'  # Windows Camera app URL
        webbrowser.open(camera_app_url)

    if fName == Bicons[4].name:
        subprocess.Popen('cmd.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)

    if fName == Bicons[5].name:
        os.startfile("outlookcal:")

    if fName == Bicons[6].name:
        subprocess.Popen('explorer.exe ms-settings:')

    if fName == Bicons[7].name:
        subprocess.Popen(['notepad.exe'])

    if fName == Bicons[8].name:
        subprocess.Popen(['control'])

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp' : desktop_path,
    }

    return render(request, 'home/templates/index.html', context)

def openParti(request):
    partitions = psutil.disk_partitions(all=True)
    folders=[]
    for partition in partitions:
        drive_letter = partition.device
        folders.append(drive_letter)
        print(drive_letter)

    context={
        'folders': folders,
    }
    return render(request,'home/templates/partition.html',context)

def get_directories_in_drive(fName):
    c_drive_path = fName
    directories = [name for name in os.listdir(c_drive_path) if os.path.isdir(os.path.join(c_drive_path, name))]
    return directories

def openPartiSpec(request,fName):
    partitions = psutil.disk_partitions(all=True)
    folders=[]
    directory_list=[]
    for partition in partitions:
        drive_letter = partition.device
        folders.append(drive_letter)

    if fName == folders[0]:
        directory_list = get_directories_in_drive(fName)


    if fName == folders[1]:
        directory_list = get_directories_in_drive(fName)


    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context={
        'folders': directory_list,
        'root' : fName,
        'perc': percent,
        'status': status,
    }
    return render(request,'home/templates/insidepart.html',context)


def openPartiSpec2(request, fName0, fName1):
    partitions = psutil.disk_partitions(all=True)
    folders = [partition.device for partition in partitions]
    fName0 = fName0.replace('/', '\\')  # Replace forward slash with backslash
    fName1 = fName1.replace('/', '\\') if fName1 else ''  # Replace forward slash with backslash if fName1 is not empty

    path = os.path.join(fName0, fName1)
    is_file = os.path.isfile(path)

    if is_file:
        # Handle file case
        webbrowser.open(path)
        path1 = os.path.join(fName0)
        directory_list = []
        file_list = []
        if os.path.exists(path1):
            for item in os.listdir(path1):
                item_path = os.path.join(path1, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)

        root = os.path.join(fName0)

        context = {
            'folders': directory_list,
            'files': file_list,
            'root': root,
            'parent1': fName1,
        }
        return render(request, 'home/templates/insidepart.html', context)

    directory_list = []
    file_list = []
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                directory_list.append(item)
            else:
                file_list.append(item)

    root = os.path.join(fName0, fName1)

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context = {
        'folders': directory_list,
        'files': file_list,
        'root': root,
        'parent1': fName1,
        'perc' : percent,
        'status' : status,
    }
    return render(request, 'home/templates/insidepart.html', context)

def newD(request):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    fName = request.GET.get('name')
    flag = request.GET.get('flag')
    new_directory = os.path.join(desktop_path, fName)
    print(flag)
    # Create the directory if it doesn't exist
    if flag == '2':
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
            print("Directory created successfully.")
        else:
            print("Directory already exists.")

    if flag=='3':
        if not os.path.exists(new_directory):
            with open(new_directory, 'w') as file:
                file.write('')  # You can write content to the file if needed
            print("File created successfully.")
        else:
            print("File already exists.")

    if flag=='4':
        subprocess.call(["powershell.exe"])

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context={
        'Icon' : Icons,
        'folders' : folders,
        'BIcons' : BIcons,
        'perc' : percent,
        'status' : status,
        'deskp': desktop_path,
    }
    return render(request,'home/templates/index.html',context)


def newD2(request, fName0):
    fName = request.GET.get('name')
    flag = request.GET.get('flag')
    print(flag)
    partitions = psutil.disk_partitions(all=True)
    folders = [partition.device for partition in partitions]
    fName0 = fName0.replace('/', '\\')  # Replace forward slash with backslash

    specified_path = fName0  # Specify the desired path here

    path = os.path.join(specified_path, fName)
    is_file = os.path.isfile(path)

    directory_list = []
    file_list = []

    if is_file:
        # Handle file case
        webbrowser.open(path)
        if os.path.exists(specified_path):
            for item in os.listdir(specified_path):
                item_path = os.path.join(specified_path, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)
    else:
        # Handle directory case
        if os.path.exists(fName0):
            for item in os.listdir(fName0):
                item_path = os.path.join(fName0, item)
                if os.path.isdir(item_path):
                    directory_list.append(item)
                else:
                    file_list.append(item)

    root = specified_path

    # Create the directory if it doesn't exist
    if flag=='2':
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory created successfully.")
        else:
            print("Directory already exists.")

    if flag=='3':
        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write('')  # You can write content to the file if needed
            print("File created successfully.")
        else:
            print("File already exists.")


    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    context = {
        'folders': directory_list,
        'files': file_list,
        'root': root,
        'perc': percent,
        'status': status,
    }
    return render(request, 'home/templates/insidepart.html', context)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
virtual_mouse_thread = None
stop_virtual_mouse = threading.Event()
virtual_rmouse_thread = None


def run_virtual_mouse():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

                index_x, index_y = 0, 0
                thumb_x, thumb_y = 0, 0
                middle_x, middle_y = 0, 0

                for id, landmark in enumerate(hand.landmark):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    if id == 8:  # Index finger
                        index_x = x
                        index_y = y

                    if id == 4:  # Thumb finger
                        thumb_x = x
                        thumb_y = y

                    if id == 12:  # Middle finger
                        middle_x = x
                        middle_y = y

                # Draw circles around the fingers
                cv2.circle(frame, (int(index_x), int(index_y)), 10, (0, 255, 255), -1)
                cv2.circle(frame, (int(thumb_x), int(thumb_y)), 10, (0, 255, 255), -1)
                cv2.circle(frame, (int(middle_x), int(middle_y)), 10, (0, 255, 255), -1)

                # Calculate distances between fingers
                distance_index_middle = ((middle_x - index_x) ** 2 + (middle_y - index_y) ** 2) ** 0.5
                distance_index_thumb = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

                if distance_index_middle < 50:
                    pyautogui.click()
                    pyautogui.sleep(1)
                elif distance_index_thumb < 80:
                    pyautogui.moveTo(index_x * (screen_width / frame_width), index_y * (screen_height / frame_height))

        cv2.imshow('Virtual Mouse', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            # Killing thread
            if virtual_mouse_thread and virtual_mouse_thread.is_alive():
                stop_virtual_mouse.set()
                virtual_mouse_thread.join()
            break

    cap.release()
    cv2.destroyAllWindows()



def activateVM(request):
    global virtual_mouse_thread
    if not virtual_mouse_thread or not virtual_mouse_thread.is_alive():
        virtual_mouse_thread = threading.Thread(target=run_virtual_mouse)
        virtual_mouse_thread.start()

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    status = "Plugged in" if plugged else "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)


def run_virtual_rmouse():
    cam = cv2.VideoCapture(0)
    print(cv2.__version__)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.0085:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        key = cv2.waitKey(1)
        if key is ord('q'):
            global virtual_rmouse_thread
            if not virtual_rmouse_thread or not virtual_rmouse_thread.is_alive():
                virtual_rmouse_thread = threading.Thread(target=run_virtual_rmouse)
                virtual_rmouse_thread.start()
            break
    cv2.destroyAllWindows()  # Close OpenCV windows

def activateRM(request):
    global virtual_rmouse_thread
    if not virtual_rmouse_thread or not virtual_rmouse_thread.is_alive():
        virtual_rmouse_thread = threading.Thread(target=run_virtual_rmouse)
        virtual_rmouse_thread.start()

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    status = "Plugged in" if plugged else "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def execHand(request):
    HandGest1 = HandGest.objects.all()
    context={
        'HandGest1' : HandGest1,
    }
    return render(request,'home/templates/gesttabs.html',context)

def execHandTab(request):
    # Url
    fbUrl = 'https://www.facebook.com/'
    instaUrl = 'https://www.instagram.com/'
    meetUrl = 'https://meet.google.com/'

    # Variables
    width, height = 500, 500

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Variables
    imgNumber = 0
    hs, ws = int(120 * 1), 213
    gestureThreshold = 300
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 30
    annotations = [[]]
    annotationNumber = -1
    annotationStart = False

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    while True:
        try:
            # Import images
            success, img = cap.read()
            img = cv2.flip(img, 1)

            hands, img = detector.findHands(img)

            if hands and len(hands) == 1:
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                print(fingers)
                lmList = hand['lmList']

                # Constrain value for easier drawing
                indexFinger = lmList[8][0], lmList[8][1]
                xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
                yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

                indexFinger = xVal, yVal

                # Gesture1
                # Thumb = Open FaceBook
                if fingers == [1, 0, 0, 0, 0]:
                    webbrowser.open(fbUrl)
                    time.sleep(2)


                # Gesture 3
                # Thumb + Index + Middle Finger = Calculator
                if fingers == [1, 1, 1, 0, 0]:
                    calculator_process = subprocess.Popen('calc.exe')
                    # Close the calculator process
                    time.sleep(2)

                # Gesture 4
                # Thumb + Index + Middle + After Index = File
                if fingers == [1, 1, 1, 1, 0]:
                    subprocess.Popen('explorer')
                    time.sleep(2)

                # Gesture 5
                # ALl up = Whatsapp
                if fingers == [0, 1, 0, 0, 0]:
                    # Open whatsapp
                    webbrowser.open('https://web.whatsapp.com/')
                    time.sleep(2)

                # #Gesture 6
                # Pinki and Thumb = Settings
                if fingers == [1, 0, 0, 0, 1]:
                    subprocess.Popen('explorer.exe ms-settings:')
                    time.sleep(2)

                # #Gesture 7
                # Thumb + Index + Pinki = Mail
                if fingers == [1, 1, 0, 0, 1]:
                    webbrowser.open('mailto:')
                    time.sleep(2)



        except BrokenPipeError as e:
            pass

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp' : desktop_path,
    }

    return render(request, 'home/templates/index.html', context)


def pres(request):
    # Replace 'Presentation' with the actual path to your Presentation folder
    presentation_folder = 'Presentation'

    # Initialize an empty list to store folder names
    folder_list = []

    # Get a list of directories within the Presentation folder
    try:
        folders = os.listdir(presentation_folder)

        # Filter out only directories (excluding files)
        for folder in folders:
            folder_path = os.path.join(presentation_folder, folder)
            if os.path.isdir(folder_path):
                folder_list.append(folder)

    except FileNotFoundError:
        # Handle the case when the Presentation folder does not exist
        return "Presentation folder not found."

    # Now folder_list contains the names of folders within the Presentation folder
    # You can do whatever you want with the folder_list, for example, return it as part of the response
    context = {
        'FolderDets': folder_list,
    }
    return render(request, 'home/templates/present.html', context)

def execPresentation(request,Fname):
    # Variables
    width, height = 1280, 720
    folderPath = 'Presentation/'+Fname

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Get list of images
    pathImages = sorted(os.listdir(folderPath), key=len)
    print(pathImages)

    # Variables
    imgNumber = 0
    hs, ws = int(120 * 1), 213
    gestureThreshold = 300
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 30
    annotations = [[]]
    annotationNumber = -1
    annotationStart = False

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)
        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage)

        # Resize the image to fit the screen
        imgCurrent = cv2.resize(imgCurrent, (width+250, height+70))

        hands, img = detector.findHands(img)

        if hands and buttonPressed is False:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
            lmList = hand['lmList']

            # Constrain value for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

            indexFinger = xVal, yVal
            # Gesture 1
            # Thumb = Backward
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                if imgNumber > 0:
                    imgNumber -= 1
                    buttonPressed = True

            # Gesture 2
            # Pinki Finger = Forward
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                    buttonPressed = True

            # Gesture 3
            # Show Pointer = Second and Index Finger
            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

            # Gesture 4
            # DrawPointer
            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotations[annotationNumber].append(indexFinger)
            else:
                annotationStart = False

            # Gesture 5
            # Erase
            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True

        # Button Pressed Iterations
        if buttonPressed:
            buttonCounter += 1
            if buttonCounter > buttonDelay:
                buttonCounter = 0
                buttonPressed = False

        for i in range(len(annotations)):
            for j in range(len(annotations[i])):
                if j != 0:
                    cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 200), 12)

            # Adding webcam image in slide
            imgSmall = cv2.resize(img, (ws, hs))
            h, w, _ = imgCurrent.shape
            imgCurrent[0:hs, w - ws:w] = imgSmall

        cv2.imshow("Image", img)
        cv2.imshow("Slides", imgCurrent)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


    # Replace 'Presentation' with the actual path to your Presentation folder
    presentation_folder = 'Presentation'

    # Initialize an empty list to store folder names
    folder_list = []

    # Get a list of directories within the Presentation folder
    try:
        folders = os.listdir(presentation_folder)

        # Filter out only directories (excluding files)
        for folder in folders:
            folder_path = os.path.join(presentation_folder, folder)
            if os.path.isdir(folder_path):
                folder_list.append(folder)

    except FileNotFoundError:
        # Handle the case when the Presentation folder does not exist
        return "Presentation folder not found."

    # Now folder_list contains the names of folders within the Presentation folder
    # You can do whatever you want with the folder_list, for example, return it as part of the response
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def index2(request):
    return render(request, 'home/templates/index.html')

def frontEndForJarvis(request):
    #runJarvis(request)
    features = []
    features.append('open youtube')
    features.append('open notepad')
    features.append('tell me a joke')
    features.append('turn bluetooth on')
    features.append('get date or time')
    features.append('open command prompt')
    features.append('open camera')
    features.append('play music')
    features.append('ip address')
    features.append('wikipedia')
    features.append('stack overflow')
    features.append('linkedin')
    features.append('play song on youtube')
    features.append('close notepad')
    features.append('shut down')
    features.append('restart computer')
    features.append('say you can sleep to turn it off')
    features.append('say no thank to turn it off')
    features.append('where are we')
    features.append('read pdf')
    features.append('send message')
    features.append('translate')
    context = {'feats': features}
    return render(request, 'home/templates/jarvis1.html',context)

def runJarvis(request,flag=1):
    # Initialize COM explicitly
    comtypes.CoInitialize()

    # Initialize pyttsx3 engine
    engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # to convert voice into text  Take command
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                speak('Timeout occurred. Please try again.')
                return 'none'

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
        except Exception as e:
            speak('Sorry, I could not understand that. Please try again.')
            return 'none'
        return query

    # To wish
    def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak('Good morning')
        elif hour >= 12 and hour <= 18:
            speak('Good Afternoon')
        else:
            speak('Good evening')
        speak('I am Jarvis Sir , please tell me how can i help you')

    # # send email
    # def sendEmail(to,content):
    #     server = smtplib.SMTP('smtp.gmail.com',587)
    #     server.ehlo()
    #     server.starttls()
    #     server.login('stevejobs01082003@gmail.com','9730889531')
    #     server.sendmail('stevejobs01082003@gmail.com',to,content)
    #     server.close()


    #Translation in python
    def translate_text(text, target_language='en'):
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation

    # read the pdf
    def pdf_reader():
        try:
            speak('What is the name of the pdf to read?')
            pdfName = takecommand().lower()
            book = open(f'{pdfName}.pdf', 'rb')
            pdfReader = PyPDF2.PdfReader(book)
            num_pages = len(pdfReader.pages)
            speak(f'Total number of pages in the book: {num_pages}')
            speak('Sir, please type the page number I have to read.')
            cm = input('Enter the page number you want me to read')
            pg = int(cm)
            page = pdfReader.pages[pg]
            text = page.extract_text()
            speak(text)
        except:
            pass

    if flag=='2':
        speak('thanks for using me sir , have a good day')
        sys.exit()
        Icons = IconsForDesktop.objects.all()
        BIcons = BottomSideIcons.objects.all()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        if plugged:
            status = "Plugged in"
        else:
            status = "Not plugged in"

        desktop_path = os.path.expanduser("~/Desktop")
        folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

        context = {
            'Icon': Icons,
            'folders': folders,
            'BIcons': BIcons,
            'perc': percent,
            'status': status,
            'deskp': desktop_path,
        }
        return render(request, 'home/templates/index.html', context)

    wish()
    while True:
            query = takecommand().lower()

            # logic building for tasks
            if 'open notepad' in query:
                # Open Notepad
                subprocess.Popen('notepad.exe')

                speak('Speak what you want to write in this notepad file')

                # Get input from the user
                text = takecommand().lower()

                # Simulate typing into Notepad
                pyautogui.typewrite(text)
                speak('Text successfully written to Notepad.')

            elif 'bluetooth on' in query or 'on bluetooth' in query:

                # Open Windows Settings
                pyautogui.press('win')
                time.sleep(3)
                pyautogui.typewrite('settings')
                pyautogui.press('enter')
                time.sleep(3)

                # Search for Bluetooth settings
                pyautogui.typewrite('Bluetooth')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(3)

                # Enable Bluetooth
                pyautogui.press('tab', presses=3)
                pyautogui.press('space')
                time.sleep(3)

                print("Bluetooth enabled successfully.")


            elif 'date' in query or 'time' in query:
                # Get the current date and time
                current_datetime = datetime.datetime.now()

                # Extract the time and date components
                current_time = current_datetime.strftime("%H:%M:%S")
                current_date = current_datetime.strftime("%Y-%m-%d")

                # Print the time and date
                speak(f"Current Time: {current_time}")
                speak(f"Current Date: {current_date}")


            elif 'open command prompt' in query:
                subprocess.Popen('start cmd', shell=True)

            elif 'open camera' in query:
                os.system("start microsoft.windows.camera:")

            elif 'play music' in query:
                music_dir = 'D:\\Yashu\\Entertainment And Spirituality\\Radha Krishna Songs'
                songs = os.listdir(music_dir)
                if songs:
                    rd = random.choice(songs)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))

            elif 'ip address' in query:
                ip = get('http://api.ipify.org').text
                speak(f'your ip address is {ip}')

            elif 'wikipedia' in query:
                speak('searching wikipedia')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak('according to wikipedia')
                speak(results)
                print(results)

            elif 'open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'stack overflow' in query:
                webbrowser.open('stackoverflow.com')

            elif 'linkedin' in query:
                webbrowser.open('https://www.linkedin.com/')

            elif 'meet' in query:
                webbrowser.open('https://www.meet.com/')

            elif 'open google' in query:
                speak('sir , what would i search in google?')
                cm = takecommand().lower()
                webbrowser.open(f'{cm}')

            elif 'play song on youtube' in query:
                speak('sir , which song do you want me to play?')
                cm = takecommand().lower()
                kit.playonyt(f'{cm}')

            # elif 'send email' in query:
            #     try:
            #         speak('what is the gmail of the receiver ?')
            #         gmailid = 'yashmahajan01082003@gmail.com'
            #         speak('what should i send ?')
            #         content = takecommand().lower()
            #         to = gmailid
            #         sendEmail(to,content)
            #         speak(f'email has been sent to {gmailid}')
            #
            #     except Exception as e:
            #         print(e)
            #         speak(f'Sorry sir ,  could not send email to {gmailid}')

            elif 'no thank' in query:
                Icons = IconsForDesktop.objects.all()
                BIcons = BottomSideIcons.objects.all()
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = battery.percent

                if plugged:
                    status = "Plugged in"
                else:
                    status = "Not plugged in"

                desktop_path = os.path.expanduser("~/Desktop")
                folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

                context = {
                    'Icon': Icons,
                    'folders': folders,
                    'BIcons': BIcons,
                    'perc': percent,
                    'status': status,
                    'deskp': desktop_path,
                }
                return render(request, 'home/templates/index.html', context)

            elif 'close notepad' in query:
                speak('ok sir, closing notepad')
                os.system("taskkill /f /im notepad.exe")

            elif 'shut down' in query:
                os.system("shutdown /s /t 0")

            elif 'restart computer' in query:
                os.system("shutdown /r /t 0")

            elif 'you can sleep' in query:
                speak('thanks for using me sir , have a good day')
                Icons = IconsForDesktop.objects.all()
                BIcons = BottomSideIcons.objects.all()
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = battery.percent

                if plugged:
                    status = "Plugged in"
                else:
                    status = "Not plugged in"

                desktop_path = os.path.expanduser("~/Desktop")
                folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

                context = {
                    'Icon': Icons,
                    'folders': folders,
                    'BIcons': BIcons,
                    'perc': percent,
                    'status': status,
                    'deskp': desktop_path,
                }
                return render(request, 'home/templates/index.html', context)


            elif 'tell me a joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)


            elif 'where are we' in query or 'where am i' in query:
                speak('wait sir , let me check')
                try:
                    ip_address = requests.get('https://api.ipify.org').text
                    print(ip_address)
                    url = f'https://get.geojs.io/v1/ip/geo/{ip_address}.json'
                    geo_requests = requests.get(url, verify=False)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f'Sir, I am not sure, but I think we are in {city} city of {country}.')
                    print(city)
                except Exception as e:
                    speak('Sorry, sir. Due to a network issue, I am not able to determine our location.')
                    pass

            elif 'take screenshot' in query:
                speak('what name would you like to give to this screenshot')
                file_name = takecommand().lower()
                screenshot = pyautogui.screenshot()
                screenshot.save(file_name)

            elif 'read pdf' in query:
                pdf_reader()

            elif 'send message' in query:
                receiver_number = "+918390195131"  # Replace with the actual phone number
                message = "Hello, this is a WhatsApp message sent using Python!"
                time_hour = 22  # Replace with the desired hour
                time_minute = 53  # Replace with the desired minute

                pywhatkit.sendwhatmsg(receiver_number, message, time_hour, time_minute)

            elif 'translate' in query:
                # Example usage
                speak("Speak the text you want to translate")
                text = takecommand().lower()
                speak("In which language do you want to convert it?")
                lang = takecommand().lower()

                if lang=='french':
                    target_language = 'fr'  # Translate to French

                if lang=='english':
                    target_language = 'en'

                if lang=='marathi':
                    target_language = 'mr'

                if lang=='russian':
                    target_language = 'ru'

                if lang=='greek':
                    target_language = 'el'

                if lang=='hindi':
                    target_language = 'hi'

                if lang=='turkish':
                    target_language = 'tr'

                if lang=='arabic':
                    target_language = 'ar'

                if lang=='japanese':
                    target_language = 'ja'

                if lang=='korean':
                    target_language = 'ko'


                translated_text = translate_text(text, target_language)
                print(translated_text)
                speak(translated_text)

            speak('sir , do you have any other work ?')

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context={
        'Icon' : Icons,
        'folders' : folders,
        'BIcons' : BIcons,
        'perc' : percent,
        'status' : status,
        'deskp': desktop_path,
    }
    return render(request,'home/templates/index.html',context)


# views.py
import subprocess
from django.shortcuts import render
from .forms import CommandForm
from .models import CommandHistory

def execute_command(command):
    # Mapping NLP commands to actual shell commands
    nlp_commands = {
        "show ip address": "ipconfig",
        "show network status": "netstat -s",
        "show arp table": "arp -a",
        "ping": "ping",
        "traceroute": "tracert",
        "network diagnostic": "netsh int ip reset",
        "network troubleshoot": "netsh advfirewall reset",
        "show wireless networks": "netsh wlan show networks",
        "show wireless drivers": "netsh wlan show drivers",
        "show wireless profiles": "netsh wlan show profiles",
        "connect to wireless network": "netsh wlan connect name='NETWORK_NAME'",
        "disconnect from wireless network": "netsh wlan disconnect",
        "show firewall settings": "netsh advfirewall show allprofiles",
        "enable firewall": "netsh advfirewall set allprofiles state on",
        "disable firewall": "netsh advfirewall set allprofiles state off",
        "allow port through firewall": "netsh advfirewall firewall add rule name='ALLOW_RULE' dir=in action=allow protocol=TCP localport=PORT",
        "deny port through firewall": "netsh advfirewall firewall add rule name='DENY_RULE' dir=in action=block protocol=TCP localport=PORT",
        "show DHCP settings": "netsh dhcp show server",
        "release DHCP lease": "ipconfig /release",
        "renew DHCP lease": "ipconfig /renew",
        "show network adapter settings": "ipconfig /all",
        "show routing table": "route print",
        "show active connections": "netstat -n",
        "show port usage": "netstat -p",
        "show firewall rules": "netsh advfirewall firewall show rule all",
        "show active ports": "netstat -ano",
        "show network interfaces": "netsh interface show interface",
        "show interface statistics": "netstat -e",
        "show interface configuration": "netsh interface ipv4 show config",
        "show IP configuration": "ipconfig /displaydns",
        "show network shares": "net view",
        "show shared resources": "net share",
        "show network traffic": "netstat -s",
        "show network usage": "netstat -e",
        "show network latency": "ping -n 10",
        "show network throughput": "ping -n 10",
        "show network connections per process": "netstat -b",
        "show network speed": "ping -n 10",
        "show network bandwidth": "ping -n 10",
        "show network latency": "ping -n 10",
        "list hidden files": "dir /a:h",
        "list system files": "dir /a:s",
        "list read-only files": "dir /a:r",
        "list files by size": "dir /o:s",
        "list files by date": "dir /o:d",
        "list files by type": "dir /o:g",
        "show disk usage": "fsutil volume diskfree c:",
        "show folder size": "dir /s",
        "show folder size (human readable)": "dir /s | find /c /v \"\" && dir /s | find /i \"bytes\"",
        "show folder tree": "tree",
        "compress files": "compact /c",
        "decompress files": "compact /u",
        "view event logs": "eventvwr.msc",
        "open control panel": "control",
        "show running services": "services.msc",
        "show scheduled tasks": "taskschd.msc",
        "show firewall settings": "firewall.cpl",
        "show network adapters": "ncpa.cpl",
        "show system properties": "sysdm.cpl",
        "show installed programs": "appwiz.cpl",
        "open device manager": "devmgmt.msc",
        "open disk management": "diskmgmt.msc",
        "open performance monitor": "perfmon.msc",
        "open registry editor": "regedit",
        "run notepad": "notepad",
        "show network uptime": "net statistics workstation",
        "show network protocols": "netstat -s",
    }

    # Check if the command matches any NLP command, if yes, get the mapped shell command
    shell_command = nlp_commands.get(command.lower())
    if shell_command:
        command = shell_command

    # Execute the command using subprocess
    output = subprocess.getoutput(command)
    return output

def terminal(request):
    cwd = request.POST.get('cwd', '')  # Get the current working directory from the form data
    output = ""  # Initialize the output variable

    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data['command']
            if command == 'cd..':  # Handle cd.. command
                # Add your logic for changing directories here
                # Example: os.chdir(new_directory)
                output = "Changed directory to <new_directory>"
            elif command == 'clearhistory':  # Handle clearhistory command
                CommandHistory.objects.all().delete()  # Delete all records from the CommandHistory model
                output = "Command history cleared"
            else:
                # Execute other commands using execute_command function
                output = execute_command(command)

            # Create a new CommandHistory entry for the executed command
            CommandHistory.objects.create(command=command, output=output)

    else:
        form = CommandForm()

    # Fetch command history here
    command_history = CommandHistory.objects.all().order_by('-timestamp')[:10]

    return render(request, 'home/templates/terminal.html',
                  {'form': form, 'command_history': command_history, 'cwd': cwd, 'output': output})

def execFaceMesh(request):
    class FaceMeshDetector():
        def __init__(self, static_image_mode=False, max_num_faces=1, refine_landmarks=False,
                     min_detection_confidence=0.5, min_tracking_confidence=0.5):

            self.static_image_mode = False,
            self.max_num_faces = 1,
            self.refine_landmarks = False,
            self.min_detection_confidence = 0.5,
            self.min_tracking_confidence = 0.5

            self.mpDraw = mp.solutions.drawing_utils
            self.mpFaceMesh = mp.solutions.face_mesh
            self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)
            self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

        def findFaceMesh(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.faceMesh.process(imgRGB)
            if results.multi_face_landmarks:
                for faceLms in results.multi_face_landmarks:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec,
                                               self.drawSpec)

                    for id, lm in enumerate(faceLms.landmark):
                        print(lm)
                        ih, iw, ic = img.shape
                        x, y = int(lm.x * iw), int(lm.y * ih)
                        print(id, x, y)
            return img

    def main():
        cap = cv2.VideoCapture(0)
        pTime = 0
        detector = FaceMeshDetector()
        while True:
            success, img = cap.read()
            img = detector.findFaceMesh(img)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS : {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cv2.destroyAllWindows()

    main()
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def execBrightnessControl(request):
    # Define the maximum and minimum brightness values
    MAX_BRIGHTNESS = 100
    MIN_BRIGHTNESS = 0
    pythoncom.CoInitialize()
    # Connect to WMI
    wmi_obj = wmi.WMI(namespace="wmi")

    # Function to set the screen brightness
    def set_brightness(value):
        # Clamp the value within the brightness range
        brightness = max(min(value, MAX_BRIGHTNESS), MIN_BRIGHTNESS)

        # Scale the brightness value to the range [0, 100]
        brightness = int(brightness * 100 / MAX_BRIGHTNESS)

        # Set the screen brightness
        wmi_obj.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

    cap = cv2.VideoCapture(0)
    hd = HandDetector()
    val = 0
    while True:
        ret, img = cap.read()
        if not ret:
            break

        hands, img = hd.findHands(img)

        if hands:
            lm = hands[0]['lmList']

            length, info, img = hd.findDistance(lm[8][0:2], lm[4][0:2], img)
            blevel = np.interp(length, [25, 145], [0, 100])
            val = np.interp(length, [0, 100], [400, 150])
            blevel = int(blevel)

            set_brightness(blevel)

            cv2.rectangle(img, (20, 150), (85, 400), (0, 255, 255), 4)
            cv2.rectangle(img, (20, int(val)), (85, 400), (0, 0, 255), -1)
            cv2.putText(img, str(blevel) + '%', (20, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)


def execFaceDistance(request):
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=1)

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            # cv2.line(img,pointLeft,pointRight,(0,200,0),3)
            # cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
            # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3

            # Finding the focal length
            # d = 50
            # f = (w*d)/W
            # print(f)

            # Finding the distance or depth
            f = 500
            d = (W * f) / w
            print(d)

            cvzone.putTextRect(img, f'Depth : {int(d)} cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def execVirtualVolumeController(request):
    pythoncom.CoInitialize()
    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(0, None)
    minVol = volRange[0]
    maxVol = volRange[1]
    print(minVol, maxVol)
    vol = 0
    volBar = 400
    volPer = 0

    # dimensions
    wCm, hCam = 1200, 720

    cap = cv2.VideoCapture(0)
    cap.set(3, wCm)
    cap.set(4, hCam)
    pTime = 0

    detector = handDetector(detectionCon=0.7)

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            # print(lmList[4],lmList[8])

            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            # Hand range 10 - 200
            # Volume Range -65  - 0
            vol = np.interp(length, [50, 250], [minVol, maxVol])
            volBar = np.interp(length, [50, 250], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])

            print(vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 0), 3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f' FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        cv2.imshow("Img", img)
        key = cv2.waitKey(1)
        if key is ord('q'):
            break
    cv2.destroyAllWindows()  # Close OpenCV windows
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)



def speciallyabled(request):
    # Variables
    width, height = 500, 500

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)


    while True:
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img)

        if hands and len(hands) == 1:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
            lmList = hand['lmList']

            # Thumb tip and index tip coordinates
            thumbTip = lmList[4][0], lmList[4][1]
            indexTip = lmList[8][0], lmList[8][1]

            # Calculate distance between thumb tip and index tip
            distance = np.linalg.norm(np.array(thumbTip) - np.array(indexTip))

            # Constrain value for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

            indexFinger = xVal, yVal

            # Gesture1
            # Display "Nice" if the distance is very less
            if distance < 30:  # Adjust the threshold value as needed
                text = 'Fine'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


            if fingers == [1, 1, 1, 1, 1]:
                text = 'Wait'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Thumb = Drink Water
            elif fingers == [1, 0, 0, 0, 0]:
                text = 'Drink Water'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture2
            # Thumb + Index = Smile
            elif fingers == [1, 1, 0, 0, 0]:
                text = 'Smile'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 3
            # Thumb + Index + Middle Finger = Understood
            elif fingers == [1, 1, 1, 0, 0]:
                text = 'Understood'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 4
            # Thumb + Index + Middle + Ring = Rock On
            elif fingers == [0, 1, 0, 0, 1]:
                text = 'Rock On'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 5
            # Index = No
            elif fingers == [0, 1, 0, 0, 0]:
                text = 'No'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 6
            # Pinky and Thumb = Call
            elif fingers == [1, 0, 0, 0, 1]:
                text = 'Call'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 7
            # Thumb + Index + Pinky = I Love U
            elif fingers == [1, 1, 0, 0, 1]:
                text = 'I Love U'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 8
            # Index + Middle + Ring = Slow
            elif fingers == [0, 1, 1, 1, 0]:
                text = 'Slow'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 9
            # Index + Middle = Louder
            elif fingers == [0, 1, 1, 0, 0]:
                text = 'Louder'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Gesture 10
            # Pinky = Repeat
            elif fingers == [0, 0, 0, 0, 1]:
                text = 'Repeat'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            elif fingers == [0, 0, 1, 0, 0]:
                text = 'Go To Hell'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()  # Close OpenCV windows

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def speciallyabled2(request):
    # Variables
    width, height = 500, 500

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Text-to-Speech Engine
    engine = pyttsx3.init()

    while True:
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img)

        if hands and len(hands) == 1:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
            lmList = hand['lmList']

            # Thumb tip and index tip coordinates
            thumbTip = lmList[4][0], lmList[4][1]
            indexTip = lmList[8][0], lmList[8][1]

            # Calculate distance between thumb tip and index tip
            distance = np.linalg.norm(np.array(thumbTip) - np.array(indexTip))

            # Constrain value for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

            indexFinger = xVal, yVal

            # Gesture1
            # Display "Nice" if the distance is very less
            if distance < 30:  # Adjust the threshold value as needed
                text = 'Fine'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            if fingers == [1, 1, 1, 1, 1]:
                text = 'Wait'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Thumb = Drink Water
            elif fingers == [1, 0, 0, 0, 0]:
                text = 'Drink Water'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture2
            # Thumb + Index = Smile
            elif fingers == [1, 1, 0, 0, 0]:
                text = 'Smile'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 3
            # Thumb + Index + Middle Finger = Understood
            elif fingers == [1, 1, 1, 0, 0]:
                text = 'Understood'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 4
            # Thumb + Index + Middle + Ring = Rock On
            elif fingers == [0, 1, 0, 0, 1]:
                text = 'Rock On'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 5
            # Index = No
            elif fingers == [0, 1, 0, 0, 0]:
                text = 'No'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 6
            # Pinky and Thumb = Call
            elif fingers == [1, 0, 0, 0, 1]:
                text = 'Call'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 7
            # Thumb + Index + Pinky = I Love U
            elif fingers == [1, 1, 0, 0, 1]:
                text = 'I Love U'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 8
            # Index + Middle + Ring = Slow
            elif fingers == [0, 1, 1, 1, 0]:
                text = 'Slow'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 9
            # Index + Middle = Louder
            elif fingers == [0, 1, 1, 0, 0]:
                text = 'Louder'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            # Gesture 10
            # Pinky = Repeat
            elif fingers == [0, 0, 0, 0, 1]:
                text = 'Repeat'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

            elif fingers == [0, 0, 1, 0, 0]:
                text = 'Go To Hell'
                cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                engine.say(text)
                engine.runAndWait()

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()  # Close OpenCV windows

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def get_file_extension(folder_path, fName):
    full_path = os.path.join(folder_path, fName)
    _, extension = os.path.splitext(full_path)
    return extension

import pygame
import threading
import glob
import os
from time import sleep

def run_pygame(Fname,flag=1):
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption('Car Simulation')

    # Set up the window
    window = pygame.display.set_mode((1200, 400))

    # Load the track and car images
    track = pygame.image.load(Fname)  # Replace with your track image filename
    car = pygame.image.load('tesla.png')
    car = pygame.transform.scale(car, (30, 60))
    prev_direction = ''
    direction_count = 0
    # Car initial position
    car_x = 997
    car_y = 300

    # Other variables
    clock = pygame.time.Clock()
    focal_dis = 30
    direction = 'up'
    drive = True
    cam_x_offset = 0
    cam_y_offset = 0
    clicked_points = []  # List to store clicked points on the path
    end_point = (441, 60)  # Replace with actual end point coordinates

    def is_on_path(click_pos):
        track_rect = track.get_rect()
        return track_rect.collidepoint(click_pos)

    DELAY = 3
    counter = 1

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        drive = not drive
                        if counter % 2 == 1:
                            counter += 1
                        else:
                            counter += 1
                    elif event.key == pygame.K_r:
                        clicked_points = []
                    elif event.key == pygame.K_q:
                        if direction == 'left':
                            direction = 'right'
                            car = pygame.transform.rotate(car, 180)
                            cam_x_offset = 30
                        elif direction == 'down':
                            direction = 'up'
                            car = pygame.transform.rotate(car, 180)
                            cam_y_offset = -10

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()
                    if is_on_path(click_pos):
                        clicked_points.append(click_pos)

            if not drive:
                continue

            clock.tick(30)

            cam_x = car_x + 15 + cam_x_offset
            cam_y = car_y + 15 + cam_y_offset

            up_px = window.get_at((cam_x, cam_y - focal_dis))
            right_px = window.get_at((cam_x + focal_dis, cam_y))
            down_px = window.get_at((cam_x, cam_y + focal_dis))
            left_px = window.get_at((cam_x - focal_dis, cam_y))

            # Print the pixel values for debugging
            print(f"up_px: {up_px}, right_px: {right_px}, down_px: {down_px}, left_px: {left_px}")
            # Close the window if specific pixel values are detected
            if (up_px == (46, 170, 108, 255) and
                    right_px == (233, 194, 168, 255) and
                    down_px == (46, 170, 108, 255) and
                    left_px == (235, 51, 36, 255)):
                pygame.quit()
                return


            if (up_px == (172, 116, 98, 255) and
                right_px == (46, 170, 108, 255) and
                down_px == (237, 28, 36, 255) and
                left_px == (46, 170, 108, 255)):
                pygame.quit()
                return

            # Check if the color is red
            if up_px[:3] == (255, 0, 0) or right_px[:3] == (255, 0, 0) or down_px[:3] == (255, 0, 0) or left_px[:3] == (255, 0, 0):
                drive = False

            if direction == 'up' and up_px[0] != 255 and right_px[0] == 255:
                direction = 'right'
                cam_x_offset = 30
                car = pygame.transform.rotate(car, -90)
                sleep(DELAY)
            elif direction == 'right' and right_px[0] != 255 and down_px[0] == 255:
                direction = 'down'
                car_x += 30
                cam_x_offset = 0
                cam_y_offset = 30
                car = pygame.transform.rotate(car, -90)
                sleep(DELAY)
            elif direction == 'down' and down_px[0] != 255 and right_px[0] == 255:
                direction = 'right'
                car_y += 30
                cam_x_offset = 30
                cam_y_offset = 0
                car = pygame.transform.rotate(car, 90)
                sleep(DELAY)
            elif direction == 'right' and right_px[0] != 255 and up_px[0] == 255:
                direction = 'up'
                car_x += 30
                cam_x_offset = 0
                car = pygame.transform.rotate(car, 90)
                sleep(DELAY)
            elif direction == 'up' and up_px[0] != 255 and left_px[0] == 255:
                direction = 'left'
                car = pygame.transform.rotate(car, 90)
                sleep(DELAY)
            elif direction == 'left' and left_px[0] != 255 and down_px[0] == 255:
                direction = 'down'
                cam_y_offset = 30
                car = pygame.transform.rotate(car, 90)
                sleep(DELAY)
            elif direction == 'down' and down_px[0] != 255 and left_px[0] == 255:
                direction = 'left'
                car_y += 30
                cam_y_offset = 0
                car = pygame.transform.rotate(car, -90)
                sleep(DELAY)
            elif direction == 'left' and left_px[0] != 255 and up_px[0] == 255:
                direction = 'up'
                car = pygame.transform.rotate(car, -90)
                sleep(DELAY)

            if flag != 1:
                # Initialize COM explicitly
                comtypes.CoInitialize()

                # Initialize pyttsx3 engine
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voices', voices[0].id)

                def speak(audio):
                    engine.say(audio)
                    engine.runAndWait()


                if direction != prev_direction:
                        speak(direction)
                        prev_direction = direction
                        direction_count = 0
                else:
                        direction_count += 1
                        if direction_count == 30:
                            speak(direction)
                            direction_count = 0

            def check_collision(x, y):
                for rect in clicked_points:
                    if rect[0] < x < rect[0] + 10 and rect[1] < y < rect[1] + 10:
                        return True
                return False

            if direction == 'up' and up_px[0] == 255 and not check_collision(car_x, car_y - 2):
                car_y -= 2
            elif direction == 'right' and right_px[0] == 255 and not check_collision(car_x + 2, car_y):
                car_x += 2
            elif direction == 'down' and down_px[0] == 255 and not check_collision(car_x, car_y + 2):
                car_y += 2
            elif direction == 'left' and left_px[0] == 255 and not check_collision(car_x - 2, car_y):
                car_x -= 2
            elif left_px[0] != 255 and right_px[0] != 255 and up_px[0] != 255 and down_px[0] != 255:
                drive2 = False

            window.fill((0, 0, 0))
            window.blit(track, (0, 0))
            window.blit(car, (car_x, car_y))
            pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)

            for point in clicked_points:
                pygame.draw.rect(window, (255, 0, 0), (point[0], point[1], 50, 50))

            pygame.display.update()
    finally:
        pygame.quit()

def execPresentation2(request, Fname,flag=1):
    if flag==1:
        run_pygame(Fname)
    else:
        run_pygame(Fname,2)
    parts = Fname.split('\\')
    filename_with_extension = parts[-1]
    filename, extension = filename_with_extension.split('.')
    png_files = glob.glob(os.path.join(filename, '*.png'))

    context = {
        'FolderDets': png_files,
    }
    return render(request, 'home/templates/drivingguide.html', context)

def drivingguide(request,path='default'):
    # Replace 'Default' with the actual folder path
    presentation_folder = path

    # Get a list of .png files in the folder
    png_files = glob.glob(os.path.join(presentation_folder, '*.png'))

    # Create a context dictionary with the list of .png files
    context = {
        'FolderDets': png_files,
    }
    return render(request, 'home/templates/drivingguide.html', context)



def voice(request,flag=1):
    # Initialize COM explicitly
    comtypes.CoInitialize()

    # Initialize pyttsx3 engine
    engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # to convert voice into text  Take command
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                speak('Timeout occurred. Please try again.')
                return 'none'

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
        except Exception as e:
            speak('Sorry, I could not understand that. Please try again.')
            return 'none'
        return query

    # To wish
    def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak('Good morning')
        elif hour >= 12 and hour <= 18:
            speak('Good Afternoon')
        else:
            speak('Good evening')
    wish()
    if flag==1:
        speak('Where are you now?')
        query = takecommand().lower()
        return query
    else:
        speak('Where do you want to go?')
        query = takecommand().lower()
        return query

def voiceGuide(request):
    source=voice(request,1)
    destination = voice(request,2)
    res = source+'\\'+destination+'.png'

    execPresentation2(request,res,2)
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def index3(request):
    folder_path = 'images'  # Replace 'path/to/your/images/folder' with the actual path to your 'images' folder
    files_list = os.listdir(folder_path)

    # Now 'files_list' contains the names of all the files in the 'images' folder
    # You can use this list as needed in your function

    # For example, you can print the list of files:
    print(files_list)
    folder_list = files_list
    context = {
        'FolderDets': folder_list,
    }
    return render(request, 'home/templates/index3.html',context)



def execVZoomer(request,Fname):
    cap = cv2.VideoCapture(0)
    cap.set(3, 1200)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)
    startDist = None
    scale = 0
    cx, cy = 500, 500

    images_folder = "images"  # Replace this with the actual path to your "images" folder

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)
        img_path = os.path.join(images_folder, Fname)
        img1 = cv2.imread(img_path)
        img1 = cv2.resize(img1, (350, 250))  # Resize img1 to match the ROI size

        if len(hands) == 2:
            if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
                lmList1 = hands[0]["lmList"]
                lmList2 = hands[1]["lmList"]

                if startDist is None:
                    # Point 8 is the tip of the index finger
                    x1, y1 = lmList1[8][1], lmList1[8][2]
                    x2, y2 = lmList2[8][1], lmList2[8][2]
                    length, info, img = detector.findDistance([lmList1[8][0], lmList1[8][1]],
                                                              [lmList2[8][0], lmList2[8][1]], img)
                    startDist = length

                length, info, img = detector.findDistance([lmList1[8][0], lmList1[8][1]],
                                                          [lmList2[8][0], lmList2[8][1]],
                                                          img)
                scale = int((length - startDist) // 2)
                cx, cy = info[4:]
                print(scale)

        else:
            startDist = None
        try:
            h1, w1, _ = img1.shape
            newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
            img1 = cv2.resize(img1, (newW, newH))

            img[cy - newH // 2: cy + newH // 2, cx - newW // 2: cx + newW // 2] = img1
        except:
            pass

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    folder_path = 'images'  # Replace 'path/to/your/images/folder' with the actual path to your 'images' folder
    files_list = os.listdir(folder_path)

    # Now 'files_list' contains the names of all the files in the 'images' folder
    # You can use this list as needed in your function

    # For example, you can print the list of files:
    print(files_list)
    folder_list = files_list
    context = {
        'FolderDets': folder_list,
    }
    return render(request, 'home/templates/index3.html', context)

def faceBlur(request):
    import os
    import cv2
    import mediapipe as mp

    def process_img(img, face_detection):
        H, W, _ = img.shape
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)

        if out.detections is not None:
            for detection in out.detections:
                location_data = detection.location_data
                bbox = location_data.relative_bounding_box

                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

                x1 = int(x1 * W)
                y1 = int(y1 * H)
                w = int(w * W)
                h = int(h * H)

                img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))

        return img

    output_dir = './output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        cap = cv2.VideoCapture(0)  # Use index 0 to capture video from the default webcam

        ret, frame = cap.read()
        while ret:
            frame = process_img(frame, face_detection)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ret, frame = cap.read()

        cap.release()
        cv2.destroyAllWindows()
        Icons = IconsForDesktop.objects.all()
        BIcons = BottomSideIcons.objects.all()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        if plugged:
            status = "Plugged in"
        else:
            status = "Not plugged in"

        desktop_path = os.path.expanduser("~/Desktop")
        folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

        context = {
            'Icon': Icons,
            'folders': folders,
            'BIcons': BIcons,
            'perc': percent,
            'status': status,
            'deskp': desktop_path,
        }
        return render(request, 'home/templates/index.html', context)

def sarthi(request):
    return render(request, 'home/templates/chatgpt.html')

def hindi_voice_to_text(request,flag):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use default microphone as audio source
    with sr.Microphone() as source:
        if flag==1:
            print("कृपया मराठीत बोला... (Please speak in Marathi)")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Listen for audio input

        if flag==2:
            print("कृपया बोलें... (Please speak in Hindi)")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Listen for audio input
    text=''
    # Recognize speech using Google Speech Recognition
    try:
        print("Transcribing speech...")
        if flag==1:
            text = recognizer.recognize_google(audio, language='hi-IN')
            # Detect language (just to verify it's Hindi)
            detected_language = detect(text)
            print("Detected language:", detected_language)
            return text
        else:
            text = recognizer.recognize_google(audio, language='mr-IN')
            return text

        # Return the transcribed text as a HttpResponse
        return 'fail'
    except sr.UnknownValueError:
        pass


def voiceQuery(request, flag):
    input = ''
    out = ''
    engInp = ''

    try:
        if flag == 'Marathi':
            input = hindi_voice_to_text(request, flag=1)
            out = 'Ma'
        else:
            input = hindi_voice_to_text(request, flag=2)
            out = 'Hin'

        import requests

        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": "Bearer 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"}

        def query(payload, max_length=512):
            payload["options"] = {"max_length": max_length}
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": input,
            "parameters": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }, max_length=2048)
        out = output

        # Format the output
        formatted_output = ''
        for item in out:
            formatted_output += item['generated_text'] + '\n\n'

        out = formatted_output

        # Translate the output to Hindi or Marathi
        # Translate the output to Hindi or Marathi
        from googletrans import Translator
        translator = Translator()
        if flag == 'Marathi':
            out = translator.translate(out, dest='mr').text
        else:
            out = translator.translate(out, dest='hi').text
    except:
        pass

    print(out)
    context = {
        'inp': input,
        'out': out,
    }

    return render(request, 'home/templates/chatgpt.html', context)

def knownBook(request):
    return render(request,'home/templates/knownBook.html')

def storeDet(request):
    import cv2, sys, numpy, os
    haar_file = 'haarcascade_frontalface_default.xml'
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')

        # Create a new Person object and save it to the database
        person = Person.objects.create(
            name=name,
            age=age,
            address=address,
            gender=gender,
            occupation=occupation
        )

    # All the faces data will be
    #  present this folder
    datasets = 'datasets'

    # These are sub data sets of folder,
    # for my faces I've used my name you can
    # change the label here
    sub_data = name

    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)

    # defining the size of images
    (width, height) = (130, 100)

    # '0' is used for my webcam,
    # if you've any other camera
    #  attached use '1' like this
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    # The program loops until it has 30 images of the face.
    count = 1
    while count < 30:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('% s/% s.png' % (path, count), face_resize)
        count += 1

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break

        Icons = IconsForDesktop.objects.all()
        BIcons = BottomSideIcons.objects.all()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        if plugged:
            status = "Plugged in"
        else:
            status = "Not plugged in"

        desktop_path = os.path.expanduser("~/Desktop")
        folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

        context = {
            'Icon': Icons,
            'folders': folders,
            'BIcons': BIcons,
            'perc': percent,
            'status': status,
            'deskp': desktop_path,
        }
        return render(request, 'home/templates/index.html', context)

def detection(request):

    # It helps in identifying the faces
    import cv2, sys, numpy, os
    size = 4
    haar_file = 'haarcascade_frontalface_default.xml'
    datasets = 'datasets'

    # Part 1: Create fisherRecognizer
    print('Recognizing Face Please Be in sufficient Lights...')

    # Create a list of images and a list of corresponding names
    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)

    # Create a Numpy array from the two lists above
    (images, labels) = [numpy.array(lis) for lis in [images, labels]]

    # OpenCV trains a model from the images
    # NOTE FOR OpenCV2: remove '.face'
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)

    # Part 2: Use fisherRecognizer on camera stream
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            # Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if prediction[1] < 500:

                #cv2.putText(im, '% s - %.0f' %
                  #          (names[prediction[0]], prediction[1]), (x - 10, y - 10),
                 #           cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                recognized_name = names[prediction[0]]
                confidence = prediction[1]

                # Fetch details from the Person model
                try:
                    person = Person.objects.filter(name=recognized_name).first()  # Retrieve person details from database
                    details = [
                        f"Name: {person.name}",
                        f"Age: {person.age}",
                        f"Gender: {person.get_gender_display()}",
                        f"Occupation: {person.occupation}"
                    ]

                except Person.DoesNotExist:
                    details = "Person not found in the database"
                y0, dy = y - 10, 20

                for i, detail in enumerate(details):
                    cv2.putText(im, detail, (x - 10, y0 + i * dy),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            else:
                cv2.putText(im, 'not recognized',
                            (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

        cv2.imshow('OpenCV', im)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)

def detection2(request):
    def voice(request):
        # Initialize COM explicitly
        comtypes.CoInitialize()

        # Initialize pyttsx3 engine
        engine = pyttsx3.init('sapi5')
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[0].id)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

    # It helps in identifying the faces
    import cv2, sys, numpy, os
    size = 4
    haar_file = 'haarcascade_frontalface_default.xml'
    datasets = 'datasets'

    # Part 1: Create fisherRecognizer
    print('Recognizing Face Please Be in sufficient Lights...')

    # Create a list of images and a list of corresponding names
    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)

    # Create a Numpy array from the two lists above
    (images, labels) = [numpy.array(lis) for lis in [images, labels]]

    # OpenCV trains a model from the images
    # NOTE FOR OpenCV2: remove '.face'
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)

    # Part 2: Use fisherRecognizer on camera stream
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            # Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if prediction[1] < 500:

                #cv2.putText(im, '% s - %.0f' %
                  #          (names[prediction[0]], prediction[1]), (x - 10, y - 10),
                 #           cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                recognized_name = names[prediction[0]]
                confidence = prediction[1]

                # Fetch details from the Person model
                try:
                    person = Person.objects.filter(name=recognized_name).first()  # Retrieve person details from database
                    details = [
                        f"Name: {person.name}",
                        f"Age: {person.age}",
                        f"Gender: {person.get_gender_display()}",
                        f"Occupation: {person.occupation}"
                    ]
                    pyttsx3.speak(details)
                except Person.DoesNotExist:
                    details = "Person not found in the database"

                cv2.putText(im, f'{details} ', (x - 10, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            else:
                cv2.putText(im, 'not recognized',
                            (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

        cv2.imshow('OpenCV', im)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
        'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import os
import comtypes
import pyttsx3
import speech_recognition as sr
import PyPDF2
import psutil

def pdf_reader(request):
    # Initialize COM explicitly
    comtypes.CoInitialize()

    # Initialize pyttsx3 engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # to convert voice into text  Take command
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                speak('Timeout occurred. Please try again.')
                return 'none'

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
        except Exception as e:
            speak('Sorry, I could not understand that. Please try again.')
            return 'none'
        return query


    try:
        speak('What is the name of the pdf to read?')
        pdfName = takecommand().lower()
        pdf_folder = 'pdf_fold'  # specify the folder path
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        if f'{pdfName}.pdf' in pdf_files:
            book = open(os.path.join(pdf_folder, f'{pdfName}.pdf'), 'rb')
            pdfReader = PyPDF2.PdfReader(book)
            num_pages = len(pdfReader.pages)
            speak(f'Total number of pages in the book: {num_pages}')
            speak('Sir, please say the page number that I have to read.')

            # Variables
            width, height = 500, 500

            # Camera setup
            cap = cv2.VideoCapture(0)
            cap.set(3, width)
            cap.set(4, height)

            # Hand Detector
            detector = HandDetector(detectionCon=0.8, maxHands=2)
            cm=1

            while True:
                try:
                    # Import images
                    success, img = cap.read()
                    img = cv2.flip(img, 1)

                    hands, img = detector.findHands(img)

                    if hands and len(hands) == 1:
                        hand = hands[0]
                        fingers = detector.fingersUp(hand)
                        print(fingers)
                        lmList = hand['lmList']

                        # Constrain value for easier drawing
                        indexFinger = lmList[8][0], lmList[8][1]
                        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
                        yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

                        indexFinger = xVal, yVal

                        # Gesture1
                        # Thumb = Open FaceBook
                        if fingers == [0, 1, 0, 0, 0]:
                            cm = 1
                            cv2.destroyAllWindows()
                            break
                            cv2.destroyAllWindows()

                            # Gesture 3
                        # Thumb + Index + Middle Finger = Calculator
                        if fingers == [0, 1, 1, 0, 0]:
                            cm = 2
                            cv2.destroyAllWindows()
                            break
                            cv2.destroyAllWindows()

                            # Gesture 4
                        # Thumb + Index + Middle + After Index = File
                        if fingers == [0, 1, 1, 1, 0]:
                            cm = 3
                            cv2.destroyAllWindows()
                            break
                            cv2.destroyAllWindows()

                            # Gesture 5
                        # ALl up = Whatsapp
                        if fingers == [0, 1, 1, 1, 1]:
                            cm = 4
                            cv2.destroyAllWindows()
                            break
                            cv2.destroyAllWindows()
                            # #Gesture 6
                        # Pinki and Thumb = Settings
                        if fingers == [1, 1, 1,1, 1]:
                            cm=5
                            cv2.destroyAllWindows()
                            break
                            cv2.destroyAllWindows()
                except BrokenPipeError as e:
                    pass

                cv2.imshow("Image", img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
            cv2.destroyAllWindows()

            pg = cm

            if pg > 0 and pg <= num_pages:
                page = pdfReader.pages[pg - 1]  # adjust for 0-based indexing
                text = page.extract_text()
                speak(text)
            else:
                speak('Invalid page number. Please try again.')
                Icons = IconsForDesktop.objects.all()
                BIcons = BottomSideIcons.objects.all()
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = battery.percent

                if plugged:
                    status = "Plugged in"
                else:
                    status = "Not plugged in"

                desktop_path = os.path.expanduser("~/Desktop")
                folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

                context = {
                    'Icon': Icons,
                    'folders': folders,
                    'BIcons': BIcons,
                    'perc': percent,
                    'status': status,
                    'deskp': desktop_path,
                }
                return render(request, 'home/templates/index.html', context)

        else:
            speak('PDF file not found in the folder.')
            Icons = IconsForDesktop.objects.all()
            BIcons = BottomSideIcons.objects.all()
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = battery.percent

            if plugged:
                status = "Plugged in"
            else:
                status = "Not plugged in"

            desktop_path = os.path.expanduser("~/Desktop")
            folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

            context = {
                'Icon': Icons,
                'folders': folders,
                'BIcons': BIcons,
                'perc': percent,
                'status': status,
                'deskp': desktop_path,
            }
            return render(request, 'home/templates/index.html', context)

    except:
        speak('An error occurred. Please try again.')
        Icons = IconsForDesktop.objects.all()
        BIcons = BottomSideIcons.objects.all()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        if plugged:
            status = "Plugged in"
        else:
            status = "Not plugged in"

        desktop_path = os.path.expanduser("~/Desktop")
        folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

        context = {
            'Icon': Icons,
            'folders': folders,
            'BIcons': BIcons,
            'perc': percent,
            'status': status,
            'deskp': desktop_path,
        }
        return render(request, 'home/templates/index.html', context)
    Icons = IconsForDesktop.objects.all()
    BIcons = BottomSideIcons.objects.all()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged in"
    else:
        status = "Not plugged in"

    desktop_path = os.path.expanduser("~/Desktop")
    folders = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    context = {
        'Icon': Icons,
        'folders': folders,
        'BIcons': BIcons,
        'perc': percent,
       'status': status,
        'deskp': desktop_path,
    }
    return render(request, 'home/templates/index.html', context)