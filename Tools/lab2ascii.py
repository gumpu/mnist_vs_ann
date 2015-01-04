
import gzip

with gzip.open('./Raw/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    byte = f.read(4)
    byte = f.read(4)
    for i in range(10000):
        byte = f.read(1)
        print(byte[0])



