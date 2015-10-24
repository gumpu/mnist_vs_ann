mnist_vs_ann
============

An exploration of the effects of various parameters of an artificial neural network on
its performance on the MNIST dataset.

This makes use of [CXXNET](https://github.com/dmlc/cxxnet).


#Setup

The executable `cxxnet` is installed in one of the directories in your
`$PATH`.

You have Python version 3 installed.

A directory called `Raw` with the following files:

    -rw-r--r-- 1 frans frans     260 Jan  4  2015 README.md
    -rw-r--r-- 1 frans frans 1648877 Jan  2  2015 t10k-images-idx3-ubyte.gz
    -rw-r--r-- 1 frans frans    4542 Jan  2  2015 t10k-labels-idx1-ubyte.gz
    -rw-r--r-- 1 frans frans 9912422 Jan  2  2015 train-images-idx3-ubyte.gz
    -rw-r--r-- 1 frans frans   28881 Jan  2  2015 train-labels-idx1-ubyte.gz

The can be found at <http://yann.lecun.com/exdb/mnist/>.

