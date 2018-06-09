import cv2, sys, os, subprocess
import pygame
pygame.init()
bg = (75,0,130)
"""xcord, ycord 249.5 224.0
ex, ey 576.0 0
nx, ny 578.475 1.1999999999999993
"""
screen_resolution = output = subprocess.Popen('xrandr | grep "\\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
screen_w, screen_h = screen_resolution.decode().split('x') 
ge = pygame.image.load('test1.png')
eyes = pygame.image.load('eyes.png')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


def show():
    gameDisplay = pygame.display.set_mode((int(screen_w), int(screen_h)))
    pygame.display.set_caption('Gsingh')
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    gameDisplay.fill(bg)
    w = (int(screen_w) - 768)//2
    h = (int(screen_h) - 1280)//2
    gameDisplay.blit(ge, (w,h))
    #gameDisplay.blit(eyes,(w,h))
    pygame.display.update()
    return gameDisplay

def move_eyes(gameDisplay, xcord, ycord,):
    w = int(screen_w)
    h = int(screen_h)
    x = (w-768)//2
    y = h-1280
    ex = (w-768)/2
    ey = h-1180
    nx = ex + (xcord/20)-10
    ny = ey + (ycord/20)-10
    print('ex, ey', ex, ey)
    print('nx, ny', nx, ny)
    gameDisplay.blit(eyes,(nx,ny))
    gameDisplay.blit(ge,(w,h))
    #code to redraw images
    pygame.display.update()

gameDisplay = show()

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    cv2.imshow('img', img)
    print(faces[-1:])
    for x, y, w, h in faces[-1:]:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
        xcord = (x+w)//2
        ycord = 2*(y+h)//3 # to look at the eyes
        print('xcord, ycord', xcord, ycord)
        move_eyes(gameDisplay, xcord, ycord)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

