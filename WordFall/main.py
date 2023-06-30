import random
import pygame
import Class.add_word as wd
from pathlib import Path
from tkinter import *
import tkinter.font
from multiprocessing import Process

#load_word 사용법 0: 기본 위치 1: TOEIC 2: User 3: 추가할 것 받아오는 거임..!!
#word = wd.load_word(data_path(1))
#wd.append(data_path(2), data_path(3))

pygame.init()

#화면크기
screen_width = 1440
screen_hight = 900
screen = pygame.display.set_mode((screen_width, screen_hight))

#화면 타이틀
pygame.display.set_caption("WordFall")

#FPS
clock = pygame.time.Clock()

global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j
mvol = 5
bvol = 5
music_volume = list(map(float, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]))
button_volume = list(map(float, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]))
i = 53
j = 53
stop = 0
e = 'o'

pygame.mixer.init()

main_music = pygame.mixer.Sound("st/main.wav")
button_sound = pygame.mixer.Sound("st/button.wav")

main_music.set_volume(0.5)
button_sound.set_volume(0.5)
main_music.play(-1)

class sc:
    class Character:
        def setdata(self, image):
            self.image = pygame.image.load(image)
            self.size = self.image.get_rect().size
            self.width = self.size[0]
            self.height = self.size[1]
        def setlength(self, x_pos, y_pos):
            self.x_pos = x_pos
            self.y_pos = y_pos
        pass
           
    dt = clock.tick(60)
    def __init__(self, name):
        self.screen_name = name
        self.frame = 120
        pass

    def bgimg(self, image):
        self.backgound = pygame.image.load(image)
    pass

class word:
    def __init__(self, r):
        r = r.strip()
        self.eng = r.split()[0]
        self.kor = r.split()[1]
        self.y_pos = 0

def help_screen():
    
    global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j

    help = sc("help_screen")
    help.bgimg("st/b.png")
    
    helpb = help.Character()
    helpb.setdata("st/help.png")
    helpb.setlength(screen_width/2-helpb.width/2, helpb.height/2)
    
    back = help.Character()
    back.setdata("st/back.png")
    back.setlength(back.width/2, back.height/2)
    
    contents = help.Character()
    contents.setdata("st/contents.png")
    contents.setlength(screen_width/2-contents.width/2, screen_hight/2-contents.height/2+helpb.height)
    
    running = True
    while running:
        if e == 'exit':
            running = False
        dt = clock.tick(help.frame)
        back_rect = back.image.get_rect()
        back_rect.left = back.x_pos
        back_rect.top = back.y_pos

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            e = 'exit'
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if back_rect.collidepoint(event.pos):
                button_sound.play()
                running = False
                            
        screen.blit(help.backgound, (0, 0))
        screen.blit(helpb.image, (helpb.x_pos, helpb.y_pos))
        screen.blit(back.image, (back.x_pos, back.y_pos))
        screen.blit(contents.image, (contents.x_pos, contents.y_pos))
        pygame.display.update()

        
def main_screen():
    
    global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j

    main = sc("main_screen")
    main.bgimg("st/bt.png")
    
    setting = main.Character()
    setting.setdata("st/setting.png")
    setting.setlength(screen_width-setting.width-20, 20)
    
    title = main.Character()
    title.setdata("st/title.png")
    title.setlength(screen_width/2-title.width/2, title.height/2-12)
    
    button1 = main.Character()
    button1.setdata("st/b1.png")
    button1.setlength(screen_width/2-button1.width/2, screen_hight/2-button1.height*2+7)
    
    button2 = main.Character()
    button2.setdata("st/b2.png")
    button2.setlength(screen_width/2-button2.width/2, screen_hight/2+button2.height/2+20)
    
    button3 = main.Character()
    button3.setdata("st/b3.png")
    button3.setlength(screen_width/2-button3.width/2, button2.y_pos+(button2.y_pos-button1.y_pos))
    
    running = True
    while running:
        if e == 'exit':
            running = False
        dt = clock.tick(main.frame)
        
        setting_rect = setting.image.get_rect()
        setting_rect.left = setting.x_pos
        setting_rect.top = setting.y_pos
        
        button1_rect = button1.image.get_rect()
        button1_rect.left = button1.x_pos
        button1_rect.top = button1.y_pos
        button2_rect = button2.image.get_rect()
        button2_rect.left = button2.x_pos
        button2_rect.top = button2.y_pos
        button3_rect = button3.image.get_rect()
        button3_rect.left = button3.x_pos
        button3_rect.top = button3.y_pos

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            e = 'exit'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                setting_screen(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if setting_rect.collidepoint(event.pos):
                setting_screen(0)
            
            elif button1_rect.collidepoint(event.pos):
                button_sound.play()
                start_screen()
            elif button2_rect.collidepoint(event.pos):
                button_sound.play()
                wd.Input_word(wd.data_path(3))
                wd.append(wd.data_path(2), wd.data_path(3))
                pass
            elif button3_rect.collidepoint(event.pos):
                button_sound.play()
                print(button_sound.get_volume())
                help_screen()
    
        screen.blit(main.backgound, (0, -1100))
        screen.blit(title.image, (title.x_pos, title.y_pos))
        screen.blit(setting.image, (setting.x_pos, setting.y_pos))
        screen.blit(button1.image, (button1.x_pos, button1.y_pos))
        screen.blit(button2.image, (button2.x_pos, button2.y_pos))
        screen.blit(button3.image, (button3.x_pos, button3.y_pos))
        pygame.display.update() #게임화면을 다시 그리기

def start_screen():

    global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j

    main_music.stop()
    main_music = pygame.mixer.Sound("st/start.wav")
    main_music.set_volume(music_volume[mvol])
    main_music.play(-1)
    start = sc("start_screen")
    start.bgimg("st/bt.png")
    background_y_pos = -1100
    speed = 10
    gb = start.Character()
    gb.setdata("st/gb.png")
    gb.setlength(screen_width/2-gb.width/2, screen_hight/2-gb.height/2)

    running = True
    while running:
        if e == 'exit':
            running = False
        dt = clock.tick(start.frame)

        gb_rect = gb.image.get_rect()
        gb_rect.left = gb.x_pos
        gb_rect.top = gb.y_pos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                e = 'exit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gb_rect.collidepoint(event.pos):
                    start_g()
        

        background_y_pos+=speed
        if background_y_pos>=0:
            speed = 0

        screen.blit(start.backgound, (0, background_y_pos))
        if speed == 0: screen.blit(gb.image, (gb.x_pos, gb.y_pos))
        
        pygame.display.update()
    
    

def start_g():
    global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j

    start_game = sc("start_g")
    start_game.bgimg("st/bt.png")

    f = open("data/TOEIC.txt", 'r')
    lines = f.readlines()
    f.close()
    print(lines)
    words = [0] * 9
    texts = [0] * 9
    text_x = [0] * 9
    #lines = random.shuffle(lines)
    #lines = random.shuffle(lines)
    #lines = random.shuffle(lines)

    words[0] = word(lines[0])
    words[1] = word(lines[1])
    words[2] = word(lines[2])
    words[0].y_pos=-400
    words[2].y_pos=-200
    
    text_color = (255, 255, 255)
    text_size = 30
    font = pygame.font.SysFont("휴먼둥근헤드라인", text_size, True, True)
    texts[0] = font.render(words[0].eng, True, text_color)
    texts[1] = font.render(words[1].eng, True, text_color)
    texts[2] = font.render(words[2].eng, True, text_color)
    
    text_x[0] = random.randrange(0, screen_width-text_size)
    text_x[1] = random.randrange(0, screen_width-text_size)
    text_x[2] = random.randrange(0, screen_width-text_size)

    x=2
    z=2
    start_ticks = pygame.time.get_ticks()
    
    running = True
    while running:
        if e == 'exit' or stop == 1:
            if stop == 1:
                main_music.stop()
                main_music = pygame.mixer.Sound("st/main.wav")
                main_music.set_volume(music_volume[mvol])
                main_music.play(-1)
                stop = 0
            running = False
        dt = clock.tick(start_game.frame)
        elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000
        
        #수정(몇개 맞으면 늘어나는걸로)
        if int(elapsed_time)%20==0 and elapsed_time>=20 and x<8:
            print(111111111111111111111111111111111111111111111111)
            x+=1
            z+=1
            words[x] = word(lines[z])
            texts[x] = font.render(words[x].eng, True, text_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                e = 'exit'
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setting_screen(1)
        
        words[0].y_pos+=1
        words[1].y_pos+=1
        words[2].y_pos+=1
        if x>2: words[3].y_pos+=1
        if x>3: words[4].y_pos+=1
        if x>4: words[5].y_pos+=1
        if x>5: words[6].y_pos+=1
        if x>6: words[7].y_pos+=1
        if x>7: words[8].y_pos+=1
        print(elapsed_time)
        print("i:{}".format(x))
        
        #수정(선에 충돌했을때 또는 맞췄을때로 if문 조건 바꾸기)
        for h in range(0, x+1):
            if words[h].y_pos==screen_width:
                print("e:{}".format(h))
                print("j:{}".format(z))
                words[h].y_pos == 0
                z+=1
                words[h] = word(lines[z])
                texts[h] = font.render(words[h].eng, True, text_color)
                text_x[h] = random.randrange(0, screen_width-text_size)
        
        screen.blit(start_game.backgound, (0, 0))
        screen.blit(texts[0], (text_x[0], words[0].y_pos))
        screen.blit(texts[1], (text_x[1], words[1].y_pos))
        screen.blit(texts[2], (text_x[2], words[2].y_pos))
        if x>2: screen.blit(texts[3], (text_x[3], words[3].y_pos))
        if x>3: screen.blit(texts[4], (text_x[4], words[4].y_pos))
        if x>4: screen.blit(texts[5], (text_x[5], words[5].y_pos))
        if x>5: screen.blit(texts[6], (text_x[6], words[6].y_pos))
        if x>6: screen.blit(texts[7], (text_x[7], words[7].y_pos))
        if x>7: screen.blit(texts[8], (text_x[8], words[8].y_pos))
        pygame.display.update()

def tk():
    root = Tk()
    root.title("Word")
    root.geometry("471x80+300+100") #가로 * 세로 + x좌표 + y좌표
    root.resizable(False, False) #창크기 변경불가
    font = tkinter.font.Font(size=50, weight="bold")
    txt = Text(root, width=471, height=80, font=font)
    txt.pack()
    def re(n):
        enter_word = txt.get("1.0", END)
        txt.delete("1.0", "end")
    root.bind("<Return>", re)
    root.mainloop()

def setting_screen(w):

    global e, main_music, button_sound, stop, mvol, bvol, music_volume, button_volume, i, j
    
    text_color = (255, 255, 255)
    font = pygame.font.SysFont("휴먼둥근헤드라인", 40, True, True)
    text1 = font.render(chr(i) if i != 58 else "10", True, text_color)
    text2 = font.render(chr(j) if j != 58 else "10", True, text_color)
    
    # 0:main 1:start 2:addwords 3:help
    setting = sc("setting_screen")
    if w==0: setting.bgimg("st/msb.png")
    elif w==1: setting.bgimg("st/ssb.png")
    
    set = setting.Character()
    set.setdata("st/set.png")
    set.setlength(screen_width/2-set.width/2, screen_hight/2-set.height/2)
    
    end = setting.Character()
    end.setdata("st/end.png")
    end.setlength(screen_width/2-end.width/2, set.y_pos+set.height-end.height-205)
    
    end2 = setting.Character()
    end2.setdata("st/end2.png")
    end2.setlength(screen_width/2-end2.width/2, set.y_pos+set.height-end2.height-55)
    
    arrm = setting.Character()
    arrm.setdata("st/arrow.png")
    arrm.setlength(screen_width/2+arrm.width, set.height/4+42)
    
    arrs = setting.Character()
    arrs.setdata("st/arrow.png")
    arrs.setlength(screen_width/2+arrs.width, set.height/2+42)
    
    arrm2 = setting.Character()
    arrm2.setdata("st/arrow2.png")
    arrm2.setlength(screen_width-set.width/2-100, set.height/4+42)
    
    arrs2 = setting.Character()
    arrs2.setdata("st/arrow2.png")
    arrs2.setlength(screen_width-set.width/2-100, set.height/2+42)
    
    running = True
    while running:
        if e == 'exit':
            running = False
        
        text1 = font.render(chr(i) if i != 58 else "10", True, text_color)
        text2 = font.render(chr(j) if j != 58 else "10", True, text_color)
    
        end_rect = end.image.get_rect()
        end_rect.left = end.x_pos
        end_rect.top = end.y_pos
        
        end2_rect = end2.image.get_rect()
        end2_rect.left = end2.x_pos
        end2_rect.top = end2.y_pos
        
        arrm_rect = arrm.image.get_rect()
        arrm_rect.left = arrm.x_pos
        arrm_rect.top = arrm.y_pos
        
        arrm2_rect = arrm2.image.get_rect()
        arrm2_rect.left = arrm2.x_pos
        arrm2_rect.top = arrm2.y_pos

        arrs_rect = arrs.image.get_rect()
        arrs_rect.left = arrs.x_pos
        arrs_rect.top = arrs.y_pos

        arrs2_rect = arrs2.image.get_rect()
        arrs2_rect.left = arrs2.x_pos
        arrs2_rect.top = arrs2.y_pos

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            e = 'exit'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if arrm_rect.collidepoint(event.pos) and mvol>0:
                button_sound.play()
                mvol -= 1
                i-=1
                main_music.set_volume(music_volume[mvol])
            elif arrm2_rect.collidepoint(event.pos) and mvol<10:
                button_sound.play()
                mvol += 1
                i+=1
                main_music.set_volume(music_volume[mvol])
            elif arrs_rect.collidepoint(event.pos) and bvol>0:
                button_sound.play()
                bvol -= 1
                j-=1
                button_sound.set_volume(button_volume[bvol])
            elif arrs2_rect.collidepoint(event.pos) and bvol<10:
                button_sound.play()
                bvol += 1
                j+=1
                button_sound.set_volume(button_volume[bvol])
            elif end_rect.collidepoint(event.pos) and w == 1:
                button_sound.play()
                stop = 1
                running = False
            elif end_rect.collidepoint(event.pos):
                button_sound.play()
                running = False
            elif end2_rect.collidepoint(event.pos):
                button_sound.play()
                e = 'exit'
        if w==0: screen.blit(setting.backgound, (0, -1100))
        elif w==1: screen.blit(setting.backgound, (0, 0))
        
        screen.blit(set.image, (set.x_pos, set.y_pos))
        screen.blit(end.image, (end.x_pos, end.y_pos))
        screen.blit(end2.image, (end2.x_pos, end2.y_pos))
        screen.blit(arrm.image, (arrm.x_pos, arrm.y_pos))
        screen.blit(arrs.image, (arrs.x_pos, arrs.y_pos))
        screen.blit(arrm2.image, (arrm2.x_pos, arrm2.y_pos))
        screen.blit(arrs2.image, (arrs2.x_pos, arrs2.y_pos))
        screen.blit(text1, ((arrm2.x_pos+arrm2.width)+(arrm.x_pos-(arrm2.x_pos+arrm2.width))/2-14, arrm.y_pos))
        screen.blit(text2, ((arrm2.x_pos+arrm2.width)+(arrm.x_pos-(arrm2.x_pos+arrm2.width))/2-14, arrs.y_pos))
        pygame.display.update()
  
#def add_word():

if __name__ == "__main__":
    main_screen()
