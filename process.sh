#!/bin/bash

mkdir -p train
mkdir -p test

wget https://pjreddie.com/media/files/train-images-idx3-ubyte.gz
wget https://pjreddie.com/media/files/train-labels-idx1-ubyte.gz
wget https://pjreddie.com/media/files/t10k-images-idx3-ubyte.gz
wget https://pjreddie.com/media/files/t10k-labels-idx1-ubyte.gz

gunzip train-images-idx3-ubyte.gz
gunzip train-labels-idx1-ubyte.gz
gunzip t10k-images-idx3-ubyte.gz
gunzip t10k-labels-idx1-ubyte.gz

python process_mnist.py

