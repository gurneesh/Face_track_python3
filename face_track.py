#!/usr/bin/env python3

import cv2, sys, os, subprocess
import pygame
pygame.init()
bg = (75,0,130)

if os.name == 'posix':
    screen_resolution = output = subprocess.Popen('xrandr | grep "\\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    screen_w, screen_h = screen_resolution.decode().split('x')
else:
    user32 = ctypes.windll.user32
    screen_resolution = str(user32.GetSystemMetrics(0)) + 'x' + str(user32.GetSystemMetrics(1))
    screen_w, screen_h = screen_resolution.split('x')

ge = pygame.image.load('test1.png')
eyes = pygame.image.load('eyes.png')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
print(screen_w, screen_h)

def show():
    gameDisplay = pygame.display.set_mode((int(screen_w), int(screen_h)))
    pygame.display.set_caption('Gsingh')
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    gameDisplay.fill(bg)
    w = (int(screen_w) - 768)//2
    h = (int(screen_h) - 1280)//2
    gameDisplay.blit(ge, (w,h))
    pygame.display.update()
    return gameDisplay

def move_eyes(gameDisplay, xcord, ycord,):
    w = int(screen_w)
    h = int(screen_h)
    img_x = ((w-768)/2) + (xcord/20)-10
    img_y = (h-1180) + (ycord/20)-10
    gameDisplay.blit(eyes,(img_x,img_y))
    gameDisplay.blit(ge,(w,h))
    pygame.display.update()

gameDisplay = show()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    print(faces[-1:])
    for x, y, w, h in faces[-1:]:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
        xcord = (x+w)//2
        ycord = 2*(y+h)//3 
        print('xcord, ycord', xcord, ycord)
        move_eyes(gameDisplay, xcord, ycord)
    #code to show your webcam feed.
    #cv2.imshow('img', img)
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
    #    break
cap.release()
cv2.destroyAllWindows()

