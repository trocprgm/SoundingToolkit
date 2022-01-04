import cv2 as cv

testimg = cv.imread('testImage.jpg')
#cv.imshow('image',testimg)
#cv.waitKey(0)

def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
