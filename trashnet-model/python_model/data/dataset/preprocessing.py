import imgaug.augmenters as iaa
import cv2
import glob
import os

data_path=glob.glob("C:/Users/thect/OneDrive/prethesis/trashnet-model/data/dataset/metal/*.jpg")

images=[]

for path in data_path:
   img=cv2.imread(path)
   images.append(img)
   pass

augmentation=iaa.Sequential([
   iaa.Sometimes(0.6, iaa.Fliplr()),
   iaa.Sometimes(0.6, iaa.Flipud()),
   iaa.Sometimes(0.4, iaa.Rotate(-2, 3)),
   iaa.GaussianBlur(0.6),
   iaa.Sometimes(0.4, iaa.ChannelShuffle(channels=[0,1,2])),
])

aug_img=augmentation(images=images)
counter=0

for i in range(0, len(aug_img)):
   filename='metal'+str(i)+'.jpg'
   cv2.imwrite(filename, aug_img[i])
   counter += 1
   if(counter > 100):
      break