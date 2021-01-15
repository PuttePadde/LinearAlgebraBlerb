
################################################
#                                              # 
#       !!!!!!!!!RETROLINEAR!!!!!!!!!!!        #
#                                              #
#       MATH BLERB BY PETER BOYE HANSEN.       # 
#    PURPOSE OF THIS CODE IS TO UNDERSTAND     # 
#               BASIC ALGEBRA.                 #
#                                              #
#    THE FORMULAR ADRESSED IN THIS CODE IS:    #
#""""""""""""""""""""""""""""""""""""""""""""""#
#                                              #
#                 F(X)=AX+B                    #
#                                              #         
#""""""""""""""""""""""""""""""""""""""""""""""#        
#  COPYRIGHT: WHO CARES, AS LONG AS PPL LEARN  #                          
################################################

# For graphical output, this code is dependent on the Pyxel Framework.

import pyxel
import time
import random

class App:
    def __init__(self):
        pyxel.init(255, 255,fullscreen=True)
        self.x = 100
        self.y = 0
        self.a = 1
        self.b = 30
        self.negative = 20
        pyxel.run(self.update, self.draw)
    
    def handle_input(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.b += 1
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.b -= 1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.a -= 0.1
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.a += 0.1
        elif pyxel.btn(pyxel.KEY_W):
            self.x += 1
        elif pyxel.btn(pyxel.KEY_S):
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_A):
            self.negative -= 1
        elif pyxel.btn(pyxel.KEY_D):
            self.negative += 1

    def update(self):
        self.handle_input()      

    def draw(self):
        pyxel.cls(0)
        self.draw_math()
        self.draw_line()
       

    def draw_line(self):
        pyxel.text(69-49, 128-5, "f(X)=AX+B" , 12)
        self.draw_axis()
        for x in range(0-self.negative, self.x):    
            self.y = ((self.a)*x) + self.b
            pyxel.pset(69+x, 255-self.y-128, random.randrange(1,4))   
            
        pyxel.text(69+x, 255-self.y-128, str(int(255-self.y-256)), 5)

    def draw_axis(self):
        pyxel.line(69, 20, 69, 200,9)
        pyxel.text(68, 10, "Y" , 3)
        pyxel.line(235, 128, 20, 128,3)
        pyxel.text(240, 126, "X" , 3)        
    
    def draw_math(self):
        pyxel.text(16,228, "X: " + str(self.x) , 15)
        pyxel.text(64,228, "A: " + str(round(self.a*10)) , 15)
        pyxel.text(128,228, "B: " + str(self.b+1) , 15)
       
App()
