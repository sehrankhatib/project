import os
import cv2

path = r"C:\Users\Sehran Khatib\Downloads\PRO-C105-Project-Images-main\PRO-C105-Project-Images-main\Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file       
        images.append(file_name)
        
#print(images)
count = len(images)

frame = cv2.imread(images[0])
# print(frame.shape)
height, width, channels = frame.shape
size = (width,height)
#print(size)

output = cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#For SUNSET
# for i in range(0,count-1,1):

#For SUNRISE
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)


    
output.release() # releasing the video generated
print("Done")