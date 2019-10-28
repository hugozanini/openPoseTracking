# Multitracking and Pose estimation 

This is an implementation of Openpose and  Deep SORT to do tracking and pose estimation in realtime and local videos. This work is based on [Live Tracker](https://github.com/ortegatron/liveposetracker).

OpenPose :  [Article](https://arxiv.org/pdf/1811.11975.pdf)  | [Code](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
Deep SORT: [Article](https://arxiv.org/pdf/1602.00763.pdf) |  [Code](https://github.com/abewley/sort)

<p align="center">
    <img src="demo.gif", width="480">
</p>

## Requeriments
To run this project, you need to install the following packages:
- [Openpose ]([https://github.com/CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose))
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Numpy](https://pypi.org/project/numpy/)
- [Pygame](https://pypi.org/project/pygame/)
- [Configparser](https://pypi.org/project/configparser/)
- [Pytest-warnings](pip%20install%20pytest-warnings)

It’s recommended to use a virtual  [environment](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3).  A configured docker image is available  as well and can be accessed through this link [put link].

### Compiling pyopenpose
Follow the instructions on [this link](https://medium.com/@robinandreaureni/python-openpose-installation-3fd3a58d4887).

PS: If you are note using a GUI interface, it's important to turn on the python flag  `cmake -DBUILD_PYTHON=ON ..`  before compile OpenPose from your build directory.

### Running the docker container

Docker instructions 
[Run docker EC2](https://michaelsobrepera.com/guides/openposeaws.html)

sudo nvidia-docker-plugin

RUN DOCKER sudo nvidia-docker run -it hugozanini/openpose_tracking:v2

### Project structure
```
📦src  
 ┣ 📂data  
 ┃ ┣ 📂input  
 ┃ ┃ ┗ 📜v1_small.mp4  
 ┃ ┗ 📂output  
 ┣ 📂deep_sort  
 ┃ ┣ 📜detection.py  
 ┃ ┣ 📜iou_matching.py  
 ┃ ┣ 📜kalman_filter.py  
 ┃ ┣ 📜linear_assignment.py  
 ┃ ┣ 📜my_filter.py  
 ┃ ┣ 📜nn_matching.py  
 ┃ ┣ 📜preprocessing.py  
 ┃ ┣ 📜preprocessing.pyc  
 ┃ ┣ 📜track.py  
 ┃ ┣ 📜tracker.py  
 ┃ ┣ 📜__init__.py  
 ┣ 📂model_data  
 ┃ ┗ 📜mars-small128.pb  
 ┣ 📂tools  
 ┃ ┣ 📜freeze_model.py  
 ┃ ┣ 📜generate_detections.py  
 ┃ ┣ 📜__init__.py    
 ┣ 📜Constants.py  
 ┣ 📜Input.py   
 ┣ 📜pose_tracking.py  
 ┣ 📜Scene.py  
 ┣ 📜utils.py  
```
### Running an example

Arguments:
```
[-m] -> Mode: local or realtime
[-i] -> Data input folder
[-o] -> Data output folder
[-x] -> Speed (fps)
```
For a local video:

    python3 pose_tracking.py -m local -i ./data/input/v1_small.mp4 -o ./data/output/v1_small_result.avi -x 30
