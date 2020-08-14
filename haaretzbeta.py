import pygame,sys
import time
from pygame.locals import*
pygame.init()
pygame.mixer.music.load('eye.mp3')
pygame.mixer.music.play(-1, 0.0)
clock = pygame.time.Clock()
FPS = 30
f = 0

a = pygame.display.set_mode((800,600), 0 , 32)
pygame.display.set_caption('ha-Aretz')

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)



img = pygame.image.load('band.jpg')
img2 = pygame.image.load('haaretz.jpg')
img3 = pygame.image.load('shaning.jpg')
img4 = pygame.image.load('steven.jpg')
img5 = pygame.image.load('hetong.jpg')
img6 = pygame.image.load('mao.jpg')
img7 = pygame.image.load('shuo.jpg')
img8 = pygame.image.load('daru.jpg')
img9 = pygame.image.load('steven1.jpg')
img10 = pygame.image.load('shaning1.jpg')
img11 = pygame.image.load('hetong1.jpg')
img12 = pygame.image.load('shuo1.jpg')
img13 = pygame.image.load('mao1.jpg')
img14 = pygame.image.load('daru1.jpg')
img15 = pygame.image.load('shaning2.jpg')
img16 = pygame.image.load('steven2.jpg')
img17 = pygame.image.load('hetong2.jpg')
img18 = pygame.image.load('mao2.jpg')
img19 = pygame.image.load('shuo2.jpg')
img20 = pygame.image.load('daru2.jpg')
direction = 'up'
steven2y = 600
hetong2y = 600
while True:
      pos = pygame.mouse.get_pos()
      d = pygame.time.get_ticks()               
      if d > 0:
         a.fill(black)
         a.blit(img3,(0,0))
      if d > 1500:
         a.fill(black)
         a.blit(img4,(0,88))
      if d > 3000:
         a.fill(black)
         a.blit(img5,(288,0))
      if d > 4500:
         a.fill(black)
         a.blit(img6,(288,88))
      if d > 6000:
         a.fill(black)
         a.blit(img7,(144,44))
      if d > 7500:
         a.fill(black)
         a.blit(img8,(144,44))
      if d > 9000:
         a.fill(white)
         a.blit(img,(0,20))
      
      if d > 11200 :
         a.blit(img2,(0,0))
         pygame.draw.line(a, white, (20,400),(20,590), 10)
         pygame.draw.line(a, white, (20,500),(60,500), 10)
         pygame.draw.line(a, white, (55,500),(55,590), 10)
         pygame.draw.line(a, white, (75,500),(75,590), 10)
         pygame.draw.line(a, white, (71,500),(111,500),10)
         pygame.draw.line(a, white, (71,585),(111,585),10)
         pygame.draw.line(a, white, (106,500),(106,600),10)
         pygame.draw.line(a, white, (126,500),(166,500),10)
         pygame.draw.line(a, white, (206,400),(186,590),10)
         pygame.draw.line(a, white, (206,400),(226,590),10)
         pygame.draw.line(a, white, (192,500),(220,500),10)
         pygame.draw.line(a, white, (246,490),(246,590),10)
         pygame.draw.line(a, white, (246,510),(286,500),10)
         pygame.draw.line(a, white, (306,500),(306,590),10)
         pygame.draw.line(a, white, (302,500),(342,500),10)
         pygame.draw.line(a, white, (302,585),(342,585),10)
         pygame.draw.line(a, white, (337,500),(337,540),10)
         pygame.draw.line(a, white, (302,540),(342,540),10)
         pygame.draw.line(a, white, (362,500),(402,500),10)
         pygame.draw.line(a, white, (382,480),(382,590),10)
         pygame.draw.line(a, white, (422,500),(463,500),10)
         pygame.draw.line(a, white, (422,585),(462,585),10)
         pygame.draw.line(a, white, (459,500),(425,585),10)
     
         fontObj = pygame.font.Font('freesansbold.ttf', 20)
         textSurfaceObj = fontObj.render('Band Member', True, white)
         textRectObj = textSurfaceObj.get_rect()
         textRectObj.center = (630, 450)
         e = a.blit(textSurfaceObj, textRectObj)
 
         vocal = fontObj.render('Vocal: DARU', True,white)
         vocalobj = vocal.get_rect()
         vocalobj.center = (635, 490)         
         e = a.blit(vocal, vocalobj)
         if e.collidepoint(pos)  and left_mouse==-1:
            f=1
         if f==1:            
            a.fill(black)
            a.blit(img14,(0,0))
            a.blit(img20,(450,0))
            back = fontObj.render('Back', True,white)
            backobj = back.get_rect()
            backobj.center = (770,10)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0   
         
         guitar1 = fontObj.render('Guitar: SHANING',True,white)
         guitar1obj = guitar1.get_rect()
         guitar1obj.center = (635,510)
         e = a.blit(guitar1,guitar1obj)
         if e.collidepoint(pos)  and left_mouse==-1:
            f=2
         if f == 2:     
            a.fill(black)
            a.blit(img10,(0,0))
            a.blit(img15,(450,0))
            back = fontObj.render('Back', True,white)
            backobj = back.get_rect()
            backobj.center = (770,10)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0   
           
            
            
         
         
         guitar2 = fontObj.render('Guitar: HETONG', True,white)
         guitar2obj = guitar2.get_rect()
         guitar2obj.center = (635,530)
         e = a.blit(guitar2,guitar2obj)                        
         if e.collidepoint(pos) and left_mouse==-1:                
            f=3
         if f==3:             
            a.fill(black)
            a.blit(img11,(0,0))                             
            a.blit(img17,(450,0))
            back = fontObj.render('Back', True,red)
            backobj = back.get_rect()
            backobj.center = (770,400)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0   
       
         
         bass = fontObj.render('Bass: STEVEN',True,white)
         bassobj = bass.get_rect()
         bassobj.center = (635,550)
         e = a.blit(bass,bassobj)
         if e.collidepoint(pos)  and left_mouse==-1:
            f=4
         if f == 4:     
            a.fill(black)           
            a.blit(img9,(0,0))
            a.blit(img16,(450,0))
            back = fontObj.render('Back', True,white)
            backobj = back.get_rect()
            backobj.center = (770,10)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0     
         
         
         
         keyboard = fontObj.render('Keyboard: MAO',True,white)
         keyboardobj = keyboard.get_rect()
         keyboardobj.center = (635,570)
         e = a.blit(keyboard,keyboardobj)
         if e.collidepoint(pos)  and left_mouse==-1:
            f=5
         if f==5:                    
            a.fill(black)
            a.blit(img13,(0,0))
            a.blit(img18,(450,0))
            back = fontObj.render('Back', True,white)
            backobj = back.get_rect()
            backobj.center = (770,10)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0   



         drum = fontObj.render('Drum: SHUO',True,white)
         drumobj = drum.get_rect()
         drumobj.center = (635,590)
         e = a.blit(drum,drumobj)
         if e.collidepoint(pos)  and left_mouse==-1:
            f=6
         if f == 6:           
            a.fill(black)
            a.blit(img12,(0,0))
            a.blit(img19,(450,0))
            back = fontObj.render('Back', True,white)
            backobj = back.get_rect()
            backobj.center = (770,10)
            e = a.blit(back,backobj)
            if e.collidepoint(pos) and left_mouse==-1:
               f=0   

            
            
            
            

      for event in pygame.event.get():
          if event.type == QUIT:
             pygame.quit()
             sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 :
             left_mouse=1
          elif event.type == pygame.MOUSEBUTTONUP and event.button ==1 :
               left_mouse=-1
          else:
               left_mouse=0
      pygame.display.update()
      #clock.tick(60)
