
# for loop
for i in xrange(n): 
    print(i)


# start index
0


# read file
f = open(fileName)
for line in f:
    print(line)

# random integer    # return a random integer N such that a <= N <= b
import random
random.randint(a, b)    

# function
def func(parameter):
    print(parameter)



# string lib
['s', 'df'] = 's df'.split(' ')
1 = 'sfds'.find('fd')    


#travel folder recursively
for parent, dirnames, filenames in os.walk(folder):


# sort list
x = [1, 3, 2]
x = sorted(x)    # then x = [1, 2, 3]


#join path
os.path.join('dir', 'filename')


#file copy, remove, move and create symbolic link
shutil.copyfile(src, dst)
os.remove(fullFilename)
os.rename(srcFullFilename, dstFullFilename)
    # cannot move file between different device        
os.symlink(src, dstLink)


#file exist
os.path.isfile(filename)

#dir exist
os.path.isdir(dirname)

# mkdir
os.mkdir(dirname)


#regard function as attribute
@property
class Person(object):
    def __int__(self):
        self._money = 100

    def money(self):
        return self._money

person = Person()
print(person.money)


# dimention
npObj.shape

# block comment
'''
    block
'''

# process xml
import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()
for elem in root.findall('object')
    if elem.find('name') == 'ignore':
        root.remove(elem)
tree.write(detFilename)

# copy
import copy
class f:
    x = 1
l = [f(), f()]
a = copy.copy(l)
b = copy.deepcopy(l)
b[0].x = 2        # b = [x = 2, x = 1]    l = [x = 1, x = 1] # deep
a[0].x = 3         # a = [x = 3, x = 1]    l = [x = 3, x = 1] # shallow

# get image size     
import PIL
print(PIL.Image.open(imagename).size)  # 8.55e-5 sec

print(PIL.Image.open(imagename).size)  # W x H

# PIL Image read and write
im = PIL.Image.open(imagename)
im.save(imname)
                                      

# opencv
    import cv2
    im = cv2.imread(imageName)        # im is np.uint8 np.array type
                                      # 2.918e-3 sec

    print(cv2.imread(imname).shape)   # H x W x C

    # draw a circle in image
    cv2.circle(image, (x,y), radius, color, thickness)     
    
    # convert image to gray type
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # capture
    capture = cv2.VideoCapture(0)
    while True:
        ret, img = capture.read()
        cv2.imshow('x', img)
        cv2.waitKey(1)


# cPickle
import cPickle
with open(filename, 'wb') as fOutput:            # write object
    cPickle.dump(object , fOutput, cPickle.HIGHEST_PROTOCOL)

with open(filename, 'rb') as fInput:            # load object
    object = cPickle.load(fInput)


# json
ipmort json
with open(filename) as f:
    data = json.load(f)                         # load json from file

with open(filename) as f:                       # save json to file
    json.dump(data, f)

# numpy 
    # swap numpy array axis
    img.shape : (123, 456, 3)
    img.transpose(2, 0, 1).shape : (3, 123, 456)


    # maximum element idx
    return np.unravel_index(np.argmax(data), data.shape)

    # 2d convolve
    import scipy
    scipy.signal.convolve2d(data, filter, boundary='fill', mode='same')

    # fft convolve, zero padding
    scipy.signal.fftconvolve(data, filter, mode='same')

    # load string list from file
    strList = np.loadtxt('list.txt', delimiter='\n', dtype=str)

    # save string list to file
    np.savetxt('list.txt', strList, fmt='%s')

    # construct an array by repeating A the number of times given by reps
    np.tite(A, reps)

    # return sorted 1D array of commom and unique elements
    np.intersect1d(arr1, arr2)

# plt
    import matplotlib.pyplot as plt
    plt.bar(x, height)

# print without newline
    import sys
    sys.stdout.write(str)

# remove single-dimensional entries from numpy array
    dst = np.squeeze(array)

# argument parse
    import argparse
    parser = argparse.ArgumentParser(description='ft up')
    parser.add_argument('--ft', dest='ft', type=str)
    args = parser.parse_args()

# get imported module path
    import module
    print module.__file__
