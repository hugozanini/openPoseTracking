#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Input import Input
from Scene import Scene
import sys
import getopt
import Constants
import pygame
import cv2
import progressbar

# Hidding Deprecation Warnings 
#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning) 

class PoseTracking():
    def __init__(self, mode):
        if mode == 'local' or mode == 'Local' or mode =='LOCAL':
            print("Running in a local video...")
            self.input = Input()
            self.mode = 1

        elif mode == 'reatime' or mode == 'RealTime' or mode =='realTime' or mode =='Realtime' or mode =='REALTIME':
            self.input = Input()
            pygame.init()
            pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
            pygame.display.set_caption("PoseTracking!")
            screen = pygame.display.get_surface()
            self.scene = Scene(screen, self.input)
            self.mode = 0

    def run(self):
        
        while True:
            # To run the algorithm
            self.input.run()

            # Showing the scene
            self.scene.run()

    def run_local(self, data_input, data_output, speed = 30):
        # Opens the Video file
        cap = cv2.VideoCapture('./data/input/v1basq_crp.mp4')

        # Abrindo o video e passando cada frame como parametro
        frames_array = []
        get_par = 0
        while(cap.isOpened()):
            ret, frame = cap.read()

            # Getting video parameters
            if get_par == 0:
                height, width, layers = frame.shape
                size = (width,height)
                get_par = 1

            self.input.run_local(ret, frame, frames_array)
            if ret == False:
                break
        
        # Saving all frames as a video
        out = cv2.VideoWriter(data_output,cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
        for i in range(len(frames_array)):
            out.write(frames_array[i])
        out.release()

      
'''
Arguments
[-i] -> Data input folder
[-o] -> Data output folder
[-m] -> Mode: local or realtime
[-x] -> Speed (fps)

'''
if __name__ == "__main__":
    options, remainder = getopt.getopt(sys.argv[1:], 'm:x:i:o')
    for opt, arg in options:
        if opt in ('-m'):
            mode = str(arg)
        elif opt in ('-x'):
            speed = int(arg)
        elif opt in ('-i'):
            data_input = str(arg)
        elif opt in ('-o'):
            data_output = str(arg)

    data_output = './data/output/test_new.avi'
    data_input = './data/input/v1basq_crp.mp4'
    print("Input: ", data_input)
    print("Output: ", data_output)
    
    running_mode = PoseTracking(mode)
    
    # Running in a local video
    if running_mode.mode == 1:
        running_mode.run_local(data_input, data_output, speed)
    
    # Running realtime
    elif running_mode.mode == 0:
        running_mode.run()
    
    else:
        print("Please select a running mode: local or realtime")


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from Input import Input
# from Scene import Scene
# import sys
# import getopt
# import Constants
# import pygame

# class Twister():
# # Define uma janela onde os videos serao colocados como input
# # Verificar se ele usa o opencv para fazer isso
#     def __init__(self):
#         self.input = Input()
#         pygame.init()
#     #    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
#     #    pygame.display.set_caption("Twister!")
#     #    screen = pygame.display.get_surface()
#     #    self.scene = Scene(screen, self.input)

#     def run(self):
        
#         while True:
#             # Aqui no input.run() que o algoritmo começa a funcionar de verdade
#             self.input.run()

#             # Aqui eu renderizo o resultado da cena
#             self.scene.run()

#     def run_local(self):
#         # Opens the Video file
#         cap = cv2.VideoCapture('./data/input/v1basq_crp.mp4')

#         # Abrindo o video e passando cada frame como parametro
#         frames_array = []
#         get_par = 0
#         while(cap.isOpened()):
#             ret, frame = cap.read()

#             # Getting video parameters
#             if get_par == 0:
#                 height, width, layers = frame.shape
#                 size = (width,height)
#                 get_par = 1

#             self.input.run_local(ret, frame, frames_array)
#             if ret == False:
#                 break
        
#         # Saving all frames as a video
#         out = cv2.VideoWriter('./data/output/result.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
#         for i in range(len(frames_array)):
#             out.write(frames_array[i])
#         out.release()
        

# if __name__ == "__main__":
#     options, remainder = getopt.getopt(sys.argv[1:], 's:x:')
#     for opt, arg in options:
#         if opt in ('-s'):
#             song = arg
#         elif opt in ('-x'):
#             speed = float(arg)
#     game = Twister()
#     #game.run()
#     game.run_local()
