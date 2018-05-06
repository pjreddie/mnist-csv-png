import os
import scipy.misc
import numpy as np

def get_images(imgf, n):
    f = open(imgf, "rb")
    f.read(16)
    images = []

    for i in range(n):
        image = []
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)
    return images

def get_labels(labelf, n):
    l = open(labelf, "rb")
    l.read(8)
    labels = []
    for i in range(n):
        labels.append(ord(l.read(1)))
    return labels

def output_csv(images, labels, outf):
    o = open(outf, "w")
    for i in range(len(images)):
        o.write(",".join(str(x) for x in [labels[i]] + images[i]) + "\n")
    o.close()

def output_png(images, labels, prefix):
    for i in range(len(images)):
        out = os.path.join(prefix, "%06d-num%d.png"%(i,labels[i]))
        scipy.misc.imsave(out, np.array(images[i]).reshape(28,28))

def csv_and_png(imgf, labelf, prefix, n):
    images = get_images(imgf, n)
    labels = get_labels(labelf, n)
    output_csv(images, labels, "mnist_%s.csv"%prefix)
    output_png(images, labels, prefix)

csv_and_png("train-images-idx3-ubyte", "train-labels-idx1-ubyte", "train", 60000)
csv_and_png("t10k-images-idx3-ubyte",  "t10k-labels-idx1-ubyte",  "test",  10000)

