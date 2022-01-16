#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import math
import pygame
import time

#Instead of this list the get_array_value function will be called and the values will be generated from the arduino voltage sensor 
audio_list = [0.1848, 0.1799, 0.1818, 0.1769, 0.1525, 0.1926, 0.1144, 0.1838, 0.1075, 0.1251, 0.1085, 0.1075, 0.1075, 0.1075, 0.1075, 0.1075, 0.1075, 0.1075, 0.2199, 0.5591, 0.5474, 0.1085, 0.1075, 0.1075, 0.1075, 0.4506, 0.2473, 0.1075, 0.1075, 0.1359, 0.1105, 0.1095, 0.1075, 0.1114, 0.1134, 0.8201, 0.1075, 0.6207, 0.8201, 0.8201, 0.1075, 0.8201, 0.262, 0.1085, 0.1075, 0.1075, 0.1916, 0.3304, 0.4213, 0.1075, 0.1075, 0.3539, 0.1193, 0.8201, 0.1075, 0.6227, 0.1144, 0.7449, 0.3519, 0.1075, 0.1095, 0.1916, 0.8201, 0.1075, 0.8201, 0.1075, 0.8201, 0.1075, 0.1075, 0.1085, 0.217, 0.1075, 0.4262, 0.8201, 0.1075, 0.1378, 0.2111, 0.1075, 0.1075, 0.1075, 0.1095, 0.1075, 0.1075, 0.1075, 0.1075, 0.2141, 0.1075, 0.1075, 0.7732, 0.2004, 0.1085, 0.1075, 0.304, 0.1075, 0.1075, 0.1075, 0.8211, 0.1134, 0.2326, 0.174]

def shape_colour(background):
    rgb_val = []
    for i in range(len(audio_list)):
        #colour
        if audio_list[i]*1000 > 700:
            rgb_val.append(audio_list[i]*1000/random.randrange(4,900))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            pygame.draw.ellipse(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (((audio_list[i]*1000/random.randrange(1,50)),(audio_list[i]*1000/random.randrange(1,50))), ((audio_list[i]*1000/random.randrange(1,50)), (audio_list[i]*1000/random.randrange(1,50)))), 0)
        elif audio_list[i]*1000 > 500:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,500))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            pygame.draw.polygon(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), [(audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i], audio_list[i]*1000/1.6)], 0)
        elif audio_list[i]*1000 > 350:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,400))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            pygame.draw.arc(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), ((audio_list[i]*1000, audio_list[i]*1000/1.2), (audio_list[i]*1000, audio_list[i]*1000/1.2)), random.randrange(1,180), random.randrange(1,180), 1)
        elif audio_list[i]*1000 > 150:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,500))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            pygame.draw.polygon(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), [(audio_list[i]*1000 + random.randint(30,50), audio_list[i]*1000), (audio_list[i]*1000, audio_list[i]*1000 + random.randint(30,50)), (audio_list[i]+ random.randint(30,50), audio_list[i]*1000 ), (audio_list[i]*1000, audio_list[i]*1000 + random.randint(30,50)), (audio_list[i]*1000 + random.randint(30,50), audio_list[i]*1000 )], 0)
        elif audio_list[i]*1000 < 50:
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            pygame.draw.circle(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (audio_list[i]*1000, audio_list[i]*1000), audio_list[i]*1300, 0)
        else:
            rgb_val.append(audio_list[i]*1000)
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            pygame.draw.lines(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), True, [(audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255)))], 1)


def shape_colour1(background):
    rgb_val = []
    for i in range(len(audio_list)):
    #colour
        if audio_list[i]*1000 > 700:
            rgb_val.append(audio_list[i]*1000/random.randrange(4,900))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            pygame.draw.ellipse(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (((audio_list[i]*1000/random.randrange(1,50)),(audio_list[i]*1000/random.randrange(1,50))), ((audio_list[i]*1000/random.randrange(1,50)), (audio_list[i]*1000/random.randrange(1,50)))), 0)
        elif audio_list[i]*1000 > 500:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,500))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            pygame.draw.polygon(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), [(audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i], audio_list[i]*1000/1.6)], 0)
        elif audio_list[i]*1000 > 300:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,400))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            pygame.draw.arc(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), ((audio_list[i]*1000, audio_list[i]*1000/1.2), (audio_list[i]*1000, audio_list[i]*1000/1.2)), random.randrange(1,180), random.randrange(1,180), 1)
        elif audio_list[i]*1000 < 50:
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            pygame.draw.circle(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (audio_list[i]*1000, audio_list[i]*1000), audio_list[i]*1300, 0)
        else:
            rgb_val.append(audio_list[i]*1000)
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            pygame.draw.lines(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), True, [(audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255)))], 1)




