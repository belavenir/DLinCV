import caffe
import numpy as np
import sys
outfilename='../../meanFiles/npy/stairs.npy'

binaryproto='/usr/prakt/w065/DLinCV/scripts/keras-posenet/meanFiles/binaryproto/stairs.binaryproto'
def getMean(meanFileLocation):
    blob = caffe.proto.caffe_pb2.BlobProto()
    data = open(meanFileLocation, 'rb').read()
    blob.ParseFromString(data)
    arr = np.array(caffe.io.blobproto_to_array(blob))
    return arr[0]


arr = getMean(binaryproto)
np.save(outfilename,arr)
