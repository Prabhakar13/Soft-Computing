'''
Author    - PRABHAKAR KUMAR
Roll      - IRM2017008
Date      - 7th Feb, 2020
Reference - https://medium.com/mti-technology/how-to-generate-gaussian-samples-3951f2203ab0
'''

import numpy as np
import pylab as plb

# Function to generate Gussian/Normal samples in
# two dimensions, whose x and y coords are independent
# standard normals
def gauss_func(distribution1,distribution2):
  normal_1=np.sqrt(-2*np.log(distribution1))*np.cos(2*np.pi*distribution2)
  normal_2=np.sqrt(-2*np.log(distribution1))*np.sin(2*np.pi*distribution2)
  return normal_1,normal_2

# Generating two uniform samples
uniform1=np.random.rand(1000)
uniform2=np.random.rand(1000)


normal_1,normal_2=gauss_func(uniform1,uniform2)

# Plotting the figures using Pylab
plb.figure()
plb.subplot(221)
plb.hist(uniform1)
plb.subplot(222)
plb.hist(uniform2)
plb.subplot(223)
plb.hist(normal_1,color="yellow")
plb.subplot(224)
plb.hist(normal_2,color="yellow")
plb.show()