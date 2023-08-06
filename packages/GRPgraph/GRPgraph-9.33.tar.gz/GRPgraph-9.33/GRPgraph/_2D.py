
from ctypes import pointer
from symtable import Function
from tracemalloc import start
from wsgiref.util import request_uri
import pygame
from pygame import draw; import pygame.camera

import keyboard
import math
import time
import random


pygame.init()

def Get_CAM_zvt_prost():
        return ['RGB','HSV','YUV']

def Mod(num):
    if num < 0:num = -num
    return num

# 1
class Vector:
    def __init__(self):
        pass

    class Vec2:
        def __init__(self,vect2d_start=[-1],vect2d_end=[-1],pos=[0,0]): 
            if vect2d_start[0]!=-1 and vect2d_end[0]!=-1:
                self.vect2d_start = vect2d_start
                self.vect2d_end = vect2d_end
                self.vec2D = [self.vect2d_start,self.vect2d_end]
                self.x = vect2d_end[0]-vect2d_start[0]
                self.y = vect2d_end[1]-vect2d_start[1]
            else:
                self.x = pos[0]
                self.y = pos[1]
            self.size = int(math.sqrt(self.x**2+self.y**2))
            self.absv = Mod(self.size)
            self.pos1 = [self.x,self.y]

            

        def raV_2D(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            if Mod(parperx_st_) == Mod(parperx_en_) and Mod(parpery_st_) == Mod(parpery_en_):
                return True
            else:
                return False


        def poV_2D(self,ugl):
            pos = [int(self.x*math.cos(ugl)-self.y*math.sin(ugl)),int(self.y*math.cos(ugl)+self.x*math.sin(ugl))]
            vec3 = Vector().Vector2D(pos=pos)
            return vec3




        def suM_2D(self,vector2D):
            pos=[self.x+vector2D.x,self.y+vector2D.y]
            vec3 = Vector().Vector2D(pos=pos)
            return vec3

        def raZ_2D(self,vector2D):
            pos=[self.x-vector2D.x,self.y-vector2D.y]
            vec3 = Vector().Vector2D(pos=pos)
            return vec3

        def umN_2D(self,delta):
            pos=[self.x*delta,self.y*delta]
            vec3 = Vector().Vector2D(pos=pos)
            return vec3
            
        def scaL_2D(self,vector2D):
            scl = self.x*vector2D.x+self.y*vector2D.y
            return scl


        def nuL_2D(self):
            if self.vect2d_end==self.vect2d_start:return True
            else:return False



        def naP_2D(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            
            if parperx_en_ == parperx_st_ and parpery_en_ == parpery_st_ :
                    return True
            else:
                    return False     
# 2
class Surfases:
    def __init__(self,size=[]):
        self.surf = pygame.Surface((size[0],size[1]))
        surf1 = self.surf
        return surf1

    def set_alphal(self,al):
        if al > 255:al=255
        if al < 0:al=0
        self.surf.set_alpha(al)
        
    def draw_surf(self,pos=[]):
        screen.blit(self.surf,(pos[0],pos[1]))

    def draw_on_surf(self,sr1,sr2,pos=[]):
        sr1.blit(sr2,(pos[0],pos[1]))

    def fill_surf(self,col=()):
        self.surf.fill(col)

    class Trans:
        def __init__(self):
            pass
# 3        
class Kamera:
    def __init__(self,size,zvet_prost='RGB',num=0):
        self.size = size
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[num],(size[0],size[1]), zvet_prost)
        self.cam.set_controls(True,False,1)

    def List_cam(self):
        cams = pygame.camera.list_cameras()
        return cams
    
    def Start(self):self.cam.start()

    def End(self):self.cam.stop()

    def Get_img(self):
        img = self.cam.get_image()
        return img

    def Get_size(self):
        width , height = self.cam.get_size()
        return width , height
    
    def Set_setings(self,wflip,hflip,sun):
        self.cam.set_controls(wflip,hflip,sun)

    def Get_setings(self):
        cont = self.cam.get_controls()
        return cont
# 4
class TimeGR:
    def __init__(self):
        pass
    def DELY(self,MLsec):
        time.sleep(MLsec)
# 5 -- new !!
class Text_:
    def __init__(self,screen_size=[],text='',glass=False,col=(),font=None,pix=0,pos=[]):
        pygame.font.init()

        self.win_w = screen_size[0]
        self.win_h = screen_size[1]
        self.text = text
        self.pos = pos
        self.pix = pix
        self.font = font
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.pos = [self.x,self.y]
        self.glass = glass
        self.col = col
        textt = pygame.font.SysFont(self.font,self.pix)
        texttt = textt.render(self.text,self.glass,self.col)
        screen1 = pygame.display.set_mode((self.win_w,self.win_h))
        self.init_text = textt
        self.texttt = texttt   
        self.screen1 = screen1
    def Render(self): 
        screen.blit(self.texttt,(self.x,self.y))
    def Set_text(self,text=''):
        self.text = text
    def Set_pos(self,pos=[]):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]  
    def Set_col(self,col):
        self.col = col
    def Get_col(self):
        return self.col
    def Set_bg(self,col=(0,0,0)):
        bg = Screen_.draw2D.Rect(col,[self.x,self.y],[len(self.text)*12.5+len(self.text)+len(self.text),self.pix+10],0,self.screen1)
        bg.Draw()
        screen.blit(self.texttt,(self.x,self.y))      