def shape_colour2(background):
    rgb_val = []
    for i in range(len(audio_list)):
    #colour
        if audio_list[i]*1000 > 700:
            rgb_val.append(audio_list[i]*1000/random.randrange(4,900))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            pygame.draw.ellipse(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (((audio_list[i]*1000/random.randrange(1,50)),(audio_list[i]*1000/random.randrange(1,50))), ((audio_list[i]*1000/random.randrange(1,50)), (audio_list[i]*1000/random.randrange(1,50)))), 0)
        elif audio_list[i]*1000 > 500:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,500))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            pygame.draw.polygon(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), [(audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i]*1000, audio_list[i]*1000/1.6), (audio_list[i], audio_list[i]*1000/1.6)], 0)
        elif audio_list[i]*1000 > 300:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,400))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            pygame.draw.arc(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), ((audio_list[i]*1000, audio_list[i]*1000/1.2), (audio_list[i]*1000, audio_list[i]*1000/1.2)), random.randrange(1,180), random.randrange(1,180), 1)
        elif audio_list[i]*1000 < 50:
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            pygame.draw.circle(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (audio_list[i]*1000, audio_list[i]*1000), audio_list[i]*1300, 0)
        else:
            rgb_val.append(audio_list[i]*1000)
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            pygame.draw.lines(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), True, [(audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255))), (audio_list[i]*1000, abs(audio_list[i]*1000 - random.randrange(0,255)))], 1)


def get_array_value():
    try:
        from pyfirmata import Arduino, util
    except:
        import pip
        pip.main(['install','pyfirmata'])
        from pyfirmata import Arduino, util
    import time
    board=Arduino('/dev/cu.usbserial-0001')
    iterator=util.Iterator(board)
    iterator.start()
    sensor=board.get_pin('a:2:i')
    time.sleep(2.0)
    x=0
    audio_list=[]
    while x<350:
        data=float(sensor.read())
        audio_list.append(data)
        x+=1
        time.sleep(0.2)
    
    return audio_list


def shape_colour3(background):
    rgb_val = []
    for i in range(len(audio_list)):
        #colour
        if audio_list[i]*1000 > 700:
            rgb_val.append(audio_list[i]*1000/random.randrange(4,900))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(4,100))
            pygame.draw.ellipse(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), ((rgb_val[0],rgb_val[2]), (rgb_val[2], rgb_val[0])), 0)
        elif audio_list[i]*1000 > 500:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,500))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,100))
            pygame.draw.polygon(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), [(rgb_val[1], rgb_val[0]), (rgb_val[2], rgb_val[1]), (rgb_val[0], rgb_val[2]) ], 0)
        elif audio_list[i]*1000 > 300:
            rgb_val.append(audio_list[i]*1000/random.randrange(3,400))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            rgb_val.append(audio_list[i]*1000/random.randrange(3,90))
            pygame.draw.arc(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), ((rgb_val[2], rgb_val[1]), (rgb_val[0], rgb_val[2])), rgb_val[0], rgb_val[1], 1)
        elif audio_list[i]*1000 < 50:
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,50)))
            pygame.draw.circle(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), (rgb_val[1], rgb_val[0]), rgb_val[2], 0)
        else:
            rgb_val.append(audio_list[i]*1000)
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            rgb_val.append(abs(audio_list[i]*1000 - random.randrange(0,255)))
            pygame.draw.lines(background, (rgb_val[0],rgb_val[1],rgb_val[2],100), True, [(rgb_val[2], rgb_val[2]), (rgb_val[0], rgb_val[1]), (rgb_val[0], rgb_val[0])], 1)
            
def gameframe():
    
    # D - Display configuration
    screen = pygame.display.set_mode((750, 480))
    pygame.display.set_caption("Audio Visualizer")
    # E - Entities (just background for now)
    background = pygame.Surface(screen.get_size(),pygame.SRCALPHA)
    background = background.convert()
    background.fill((255, 255, 240))
    
   


      
   
    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    # L - Loop
    while keepGoing:
    # T - Timer to set frame rate
        clock.tick(30)
    # E - Event handling
        for event in pygame.event.get():
               if event.type == pygame.QUIT:
                       keepGoing = False
               


    # R - Refresh display
        shape_colour1(background) 
        time.sleep(0.2)
        screen.blit(background, (0, 0))




        pygame.display.flip()
    # Close the game window
    pygame.quit()
    


def main():
    gameframe()
main()


# In[ ]:





# In[ ]:





# In[ ]:




