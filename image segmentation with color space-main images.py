#!/usr/bin/env python
# coding: utf-8

# # Segmentation with color spaces HSV & RGB

# ## import libraries 

# In[7]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors


# ## add images to a list

# In[8]:


path = "./pic_color/plant"

images = []
for i in range(1,18):

    image = cv2.cvtColor(cv2.imread(path +" "+ '('+str(i)+')' + ".png"), cv2.COLOR_BGR2RGB)
    images.append(image)


# ## Add all the steps to a function

# In[9]:


def segment_image(image):
    ''' Attempts to segment the white spots out of the provided image '''

    # Convert the image into HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    
    # Set a yellow range
    light_yellow = (47/2, (53/100) * 255, (60/100) * 255) 
    dark_yellow = (50/2, (100/100) * 255, (100/100) * 255)

    # Apply the white mask
    mask = cv2.inRange(hsv_image, light_yellow, dark_yellow)

    
    result = cv2.bitwise_and(image, image, mask=mask)
    return result


# ## get the results

# In[10]:


results = [segment_image(image) for image in images]


# # plot

# In[14]:


for i in range(17):
    print('i is=',i)
    plt.subplot(1, 2, 1)
    plt.imshow(images[i])
    plt.xlabel('original')
    plt.subplot(1, 2, 2)
    plt.imshow(results[i])
    plt.xlabel('masked')
    #plt.savefig(r'C:\Users\asus\Desktop\notebooks\results\res'+ str(i+1))
    plt.show()
   


# In[ ]:




