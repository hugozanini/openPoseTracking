#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Input import Input
from Scene import Scene
import sys
import getopt
import Constants
import pygame
import cv2

class Twister():
# Define uma janela onde os videos serao colocados como input
# Verificar se ele usa o opencv para fazer isso
    def __init__(self):
        self.input = Input()
        pygame.init()
    #    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    #    pygame.display.set_caption("Twister!")
    #    screen = pygame.display.get_surface()
    #    self.scene = Scene(screen, self.input)

    def run(self):
        
        while True:
            # Aqui no input.run() que o algoritmo começa a funcionar de verdade
            self.input.run()

            # Aqui eu renderizo o resultado da cena
            self.scene.run()

    def run_local(self):
        # Opens the Video file
        cap = cv2.VideoCapture('./data/input/v1_small.mp4')

        # Abrindo o video e passando cada frame como parametro
        frames_array = []
        get_par = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break



            # Getting video parameters
            if get_par == 0:
                height, width, layers = frame.shape
                size = (width,height)
                get_par = 1

            self.input.run_local(ret, frame, frames_array)
            if ret == False:
                break
        
        # Saving all frames as a video
        out = cv2.VideoWriter('./data/output/result_small.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
        for i in range(len(frames_array)):
            out.write(frames_array[i])
        out.release()
        

if __name__ == "__main__":
    options, remainder = getopt.getopt(sys.argv[1:], 's:x:')
    for opt, arg in options:
        if opt in ('-s'):
            song = arg
        elif opt in ('-x'):
            speed = float(arg)
    game = Twister()
    #game.run()
    game.run_local()
