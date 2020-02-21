from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from random import normalvariate
import numpy as np
from numpy.dual import norm
from math import sqrt


# reading the image
img = Image.open('/Users/sana/Downloads/2a/sample.jpg')
imggray = img.convert('LA')
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])

def random_unit_vector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    the_norm = sqrt(sum(x * x for x in unnormalized))
    return [x / the_norm for x in unnormalized]


def first_pc(a):
    epsilon = 1e-10
    a = np.array(a, dtype=float)
    cov = a.dot(a.T)
    n = cov.shape[0]
    x = random_unit_vector(n)
    current_v = x

    while True:
        last_v = current_v
        current_v = np.dot(cov, last_v)
        current_v = current_v / norm(current_v)

        if abs(np.dot(current_v, last_v)) > 1 - epsilon:
            return current_v
n = 10 #n inja meghdar dehi mishavad ke haman m khaste shode ruye masale ast
q = np.zeros((n,836))
q[0] = first_pc(imgmat)
s = np.zeros((836,600))
for x in range(1,n):
    o = np.zeros((x,836))
    for i in range(0,x):
        o[i]=q[i]
    f = np.dot(np.transpose(o),o)
    for i in range(0,600):
        np.transpose(s)[i] = (np.transpose(imgmat)[i]-np.dot(f,np.transpose(imgmat)[i]))
    q[x]= first_pc(s)

# showing the image
o = np.zeros((n,836))
for i in range(0,n):
    o[i]=q[i]
f = np.dot(np.transpose(o),o)
plt.style.use('classic')
plt.imshow(np.dot(f,imgmat), cmap='gray')
title = "Original Image"
plt.title(title)
plt.show()
