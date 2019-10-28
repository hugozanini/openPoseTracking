SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


import cv2
import pygame

 
def run_local():
        # Opens the Video file
        cap = cv2.VideoCapture('./data/input/v1basq_crp.mp4')

        # Abrindo o video e passando cada frame como parametro
        frames_array = []
        get_par = 0
        while(cap.isOpened()):
            ret, frame = cap.read()

            if get_par == 0:
                height, width, layers = frame.shape
                size = (width,height)
                get_par = 1

            #self.input.run_local(ret, frame, frames_array)
            if ret == False:
                break
            frames_array.append(frame)
        
        # Saving all frames as a video
        out = cv2.VideoWriter('./data/output/result.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
        for i in range(len(frames_array)):
            out.write(frames_array[i])
        out.release()
 
run_local()
# Para fazer a captura de video
# video_capture = cv2.VideoCapture(0)

# cv2.namedWindow("Window")


# while True:
#     ret, frame = video_capture.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     pgImg = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "RGB")
#     print(pgImg)


#     cv2.imshow("Window", frame)

#    #This breaks on 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#video_capture.release()
#cv2.destroyAllWindows()