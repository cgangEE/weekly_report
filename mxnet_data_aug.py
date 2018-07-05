#!/usr/bin/env python
import mxnet as mx
import cv2
import numpy as np

aug_list = mx.image.CreateAugmenter(data_shape=(324, 324, 3), 
        rand_mirror=True, brightness=1.125, contrast=1.125,
        saturation=0.125, pca_noise=0.05, inter_method=1)

example_image = cv2.imread('1.png') 

for aug in aug_list:
    print(aug)
    aug_image = example_image.copy()
    print(aug_image.shape)
    aug_image = aug(mx.nd.array(aug_image))
    print(aug_image.shape)
cv2.imshow('x', aug_image.asnumpy().astype(np.uint8))
cv2.waitKey(0)