# 6
class GPMath:
    def __init__(self):
        pass
    def COS(self,ugl):
        return math.cos(ugl)
    def SIN(self,ugl):
        return math.sin(ugl)
    
    def RAST(self,pos1=[],pos2=[]):
        if pos1[0]>pos2[0]:w = pos1[0]-pos2[0]
        else:              w = pos2[0]-pos1[0]
        if pos1[1]>pos2[1]:h = pos1[1]-pos2[1]
        else:              h = pos2[1]-pos1[1]
        dl = math.sqrt(w*w+h*h)
        return dl
        
    def RAST_CENT(self,rect1 = [],rect2 = []):
        if rect1[4][0]>rect2[4][0]:w = rect1[4][0]-rect2[4][0]
        else:              w = rect2[4][0]-rect1[4][0]
        if rect1[4][1]>rect2[4][1]:h = rect1[4][1]-rect2[4][1]
        else:              h = rect2[4][1]-rect1[4][1]
        dl = math.sqrt(w*w+h*h)
        return dl

    class RandomGR:
                                    def __init__():
                                        pass   
                                    def GET_randint(nume = 1,stn = 1 ,endn = 1):
                                        num = []
                                        for i in range(nume):num.append(random.randint(stn,endn));return num

                                    def GET_random():
                                        num = random.random();return num  
# 7 -- new !!
class Color:
    def __init__(self,r,g,b,hsv=0):
        
        self.hsv = hsv
        self.r = r
        self.b = b
        self.g = g
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)
    def Set_hsv(self,hsv):

        self.hsv = hsv
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)
        return self.color
    def Color_mesh(self,color,mesh=0.5):
        hsv = (self.hsv + color.hsv)/mesh
        r = (self.r + color.r)/mesh
        g = (self.g + color.g)/mesh
        b = (self.b + color.b)/mesh
        col = Color(r,g,b,hsv)
        return col      
# 8 -- new !!
class Sub:
    def __init__(self):
        pass
    class Bord:
        def __init__(self):
            pass
        def On_key_press(self,key):
            on = keyboard.is_pressed(key)
            return on
        def Key_function(self,key,function):
            if True==keyboard.is_pressed(key):
                function()
    class Mouse:
        def __init__(self):
            pass
        def Get_Pos(self):
            pos = pygame.mouse.get_pos();  return pos
        def Get_pres(self,but=""):
            pr = pygame.mouse.get_pressed()
            if but == "l":  return pr[0]
            elif but == "r":  return pr[2]
            elif but == "m":  return pr[1]
        def Pres_function(self,button,function):
            pr = pygame.mouse.get_pressed()
            if button == "l" and pr[0] == True:  
                function()
            elif button == "r" and pr[2] == True:  
                function()
            elif button == "m" and pr[1] == True:  
                function()
        def Set_viz(self,viz):
            pygame.mouse.set_visible(viz)
        def Get_viz(self):
            viz = pygame.mouse.get_visible()
            return viz
        def Set_pos(self,pos=[]):
            pygame.mouse.set_pos([pos[0],pos[1]])
# 19 -- new !!
class Screen_:
    def __init__(self,size=[],caption='Program'):
        global screen,clock


        self.win_size = size
        self.win_w = self.win_size[0]
        self.win_h = self.win_size[1]
        self.caption = caption

        pygame.init()
        pygame.display.init()
        
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.win_w,self.win_h))
        pygame.display.set_caption(self.caption)

        self.clock = clock
        self.screen = screen
    def set_alpha(self,alp):
        screen.set_alpha(alp)
    def get_color(self,x,y):
        col = screen.get_at([x,y])
        col1 = [col[0],col[1],col[2]]
        return col1
    def get_center(self):
        xc = self.win_w/2
        yc = self.win_h/2
        return xc , yc
    def set_fps(self,fps):
        if fps == "MAX":fps = 1000
        if fps == "MIN":fps = 30
        self.clock.tick(fps)
    def get_fps(self):return int(self.clock.get_fps())
    def close(self,running=True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        return running 
    class Update:
        def __init__(self):
            pygame.display.flip()
        def BG_col(self,col= (0,0,0)):
            screen.fill(col)
    class draw2D:
                                            def __init__(self):
                                                pass
                                            class Rect:
                                                def __init__(self,col=(),pos=[],size=[],sh=0,surf=0):
                                                    sh2 = 1
                                                    center =  [pos[0] + size[0]/2,pos[1]+size[1]/2]
                                                    pos1=[pos[0],pos[1]]
                                                    size1=[size[0],size[1]]
                                                    rectt = [pos1,size1,center,col,sh]
                                                    self.pos1 = pos
                                                    self.size1 = size
                                                    self.surf = surf
                                                    self.col = col
                                                    self.sh = sh
                                                    self.sh2 = sh2
                                                    self.rectt = rectt        
                                                    self.center = center                                          
                                                def Draw(self):
                                                    rect = pygame.Rect(self.pos1[0],self.pos1[1],self.size1[0],self.size1[1])
                                                    self.rect = rect
                                                    pygame.draw.rect(
                                                        self.surf, 
                                                        self.col, 
                                                        self.rect,
                                                        self.sh
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos1[0],self.pos1[1],self.size1[0],self.size1[1])
                                                    self.rect = rect
                                                    pygame.draw.rect(
                                                        self.surf, 
                                                        self.col, 
                                                        self.rect,
                                                        self.sh
                                                    )
                                                    rect1 = pygame.Rect(self.pos1[0],self.pos1[1],self.size1[0],self.size1[1])
                                                    pygame.draw.rect(
                                                        self.surf,
                                                        col,
                                                        rect1,
                                                        self.sh2
                                                    )                                               
                                                def Obv(self,col=(0,0,0)):
                                                    rect1 = pygame.Rect(self.pos1[0],self.pos1[1],self.size1[0],self.size1[1])
                                                    pygame.draw.rect(
                                                        self.surf,
                                                        col,
                                                        rect1,
                                                        self.sh2
                                                    )
                                                def Set_size(self,size2=[]):
                                                    self.size1 = size2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Set_col(self,col2=()):
                                                    self.col = col2
                                                def Get_size(self):
                                                    return self.size1
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_sh2(self,sh2):
                                                    self.sh2=sh2
                                                def Fyg(self):
                                                    return self.rectt
                                                def Get_center(self):
                                                    return self.center
                                                def Get_surf(self):
                                                    return self.surf
                                                def Get_sh2(self):
                                                    return self.sh2


                                            class Circle:
                                                def __init__(self,col=(),pos=[],rad=0,sh=0,surf=0):
                                                    center = [pos[0],pos[1]]
                                                    sh2 = 1
                                                    pos1=[pos[0],pos[1]]
                                                    rectt = [pos1,rad,center,col,sh]
                                                    self.sh2 = sh2
                                                    self.col = col
                                                    self.sh = sh
                                                    self.rad = rad
                                                    self.surf = surf
                                                    self.pos1 = [pos[0],pos[1]]
                                                    self.center = [pos[0],pos[1]]
                                                    self.rectt = rectt
                                                    self.pos = pos
                                                def Draw(self):
                                                    pygame.draw.circle (
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh
                                                    )               
                                                def Obv(self,col=(0,0,0)):
                                                    pygame.draw.circle(
                                                        self.surf,
                                                        col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    pygame.draw.circle (
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh
                                                    )
                                                    pygame.draw.circle(
                                                        self.surf,
                                                        col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh2
                                                    )          
                                                def Set_rad(self,rad2):
                                                    self.rad = rad2
                                                def Set_col(self,col2=()):
                                                    self.col = col2
                                                def Get_rad(self):
                                                    return self.rad
                                                def Get_sh(self):
                                                    return self.sh
                                                def Fyg(self):
                                                    return self.rectt
                                                def Get_center(self):
                                                    return self.center
                                                def Get_surf(self):
                                                    return self.surf
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_sh(self,sh2):
                                                    self.sh=sh2
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Get_sh(self):
                                                    return self.sh


                                            class Ellips:
                                                def __init__(self,col=(),pos=[],size=[],sh=0,surf=0):
                                                    center =  [pos[0] + size[0]/2,pos[1]+size[1]/2]
                                                    poses=[pos[0],pos[1]]
                                                    size=[size[0],size[1]]
                                                    sh2 = 1
                                                    rectt = [poses,size,center,col,sh]
                                                    self.sh2 = sh2
                                                    self.center = center
                                                    self.poses = poses
                                                    self.size = size
                                                    self.rectt = rectt
                                                    self.col = col
                                                    self.pos = pos
                                                    self.sh = sh
                                                    self.surf = surf
                                                def Draw(self):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(
                                                        self.surf,
                                                        self.col,
                                                        self.rect,
                                                        self.sh
                                                    )
                                                def Obv(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(
                                                        self.surf,
                                                        self.col,
                                                        self.rect,
                                                        self.sh
                                                    )
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )
                                                def Set_size(self,size=[]):
                                                    self.size = size
                                                def Get_center(self):
                                                    return self.center
                                                def Get_sh(self):
                                                    return self.sh
                                                def Fyg(self):
                                                    return self.rectt
                                                def Get_surf(self):
                                                    return self.surf
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Get_size(self):
                                                    return self.size
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2


                                            class Tringl:
                                                def __init__(self,col=(),pos1=[],pos2=[],pos3=[],sh=0,surf=0):  
                                                    rectt = [pos1,pos2,pos3,col,sh]
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.col = col
                                                    self.pos1 = pos1
                                                    self.pos2 = pos2
                                                    self.pos3 = pos3
                                                    self.poses = [self.pos1,self.pos2,self.pos3]
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.rectt = rectt
                                                def Draw(self):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )
                                                def Obv(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.pos1 = poses[0]
                                                    self.pos2 = poses[1]
                                                    self.pos3 = poses[2]
                                                def Set_pos1(self,pos1=[]):
                                                    self.pos1 = pos1
                                                def Set_pos2(self,pos2=[]):
                                                    self.pos2 = pos2
                                                def Set_pos3(self,pos3=[]):
                                                    self.pos3 = pos3


                                            class Line:
                                                def __init__(self,col=(),start_pos=[],end_pos=[],sh=1,surf=0):
                                                    xcnt = start_pos[0]+(end_pos[0]-start_pos[0])/2;ycnt = start_pos[1]+(end_pos[1]-start_pos[1])/2
                                                    center = [xcnt,ycnt]
                                                    rectt = [start_pos,end_pos,center,col,sh]
                                                    self.x_center = xcnt
                                                    self.y_center = ycnt
                                                    self.center = center
                                                    self.rectt = rectt
                                                    self.col = col
                                                    self.start_pos = start_pos
                                                    self.end_pos = end_pos
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.poses = [self.start_pos,self.end_pos]
                                                def Draw(self):
                                                    pygame.draw.line( 
                                                        self.surf,
                                                        self.col,
                                                        (self.start_pos[0],self.start_pos[1]),
                                                        (self.end_pos[0],self.end_pos[1]),
                                                        self.sh
                                                    )
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.start_pos = poses[0]
                                                    self.end_pos = poses[1]
                                                def Set_start_pos(self,pos=[]):
                                                    self.start_pos = pos
                                                def Set_end_pos(self,pos=[]):
                                                    self.end_pos = pos
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Get_col(self):
                                                    return self.col
                                                def Get_poses(self):
                                                    return self.poses
                                                def Get_start_pos(self):
                                                    return self.start_pos
                                                def Get_end_pos(self):
                                                    return self.end_pos


                                            class Liness:
                                                def __init__(self,col=(),points=(),snap=False,sh=1,surf=0):
                                                    rectt = [points,col,snap,sh]

                                                    self.col = col
                                                    self.points = points
                                                    self.snap = snap
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.rectt = rectt  
                                                def Draw(self):
                                                    pygame.draw.lines( 
                                                        self.surf,
                                                        self.col,
                                                        self.snap,
                                                        self.points,
                                                        self.sh
                                                    )
                                                def Get_points_ind(self,index=0,cor=None):
                                                    if cor == None:
                                                        return self.points[index]
                                                    elif cor == "x" or cor == "X":
                                                        return self.points[index][0]
                                                    elif cor == "y" or cor == "Y":
                                                        return self.points[index][1]
                                                def Get_points(self):
                                                    return self.points
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_snap(self):
                                                    return self.snap
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2


                                            class Pixel:
                                                def __init__(self,col=(),pos=[],sh=1,surf=0):   
                                                    rectt = [pos,col,sh]
                                                    
                                                    self.rectt = rectt
                                                    self.pos = pos
                                                    self.col = col
                                                    self.sh = sh
                                                    self.surf = surf
                                                def Draw(self):
                                                    pygame.draw.line(   
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        (self.pos[0],self.pos[1]),
                                                        self.sh
                                                    )
                                                def Get_pos(self):
                                                    return self.pos
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_pos(self,pos=[]):
                                                    self.pos = pos
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2


                                            class Arc:
                                                def __init__(self,col=(),pos=[],start_angle=0,stop_angle=0,rad=1,sh=1,st='-',surf=0):
                                                    grad = 56.5
                                                    ugl1 = start_angle/grad
                                                    rectt=[pos,start_angle,stop_angle,col,sh,st]

                                                    self.grad = grad
                                                    self.ugl = ugl1
                                                    self.start_angl = start_angle
                                                    self.end_angl = stop_angle
                                                    self.col = col
                                                    self.pos = pos
                                                    self.rad = rad
                                                    self.sh = sh
                                                    self.st = st
                                                    self.surf = surf
                                                    self.rectt = rectt                                                   
                                                def Draw(self):
                                                    
                                                    for l in range(int(self.end_angl*3.5)):
                                                        if self.st=='-': self.ugl+=0.005
                                                        elif self.st=='+': self.ugl-=0.005
                                                        for i in range(0,self.rad,2): 
                                                            xl=self.pos[0]+i*math.sin(self.ugl);yl=self.pos[1]+i*math.cos(self.ugl)
                                                            if i == self.rad - self.sh:
                                                                xpos = xl;ypos = yl
                                                        pygame.draw.line(self.surf,
                                                                        self.col,
                                                                        [xl,yl],
                                                                        [xpos,ypos],
                                                                        5)     
                                                def Set_end_ugl(self,ugl):
                                                    self.end_angl = ugl       
                                                def Set_start_ugl(self,ugl):
                                                    self.start_angl = ugl
                                                def Set_st(self,st='-'):
                                                    self.st = st     
                                                def Get_st(self):
                                                    return self.st
                                                def Get_col(self):
                                                    return self.col
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_rad(self,rad):
                                                    self.rad = rad
                                                def Get_rad(self):
                                                    return self.rad
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Get_sh(self):
                                                    return self.sh
# 10
class IMG:
    def __init__(self):
        pass
    def loadIMG(self,file=''):
        imgg = pygame.image.load(file)
        return imgg

    def DrawIMG(self,pos=[],iimmgg=0):
        rect = iimmgg.get_rect(bottomright=(pos[0]+iimmgg.get_width(),
                                            pos[1]+iimmgg.get_height())) 
        screen.blit(iimmgg,rect)
        return rect

    def IMGScale(self,pov,width,height):
        tid = pygame.transform.scale(pov,(width,height))
        return tid
    
    def Save_img(self,pov,file_name=''):
        pygame.image.save(pov,file_name)
# 11
class Graphick:
    def __init__(self):
        pass
    def SETcirclGRAPH(self,col=[],znh=[]):
        pit = [col,znh]
        return pit
    def DRcirclGRAPH_2D(self,r=1,xp=1,yp=1,grph=[]):
        kf = 0
        ugl = 1;ugl1=1
        c=r
        g1 = 0
        for g in range(len(grph[0])):
            kf = kf + grph[0][g]

        for g in range(len(grph[1])):
            coll = grph[1][g]
            ugl = ugl1
            for n in range(int(700/kf*grph[0][g1])):
                xl = xp + c * math.sin(ugl)
                yl = yp + c * math.cos(ugl)
                ugl+=0.009
                pygame.draw.line(screen,coll,(xp,yp),(xl,yl),4)
                ugl1 = ugl


            g1 +=1